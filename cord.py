import pyautogui
import time

while True:
    current_mouse_position = pyautogui.position()
    time.sleep(0.5)
    print(current_mouse_position)