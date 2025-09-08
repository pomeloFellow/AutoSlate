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