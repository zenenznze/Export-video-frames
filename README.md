# Export Video Frames / 视频帧导出工具

A simple Python script to extract frames from video files at specified intervals or time points.

一个简单的 Python 脚本，用于从视频文件中按指定时间间隔或时间点提取帧。

## Features / 功能特点

- Extract frames at regular intervals (e.g., every 1 second)
- Extract frames at specific time points
- Support for various time formats (HH:MM:SS, MM:SS, or seconds)
- Progress bar showing extraction status

- 按固定时间间隔提取帧（例如：每1秒一帧）
- 在指定时间点提取帧
- 支持多种时间格式（时:分:秒，分:秒，或秒数）
- 显示提取进度条

## Requirements / 环境要求

- Python 3.6+
- OpenCV (cv2)
- tqdm

## Installation / 安装方法

1. Clone this repository / 克隆此仓库:
```bash
git clone https://github.com/zenenznze/Export-video-frames.git
```

2. Install required packages / 安装所需包:
```bash
pip install -r requirements.txt
```

## Usage / 使用方法

```bash
python extract_frames.py video_path [--output_dir frames] [--interval 1] [--time_points "00:01:23" "01:30" "45"]
```

### Arguments / 参数说明

- `video_path`: Path to the input video file / 输入视频文件的路径
- `--output_dir`: Output directory for frames (default: 'frames') / 帧输出目录（默认：'frames'）
- `--interval`: Time interval between frames in seconds (default: 1) / 提取帧的时间间隔，以秒为单位（默认：1）
- `--time_points`: List of specific time points to extract frames from / 指定要提取帧的时间点列表
  - Format / 格式: HH:MM:SS or MM:SS or seconds / 时:分:秒 或 分:秒 或 秒数

### Examples / 使用示例

1. Extract frames every 2 seconds / 每2秒提取一帧:
```bash
python extract_frames.py video.mp4 --interval 2
```

2. Extract frames at specific time points / 在指定时间点提取帧:
```bash
python extract_frames.py video.mp4 --time_points "00:01:23" "01:30" "45"
```

## Notes / 注意事项

1. The script uses OpenCV for video processing, ensuring fast and stable performance.
   脚本使用 OpenCV 处理视频，确保快速稳定的性能。

2. Extracted frames are saved as JPEG files in the output directory.
   提取的帧以 JPEG 格式保存在输出目录中。

3. The progress bar shows real-time extraction status and estimated time remaining.
   进度条显示实时提取状态和预计剩余时间。

4. If the output directory already exists, old frame files will be cleared before extraction.
   如果输出目录已存在，提取前会清理旧的帧文件。

## License / 许可证

MIT License / MIT 许可证
