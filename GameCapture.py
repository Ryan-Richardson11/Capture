import threading
import tkinter as tk
import cv2
import os
import pyautogui
import numpy as np
import datetime as dt


class GameCapture:
    def __init__(self, window):
        self.window = window
        self.window.title("Game Capture")
        self.window.minsize(1000, 500)
        self.recording = False
        self.gameplay = None
        self.frame_rate = 30.0

        # UPDATE Tkinter button Styles *********
        button_font = ("Helvetica", 12, "bold")
        self.record_button = tk.Button(
            text="Record", bg="green", width=10, height=5, font=button_font, command=self.record_gameplay)
        self.record_button.pack(anchor="center", pady=10)

        self.stop_button = tk.Button(
            text="Stop", bg="red", width=10, height=5, font=button_font, command=self.stop_recording)
        self.stop_button.pack(anchor="center", pady=10)

    def record_gameplay(self):
        self.recording = True
        fourcc = cv2.VideoWriter_fourcc(*"mp4v")
        resolution = (1920, 1080)
        time_stamp = dt.datetime.now().strftime("%Y%m%d_%H%M%S")
        self.save_path = os.path.join(os.path.expanduser(
            "~"), "Videos", f"gameplay_{time_stamp}.mp4")

        self.gameplay = cv2.VideoWriter(
            self.save_path, fourcc, self.frame_rate, resolution)

        # Incorrect logic to get correct video framerate when played back

        def capture_loop():
            start_time = dt.datetime.now()
            frame_count = 0
            while self.recording:
                # *** Replace pyautogui with more advanced library ***
                screenshot = pyautogui.screenshot()
                cur_frame = cv2.cvtColor(
                    np.array(screenshot), cv2.COLOR_RGB2BGR)

                if self.gameplay:
                    self.gameplay.write(cur_frame)
                    frame_count += 1

                    # Calculate elapsed time and dynamically adjust frame rate
                    elapsed_time = (dt.datetime.now() -
                                    start_time).total_seconds()
                    if elapsed_time >= 1.0:
                        current_fps = frame_count / elapsed_time
                        print(f"Current FPS: {current_fps}")
                        frame_count = 0
                        start_time = dt.datetime.now()

        threading.Thread(target=capture_loop, daemon=True).start()

    def stop_recording(self):
        self.recording = False
        if self.gameplay:
            self.gameplay.release()

    def identify_game(self):
        pass


if __name__ == "__main__":
    window = tk.Tk()
    run = GameCapture(window)
    window.mainloop()
