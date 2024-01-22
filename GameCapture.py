import tkinter as tk
import cv2
import os
import pyautogui
import numpy as np


class GameCapture:
    def __init__(self, window):
        self.window = window
        self.window.title("Game Capture")
        self.window.minsize(1000, 500)
        self.save_path = os.path.join(
            os.path.expanduser("~"), "Videos", "gameplay.mp4")
        self.recording = False
        button_font = ("Helvetica", 12, "bold")

        self.record_button = tk.Button(
            text="Record", bg="green", width=10, height=5, font=button_font, command=self.record_gameplay)
        self.record_button.pack(anchor="center", pady=10)

        self.stop_button = tk.Button(
            text="Stop", bg="red", width=10, height=5, font=button_font, command=self.stop_recording)
        self.stop_button.pack(anchor="center", pady=10)

    def record_gameplay(self):
        recording = True
        fourcc = cv2.VideoWriter_fourcc(*"XVID")
        fps = 30.0
        resolution = (1920, 1080)

        gameplay = cv2.VideoWriter(self.save_path, fourcc, fps, resolution)

        while recording:
            screenshot = pyautogui.screenshot()
            cur_frame = cv2.cvtColor(np.array(screenshot), cv2.COLOR_RGB2BGR)
            gameplay.write(cur_frame)

        gameplay.release()

    def stop_recording(self):
        self.recording = False

    def identify_game(self):
        pass


if __name__ == "__main__":
    window = tk.Tk()
    run = GameCapture(window)
    window.mainloop()
