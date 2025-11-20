//Based on BRAW SDK ExtractAudio.cpp example

#include "BlackmagicRawAPI.h"
#include "braw_wrapper.h"

#include <stdio.h>
#include <iostream>


std::vector<float> resample_linear(const std::vector<float>& input, uint32_t inRate, uint32_t outRate = 16000) {
    if (input.empty() || inRate == 0) return {};

    double ratio = double(outRate) / double(inRate);
    size_t outLen = size_t(input.size() * ratio);

    std::vector<float> output(outLen);

    for (size_t i = 0; i < outLen; i++) {
        double pos = double(i) / ratio;
        size_t idx = size_t(pos);

        if (idx >= input.size() - 1) {
            output[i] = input.back();
        } else {
            float frac = float(pos - idx);
            output[i] = input[idx] * (1.0f - frac) + input[idx + 1] * frac; // linear interpolation
        }
    }

    return output;
}


py::array_t<float> OutputAudioArray(IBlackmagicRawClipAudio* audio, HRESULT& result) 
{
    result = S_OK;

    uint64_t audioSamples;
    uint32_t bitDepth;
    uint32_t channelCount;
    uint32_t sampleRate;

    result = audio->GetAudioSampleCount(&audioSamples);
    if (result != S_OK) return {};

    result = audio->GetAudioBitDepth(&bitDepth);
    if (result != S_OK) return {};

    result = audio->GetAudioChannelCount(&channelCount);
    if (result != S_OK) return {};

    result = audio->GetAudioSampleRate(&sampleRate);
    if (result != S_OK) return {};

    std::vector<float> mono;
    mono.reserve(audioSamples);

    static constexpr uint32_t maxSampleCount = 48000;
    uint32_t bufferBytes = (maxSampleCount * channelCount * bitDepth) / 8;

    std::vector<uint8_t> raw(bufferBytes);

    uint64_t index = 0;
    while (index < audioSamples)
    {
        uint32_t samplesRead = 0;
        uint32_t bytesRead = 0;

        result = audio->GetAudioSamples(
            index,
            raw.data(),
            bufferBytes,
            maxSampleCount,
            &samplesRead,
            &bytesRead
        );

        if (result != S_OK) return {};
        if (samplesRead == 0) break;

        const uint8_t* ptr = raw.data();

        for (uint32_t i = 0; i < samplesRead; i++)
        {
            float sum = 0.0f;

            for (uint32_t ch = 0; ch < channelCount; ch++)
            {
                float s = 0.0f;

                if (bitDepth == 16)
                {
                    int16_t v = *(int16_t*)ptr;
                    ptr += 2;
                    s = float(v) / 32768.0f;
                }
                else if (bitDepth == 24)
                {
                    int32_t v = (ptr[0] | (ptr[1] << 8) | (ptr[2] << 16));
                    if (v & 0x800000) v |= ~0xFFFFFF;
                    ptr += 3;
                    s = float(v) / 8388608.0f;
                }
                else if (bitDepth == 32)
                {
                    float v = *(float*)ptr;
                    ptr += 4;
                    s = v;
                }

                sum += s;
            }

            mono.push_back(sum / float(channelCount));
        }

        index += samplesRead;
    }

    // ---- RESAMPLE TO 16 KHZ ----
    std::vector<float> resampled = resample_linear(mono, sampleRate, 16000);

    // ---- CONVERT TO NUMPY ----
    py::array_t<float> arr(resampled.size());
    std::memcpy(arr.mutable_data(), resampled.data(), resampled.size() * sizeof(float));
    return arr;
}



py::array_t<float> BRAW_extract_raw_audio(const std::string &clipName){
    HRESULT result = S_OK;

    IBlackmagicRawFactory* factory = nullptr;
	IBlackmagicRaw* codec = nullptr;
	IBlackmagicRawClip* clip = nullptr;
	IBlackmagicRawClipAudio* audio = nullptr;

    do
	{
		factory = CreateBlackmagicRawFactoryInstanceFromPath(BRAW_LIB_PATH.c_str());
		if (factory == nullptr)
		{
			std::cerr << "Failed to create IBlackmagicRawFactory!" << std::endl;
			break;
		}

		result = factory->CreateCodec(&codec);
		if (result != S_OK)
		{
			std::cerr << "Failed to create IBlackmagicRaw!" << std::endl;
			break;
		}

		result = codec->OpenClip(clipName.c_str(), &clip);
		if (result != S_OK)
		{
			std::cerr << "Failed to open IBlackmagicRawClip!" << std::endl;
			break;
		}

		result = clip->QueryInterface(IID_IBlackmagicRawClipAudio, (void**)&audio);
		if (result != S_OK)
		{
			std::cerr << "Failed to get IBlackmagicRawClipAudio!" << std::endl;
			break;
		}

        py::array_t<float> audiobuffer;
		audiobuffer = OutputAudioArray(audio, result);

	} while(0);

	if (audio != nullptr)
		audio->Release();

	if (clip != nullptr)
		clip->Release();

	if (codec != nullptr)
		codec->Release();

	if (factory != nullptr)
		factory->Release();

    if (result != S_OK)
        throw std::runtime_error("Failed to extract audio");

    return audiobuffer;
}
