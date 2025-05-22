# RTSP Motion Detector with Timestamp and Frame Logging

This Python script connects to an RTSP camera stream, detects motion via pixel difference analysis, overlays timestamps on frames, and saves them on motion detection or regular intervals.

## Features

- 🟡 Overlay timestamps with a visual background strip
- 📹 Real-time RTSP stream display
- 📦 Saves frames on:
  - Motion detection
  - Regular time intervals (based on frame count and FPS)
- ⚙️ Simple motion detection using pixel difference count

## Prerequisites

- Python 3.7 or higher
- An RTSP camera or local RTSP stream URL

## Installation

1. Clone the repo or download the script.
2. Install required packages:

```bash
pip install -r requirements.txt
````

3. Update the script:

```python
rtsp_link = r'rtsp://localhost:8554/stream'  # Replace with your RTSP link
```

## Usage

Run the script:

```bash
python motion_capture.py
```

## Output

* Motion frames: `motion_YYYYMMDD_HHMMSS.jpg`
* Regular frames: `regular_YYYYMMDD_HHMMSS.jpg`

## Notes

* Motion detection sensitivity is adjustable via:

```python
return count > 1000  # Lower = more sensitive
```

* Change `save_interval` to adjust regular snapshot frequency (in seconds).

