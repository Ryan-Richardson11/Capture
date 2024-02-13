import threading
import tkinter as tk
import cv2
import os
import pyautogui
import numpy as np
import datetime as dt
from screenshot import ScreenShot


class GameCapture:
    def __init__(self, window):
        self.window = window
        self.window.title("Game Capture")
        self.window.minsize(1000, 500)
        self.recording = False
        self.gameplay = None
        self.frame_rate = 24.0
        # Instance of ScreenShot class created
        self.screenshot = ScreenShot()

        # UPDATE Tkinter button Styles *********
        button_font = ("Helvetica", 12, "bold")
        self.record_button = tk.Button(
            text="Record", bg="green", width=10, height=5, font=button_font, command=self.record_gameplay)
        self.record_button.pack(anchor="center", pady=10)

        self.play_button = tk.Button(
            text="Playback", bg="blue", width=10, height=5, font=button_font, command=self.play_gameplay)
        self.play_button.pack(anchor="center", pady=10)

        self.stop_button = tk.Button(
            text="Stop", bg="red", width=10, height=5, font=button_font, command=self.stop_recording)
        self.stop_button.pack(anchor="center", pady=10)

        self.screenshot_button = tk.Button(
            text="Screenshot", bg="gray", width=10, height=5, font=button_font, command=self.screenshot.screen_capture)
        self.screenshot_button.pack(anchor="center", pady=10)

    def record_gameplay(self):
        self.recording = True
        fourcc = cv2.VideoWriter_fourcc(*"mp4v")
        resolution = (1600, 900)
        time_stamp = dt.datetime.now().strftime("%Y%m%d_%H%M%S")
        self.save_path = os.path.join(os.path.expanduser(
            "~"), "Videos", f"gameplay_{time_stamp}.mp4")

        self.gameplay = cv2.VideoWriter(
            self.save_path, fourcc, self.frame_rate, resolution)

        def capture_loop():
            while self.recording:
                screenshot = pyautogui.screenshot()
                cur_frame = cv2.cvtColor(
                    np.array(screenshot), cv2.COLOR_RGB2BGR)

                if self.gameplay:
                    self.gameplay.write(cur_frame)

        threading.Thread(target=capture_loop, daemon=True).start()

    def stop_recording(self):
        self.recording = False
        if self.gameplay:
            self.gameplay.release()

    def play_gameplay(self):
        cap = cv2.VideoCapture(self.save_path)
        if not cap.isOpened():
            print("Error opening video file")
            return

        while True:
            ret, frame = cap.read()
            if not ret:
                break

            cv2.imshow("Gameplay", frame)
            if cv2.waitKey(int(1000 / self.frame_rate)) & 0xFF == ord('q'):
                break

        cap.release()
        cv2.destroyAllWindows()
    # implements identifyWindow class

    def identify_game(self):
        pass


if __name__ == "__main__":
    window = tk.Tk()
    run = GameCapture(window)
    window.mainloop()
