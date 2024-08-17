import cv2
import numpy as np
from datetime import datetime

# Function to add timestamp to the frame
def add_timestamp(frame):
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    cv2.putText(frame, timestamp, (10, frame.shape[0] - 10),
                cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 2, cv2.LINE_AA)
    cv2.rectangle(frame, (0, frame.shape[0] - 30), (200, frame.shape[0]), (255, 255, 0), -1)
    return frame

# Motion detection function
def detect_motion(frame, prev_frame):
    diff = cv2.absdiff(frame, prev_frame)
    gray_diff = cv2.cvtColor(diff, cv2.COLOR_BGR2GRAY)
    _, thresh = cv2.threshold(gray_diff, 25, 255, cv2.THRESH_BINARY)
    count = np.count_nonzero(thresh)
    return count > 1000  # Adjust threshold as needed

# Main function
def main():
    rtsp_link = r'rtsp://localhost:8554/stream'  # Replace with your RTSP link
    cap = cv2.VideoCapture(rtsp_link)

    if not cap.isOpened():
        print("Error: Couldn't open RTSP stream.")
        return

    prev_frame = None
    frame_counter = 0
    save_interval = 60  # Save frames every 60 seconds

    while True:
        ret, frame = cap.read()
        if not ret:
            print("Error: Couldn't read frame.")
            break

        frame = add_timestamp(frame)
        current_time = datetime.now()

        if prev_frame is not None:
            if detect_motion(frame, prev_frame):
                filename = f"motion_{current_time.strftime('%Y%m%d_%H%M%S')}.jpg"
                cv2.imwrite(filename, frame)
                print(f"Motion detected! Saved frame as {filename}")

        # Save frame for logging every `save_interval` seconds
        if frame_counter % (save_interval * int(cap.get(cv2.CAP_PROP_FPS))) == 0:
            filename = f"regular_{current_time.strftime('%Y%m%d_%H%M%S')}.jpg"
            cv2.imwrite(filename, frame)
            print(f"Saved frame as {filename}")

        prev_frame = frame
        frame_counter += 1

        cv2.imshow('Video Stream', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == '__main__':
    main()
