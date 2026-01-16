#include <pybind11/pybind11.h>
#include <pybind11/numpy.h>
#include "BlackmagicRawAPI.h"
#include <stdio.h>
#include <iostream>

namespace py = pybind11;

std::vector<float> resample_linear(const std::vector<float>& input, uint32_t inRate, uint32_t outRate);
py::array_t<float> OutputAudioArray(IBlackmagicRawClipAudio* audio, HRESULT& result);
py::array_t<float> BRAW_extract_raw_audio(const std::string &clipName);

py::array_t<float> BRAW_extract_wrapper(const std::string& path);