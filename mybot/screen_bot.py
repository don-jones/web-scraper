import time
import cv2
import mss
import numpy as np

# --- CONFIGURATION ---
OUTPUT_FILE = "screen_recording.mp4"
RECORD_SECONDS = 10  # Duration of the recording
FPS = 30  # Targeted Frames Per Second

print(f"Recording starting in 2 seconds... Will record for {RECORD_SECONDS}s.")
time.sleep(2)

with mss.mss() as sct:
    # Get primary monitor metrics
    monitor = sct.monitors[1]

    # Grab a sample frame to detect actual pixel width/height (handles Retina scaling)
    sample_img = sct.grab(monitor)
    frame_width = sample_img.width
    frame_height = sample_img.height

    # Define the video codec and create VideoWriter object
    # 'mp4v' works natively across macOS, Windows, and Linux
    fourcc = cv2.VideoWriter_fourcc(*"mp4v")
    video_writer = cv2.VideoWriter(
        OUTPUT_FILE, fourcc, FPS, (frame_width, frame_height)
    )

    start_time = time.time()
    time_per_frame = 1.0 / FPS
    frames_recorded = 0

    print("🔴 RECORDING STARTED...")

    try:
        while (time.time() - start_time) < RECORD_SECONDS:
            frame_start = time.time()

            # 1. Capture the screen frame
            scr_img = sct.grab(monitor)

            # 2. Convert raw bytes to a NumPy array
            frame = np.array(scr_img)

            # 3. MSS captures in BGRA; OpenCV video encoding requires standard BGR
            frame = cv2.cvtColor(frame, cv2.COLOR_BGRA2BGR)

            # 4. Write the frame to the video file
            video_writer.write(frame)
            frames_recorded += 1

            # 5. Dynamic sleep to maintain target frame rate precisely
            elapsed = time.time() - frame_start
            sleep_time = time_per_frame - elapsed
            if sleep_time > 0:
                time.sleep(sleep_time)

    except KeyboardInterrupt:
        print("\nRecording stopped early by user.")

    # Clean up and release the file lock
    video_writer.release()
    cv2.destroyAllWindows()

    actual_duration = time.time() - start_time
    print("🏁 RECORDING FINISHED")
    print(f"Saved to: {OUTPUT_FILE}")
    print(f"Recorded {frames_recorded} frames in {actual_duration:.2f} seconds.")

