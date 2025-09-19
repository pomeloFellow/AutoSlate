class AudioError(Exception):
    def __init__(self, text):
        super().__init__(text)

class EmptyAudioBuffer(AudioError):
    def __init__(self):
        super().__init__("Audio buffer empty")

class BufferHasInfValues(AudioError):
    def __init__(self):
        super().__init__("Audio buffer has inf values")

class AudioBufferTooSmall(AudioError):
    def __init__(self):
        super().__init__("Audio clip too short")

class TranscriberError(AudioError):
    def __init__(self, text):
        super().__init__(text)
