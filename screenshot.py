import os
import pyautogui
import time


class ScreenShot:
    def __init__(self):
        self.pictures_folder = pictures_folder = os.path.join(
            os.path.expanduser("~"), "Pictures")

    def screen_capture(self, fileName):
        time.sleep(1)

        filePath = os.path.join(self.pictures_folder, fileName)

        screenshot = pyautogui.screenshot()
        screenshot.save(filePath)
