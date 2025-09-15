class FileError(Exception):
    pass

class DirNotFoundError(FileError):
    """Error if path is not a directory

    Args:
        FileError (path): path to check
    """
    def __init__(self, path):
        super().__init__(f"Directory not found: {path}")
        self.path = path

class FileNotFoundError(FileError):
    """Error if file path is not found

    Args:
        FileError (path): path to check
    """
    def __init__(self, path):
        super().__init__(f"{path} cannot be found")
        super.path = path

class NoVideosInDirError(FileError):
    """Error if no video files in directory

    Args:
        FileError (path): Directory path to check for videos
    """
    def __init__(self, path):
        super().__init__(f"No videos in {path}")
        self.path = path

class NotMP4Error(FileError):
    """Error if file is not mp4

    Args:
        FileError (path): Path to file to check
    """
    def __init__(self, path):
        super().__init__(f"{path} is not an MP4")
        super.path = path

class FileAlreadyExistsError(FileError):
    """Error if file path already exists

    Args:
        FileError (path): Path to check
    """
    def __init__(self, path):
        super().__init__(f"Cannot rename to {path}. File already exists.")
        super.path = path