# Export Video Frames

A simple Python script to extract frames from video files at specified intervals or time points.

## Features

- Extract frames at regular intervals (e.g., every 1 second)
- Extract frames at specific time points
- Support for various time formats (HH:MM:SS, MM:SS, or seconds)
- Progress bar showing extraction status

## Requirements

- Python 3.6+
- OpenCV (cv2)
- tqdm

## Installation

1. Clone this repository:
```bash
git clone https://github.com/zenenznze/Export-video-frames.git
```

2. Install required packages:
```bash
pip install -r requirements.txt
```

## Usage

```bash
python extract_frames.py video_path [--output_dir frames] [--interval 1] [--time_points "00:01:23" "01:30" "45"]
```

### Arguments

- `video_path`: Path to the input video file
- `--output_dir`: Output directory for frames (default: 'frames')
- `--interval`: Time interval between frames in seconds (default: 1)
- `--time_points`: List of specific time points to extract frames from (format: HH:MM:SS or MM:SS or seconds)

### Examples

1. Extract frames every 2 seconds:
```bash
python extract_frames.py video.mp4 --interval 2
```

2. Extract frames at specific time points:
```bash
python extract_frames.py video.mp4 --time_points "00:01:23" "01:30" "45"
```

## License

MIT License
