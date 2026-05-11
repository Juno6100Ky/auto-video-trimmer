import subprocess
import argparse  #in new replace with input()
from pathlib import Path

def get_output_name(input_path):
    """Generate the unique name like filename_p1.mp4, filename_p2.mp4, etc."""
    p = Path(input_path)
    base_name = p.stem
    suffix = p.suffix

    counter =1
    while True:
        candidate = p.with_name(f"{base_name}_p{counter}{suffix}")
        if not candidate.exists():
            return str(candidate)
        counter += 1

def trim_video(input_path, start, duration):
    output_path = get_output_name(input_path)

    """Trim a video using ffmpeg"""
    command = [
        'ffmpeg', 
        '-ss', start, 
        '-i', input_path,
        '-t', duration,
        '-c', 'copy',
        output_path]
    
    try:
        subprocess.run(command, check=True)
        print(f"\n✅ Success! saved as: {output_path}")
    except subprocess.CalledProcessError as ce:
        print(f"\n❌ ffmpeg failed! Check your timestamps or file format.")
    except FileNotFoundError:
        print("Error: ffmpeg is not instlled or not in your file path.")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description =  "Fast video trimmer CLI")
    parser.add_argument("-i","--input", required = True, help="Input video file")
    parser.add_argument("-ss", "--start", required = True, help="Start time (HH:MM:SS)")
    parser.add_argument("-t", "--duration", required = True, help="Duration (HH:MM:SS)")
    args = parser.parse_args()

    trim_video(args.input, args.start, args.duration)