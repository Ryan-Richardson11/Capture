import os
import pyautogui
import time
import datetime as dt


class ScreenShot:
    def __init__(self):
        self.pictures_folder = os.path.join(
            os.path.expanduser("~"), "Pictures")

    def screen_capture(self):
        time_stamp = dt.datetime.now().strftime("%Y%m%d_%H%M%S")
        time.sleep(1)
        fileName = f"screenshot_{time_stamp}.png"

        filePath = os.path.join(self.pictures_folder, fileName)

        screenshot = pyautogui.screenshot()
        screenshot.save(filePath)
