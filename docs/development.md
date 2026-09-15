# AutoSlate

## Pipeline
General Process Steps
- File path & type validation
- Extract audio data from video
    - Convert to Whisper format
- Detect text & confidence with Whisper
- Get key words/info from text
- Convert to file name
- Rename file

## User Controls/Indicators
Indicators
- Progress/Current Stage
- Result text & confidence
- Any errors

Controls
- Search Range (fromTime, toTime)
- Minimum confidence
- File rename approval

## Systems
The GUI allows the user to specify a file/folder of videos and file relabeling settings.

Relabeling is per file - application logic handles interating through folder. First, validate and get the video file type. Based on that type, extract raw audio data - trimmed to user defined search range. Using Whisper, find slate call. Convert detected speech to file name. Return old & new file name suggestion, confidence, or errors.

GUI displays: old file name, new file name, confidence, (or errors): for all files processed.
Allow user to adjust new file names and apply them.

## Improvements
- Maybe allow for online audio recognition use instead of local model?
- Produce log per operation? 
- Update file metadata as well?