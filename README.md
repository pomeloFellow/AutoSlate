# Set Up in WSL (VSCode):

## Install python 3.10 or later
`sudo apt install python3 python3-venv python3-pip -y`

## Create virtual environment
`python3 -m venv venv`

## Activate virtual environment
`source venv/bin/activate`

## Upgrade pip
`pip install --upgrade pip`

## Install packages
`pip install opencv-python ffmpeg-python librosa pytesseract faster-whisper typer`\
`sudo apt install tesseract-ocr -y`\
`sudo apt install ffmpeg -y`

## Run from root
NOTE: BE AWARE OF "/" or "\" convention
`python -m src.main -i "<input folder>"`

# Dev Road Map
- [x] File system (open,rename,text->filename)
- [ ] GUI
- [ ] Audio processor
    - [x] Get audio
        - [x] .mp4
        - [ ] .braw
    - [x] Preprocessing (Noise Reduction)
    - [x] Detect slate clap
    - [x] Find slate call
    - [x] Transcribe
- [ ] Video processor
    - [ ] Get frames
    - [ ] Preprocessing
    - [ ] Transcribe
- [ ] Additional Perameters
    - [ ] Rely on video cue only
    - [ ] Rely on audio cue only
    - [ ] Accept only above a certain confidence for video
    - [x] Accept only above a certain confidence for audio
    - [x] Print confidence for each video
    - [x] User set time chunk to check