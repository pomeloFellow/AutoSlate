# entry point for application
from src.core.core import relabel_videos
import argparse


def main():
    parser = argparse.ArgumentParser(
                        prog='AutoSlate',
                        description='Rename video files based on slate in audio and video')
    
    # arguments/ flags
    parser.add_argument("--input", "-i", required=True, help="Path to input folder")
    parser.add_argument("--start_time", "-st", required=False, default=0)
    parser.add_argument("--min_time", "-mt", required=False, default=-1)
    parser.add_argument("--min_confidence", "-mc",required=False, default=-1)

    # args creation
    args = parser.parse_args()

    # core logic
    relabel_videos(args.input, int(args.start_time), int(args.min_time), float(args.min_confidence))


if __name__ == "__main__":
    main()