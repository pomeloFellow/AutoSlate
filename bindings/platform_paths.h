#ifdef _WIN32
    #define BRAW_LIB_PATH "blackmagic_sdk/windows/lib"
#elif __APPLE__
    #define BRAW_LIB_PATH "blackmagic_sdk/macos/Include/BlackmagicRawAPI.h"
#elif __linux__
    #define BRAW_LIB_PATH "blackmagic_sdk/linux/lib"
#else
    #error "Unsupported platform"
#endif
