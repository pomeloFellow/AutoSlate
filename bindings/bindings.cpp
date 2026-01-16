#include <pybind11/pybind11.h>
#include <pybind11/numpy.h>

#include "braw_wrapper.h"

namespace py = pybind11;

py::array_t<float> BRAW_extract_wrapper(const std::string& path) {
    return BRAW_extract_raw_audio(const_cast<char*>(path.c_str()));
}

PYBIND11_MODULE(braw_extension, m) {
    m.doc() = "Python bindings for BRAW audio extraction";

    m.def(
        "BRAW_extract_raw_audio",
        &BRAW_extract_wrapper,
        py::arg("path"),
        "Extract raw audio from a .braw file and return float32 mono 16000 Hz numpy array"
    );
}
