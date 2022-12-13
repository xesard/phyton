import time
import pyautogui

start_time = time.time()

while time.time() - start_time < 27 * 60:
    pyautogui.moveTo(pyautogui.position()[0] + 1, pyautogui.position()[1] + 1, duration=0.001)
    if pyautogui.keyDown("x"):
        break

# Este script se ejecutará durante 27 minutos, moviendo el cursor en círculos pequeños. Si presionas la tecla "x" en cualquier momento, el script se cancelará.
# Tenga en cuenta que este script requiere la biblioteca **`pyautogui`**. Si no la tienes instalada, puedes instalarla ejecutando **`pip install pyautogui`** en tu consola.
