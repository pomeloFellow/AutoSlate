#include "BlackmagicRawAPI.h";

std::vector<float> resample_linear(const std::vector<float>& input, uint32_t inRate, uint32_t outRate = 16000);
py::array_t<float> OutputAudioArray(IBlackmagicRawClipAudio* audio, HRESULT& result);
py::array_t<float> BRAW_extract_raw_audio(const std::string &clipName);

