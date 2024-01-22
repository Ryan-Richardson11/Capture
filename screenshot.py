import os
import pyautogui
import time


def screen_capture(fileName):
    time.sleep(1)

    pictures_folder = os.path.join(os.path.expanduser("~"), "Pictures")

    filePath = os.path.join(pictures_folder, fileName)

    screenshot = pyautogui.screenshot()
    screenshot.save(filePath)


screen_capture("screenshot.png")
