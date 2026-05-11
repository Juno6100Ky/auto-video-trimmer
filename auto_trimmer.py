import subprocess #for runnind commands in terminal
from pathlib import Path # for handling file path


def get_video_duration(input_path):
    """Check the video is valid and get its duration with ffprobe"""
    command = ['ffprobe', '-v', 'error', '-show_entries', 'format=duration', '-of', 'default=noprint_wrappers=1:nokey=1', input_path]
    try:
        result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, check=True)
        return float(result.stdout.strip())
    except subprocess.CalledProcessError:
        return None
    

def auto_segment_video(input_path, segment_duration):
    """Automatically segment the video and save with unique names"""
    p = Path(input_path)
    if not p.exists():
        print(f"❌ Error: The file at {input_path} does not exists.")
        return
    duration = get_video_duration(input_path)
    if duration is None:
        print(f"❌ Error: Could not read the video. It might be corrupted or invalid media file.")
        return
    print(f"\n✅ Video found! Total duration: {duration/60:.2f} minutes.")
    print(f"⏱️ Splitting the entire video into chuncks of {segment_time} minutes.")
    
    base_name = p.stem
    suffix = p.suffix
    output_pattern = str(p.with_name(f"{base_name}_05min_part%02d{suffix}"))
    command = [
        'ffmpeg', 
        '-i', str(p), 
        '-c', 'copy',
        '-f', 'segment',
        '-segment_time', segment_time,
        '-reset_timestamps', '1',
        output_pattern]
    try:
        subprocess.run(command, check=True)
        print(f"\n✅ Success! All segments saved in: {p.parent}")

    except subprocess.CalledProcessError:
        print(f"\n❌ ffmpeg failed! ffmpeg failed to process. Check your segment time or file format.")
        
        
if __name__ == "__main__":
    print("***Python Video Auto-Segmenter***")
    raw_path = input("Enter the full path of the video file: ").strip()
    if raw_path.startswith('"') and raw_path.endswith('"'):
        clean_path = raw_path[1:-1]
    elif raw_path.startswith("'") and raw_path.endswith("'"):
        clean_path = raw_path[1:-1]
    else:
        clean_path = raw_path

    segment_time = input("Enter the segment duration for each chunk (e.g., 00:05:00): ").strip()

    auto_segment_video(clean_path, segment_time)

