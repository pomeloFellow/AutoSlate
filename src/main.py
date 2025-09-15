# entry point for application
from src.core.core import relabel_videos
import argparse


def main():
    parser = argparse.ArgumentParser(
                        prog='AutoSlate',
                        description='Rename video files based on slate in audio and video')
    
    # arguments/ flags
    parser.add_argument("--input", "-i", required=True, help="Path to input folder")

    # args creation
    args = parser.parse_args()

    # core logic
    relabel_videos(args.input)




if __name__ == "__main__":
    main()