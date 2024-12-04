import os
import argparse
import cv2
from tqdm import tqdm

def time_to_seconds(time_str):
    """将时间字符串（HH:MM:SS）转换为秒数"""
    try:
        time_parts = time_str.split(':')
        if len(time_parts) == 3:
            hours, minutes, seconds = map(float, time_parts)
            return hours * 3600 + minutes * 60 + seconds
        elif len(time_parts) == 2:
            minutes, seconds = map(float, time_parts)
            return minutes * 60 + seconds
        else:
            return float(time_str)
    except:
        raise ValueError("时间格式无效。请使用 HH:MM:SS 或 MM:SS 或秒数")

def extract_frames(video_path, output_dir, interval=None, time_points=None):
    """
    从视频中提取帧
    :param video_path: 视频文件路径
    :param output_dir: 输出目录
    :param interval: 提取帧的时间间隔（秒）
    :param time_points: 指定时间点列表（可选）
    """
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    # 清空输出目录中的旧文件
    for f in os.listdir(output_dir):
        if f.endswith('.jpg'):
            os.remove(os.path.join(output_dir, f))
    
    cap = cv2.VideoCapture(video_path)
    if not cap.isOpened():
        print("无法打开视频文件")
        return
    
    fps = cap.get(cv2.CAP_PROP_FPS)
    total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    duration = total_frames / fps
    
    try:
        if time_points:
            # 按指定时间点提取帧
            print(f"\n总共需要提取 {len(time_points)} 个时间点的帧")
            for time_point in tqdm(time_points, desc="提取进度"):
                seconds = time_to_seconds(time_point)
                frame_number = int(seconds * fps)
                
                cap.set(cv2.CAP_PROP_POS_FRAMES, frame_number)
                ret, frame = cap.read()
                if ret:
                    output_path = os.path.join(output_dir, f'frame_{time_point.replace(":", "_")}.jpg')
                    cv2.imwrite(output_path, frame)
        
        else:
            # 按时间间隔提取
            interval_value = interval if interval else 1
            frame_interval = int(fps * interval_value)
            total_frames_to_extract = int(duration / interval_value)
            
            print(f"\n视频总长: {duration:.1f}秒")
            print(f"预计提取: {total_frames_to_extract} 帧")
            
            frame_count = 0
            saved_count = 0
            
            with tqdm(total=total_frames_to_extract, desc="提取进度") as pbar:
                while True:
                    ret, frame = cap.read()
                    if not ret:
                        break
                    
                    if frame_count % frame_interval == 0:
                        output_path = os.path.join(output_dir, f'frame_{saved_count}.jpg')
                        cv2.imwrite(output_path, frame)
                        saved_count += 1
                        pbar.update(1)
                    
                    frame_count += 1
            
            print(f"\n成功提取了 {saved_count} 帧到目录: {output_dir}")
    
    finally:
        cap.release()

def main():
    parser = argparse.ArgumentParser(description='从视频中提取帧')
    parser.add_argument('video_path', help='输入视频文件的路径')
    parser.add_argument('--output_dir', help='输出目录路径', default='frames')
    parser.add_argument('--interval', type=float, help='提取帧的时间间隔（秒），例如：2表示每隔2秒提取一帧')
    parser.add_argument('--time_points', nargs='+', help='指定时间点列表（格式：HH:MM:SS 或 MM:SS），例如：00:01:23 01:30 45')
    
    args = parser.parse_args()
    
    # 如果output_dir是相对路径，将其转换为绝对路径
    if not os.path.isabs(args.output_dir):
        args.output_dir = os.path.join(os.path.dirname(args.video_path), args.output_dir)
    
    extract_frames(args.video_path, args.output_dir, args.interval, args.time_points)

if __name__ == '__main__':
    main()
