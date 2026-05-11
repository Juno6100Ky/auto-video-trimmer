# Auto Video Automation Suite 

A Python-based automation tool for rapid video processing using FFmpeg. 
The tool is designed to solve the problem of trimming large (1GB+) files instantly without the heavy CPU overhead of traditional video editors.

#🚀 The Problem & The Solution
Traditional video editing software re-encodes files, which takes significant time/CPU power and change the video quality.

These scripts utilize **FFmpeg Stream Copying**, making the task **I/O-Bound**. Instead of re-rendering, the scripts "slice" the video stream, 
resulting in near-instant processing while maintaining original quality.

## 🛠 Features
This repository includes two versions of the automation tool:

**Target User:** General use and batch processing of trimming.

### 1. `ffmpeg-auto.py` (Initial version)
- **Interface:** Command-line arguments using `argparse`.
- **Functionality:** Precise trimming of specific segments using `-ss` and `-t` flags.

### 2. `auto-trimmer.py` (Interactive & Automatic)
- **Interface:** Interactive `input()` prompts.
- **Functionality:** - Automatically segments an entire video into equal parts.
  - Handles file path cleaning (auto-removes quotes).
  - Includes `ffprobe` validation to check for file corruption before processing.

## 🔧 Technical Stack
- **Language:** Python 3.12+
- **Core Engine:** FFmpeg / FFprobe
- **Libraries:** `subprocess` (System execution), `pathlib` (Modern path management), `argparse`.

## 📦 Installation & Usage
1. **Prerequisites:** Ensure FFmpeg is installed on your system:

   -**for Linux**
   ```bash
   sudo apt update && sudo apt install ffmpeg

2. **Run the interactive tool**
   ```bash
   python3 auto-trimmer.py
