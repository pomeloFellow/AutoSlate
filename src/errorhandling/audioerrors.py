class AudioError(Exception):
    pass

def empty_audio_buffer(AudioError):
    def __init__(self):
        super().__init__(f"Audio buffer empty")

def buffer_as_inf_values(AudioError):
    def __init__(self):
        super().__init__(f"Audio buffer has inf values")

def audio_buffer_too_small(AudioError):
    def __init__(self):
        super().__init__(f"Audio clip too short")

def transcriber_error(AudioError):
    def __init__(self):
        super().__init__(f"No text key in dict")