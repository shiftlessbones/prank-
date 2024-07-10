import subprocess
from time import sleep
import threading

# Variable to control the loop
running = True

# Function to stop the loop
def stop_loop():
    global running
    while running:
        user_input = input("Type 's' to stop: ")
        if user_input.lower() == 's':
            running = False

# Start a thread to listen for the stop command
input_thread = threading.Thread(target=stop_loop)
input_thread.start()

# Path to the video file
video_path = r'C:\Users\panta\OneDrive\Desktop\virus'

try:
    while running:
        subprocess.Popen(['vlc', video_path])
        sleep(0.3)
except KeyboardInterrupt:
    print("Process interrupted and stopped.")

# Wait for the input thread to finish
input_thread.join()
print("Loop has been stopped.")
