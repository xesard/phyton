import time
import pyautogui

start_time = time.time()

while time.time() - start_time < 27 * 60:
    pyautogui.moveTo(pyautogui.position()[0] + 1, pyautogui.position()[1] + 1, duration=0.001)
    if pyautogui.keyDown("x"):
        break
