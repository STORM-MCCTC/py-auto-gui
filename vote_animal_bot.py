import pyautogui
import time
loop = True

while loop == True:
    time.sleep(1)
    pyautogui.moveTo(x=351, y=363, duration=0.5)
    pyautogui.click(x=351, y=363)
    pyautogui.write("Donnadio Mark",)
    pyautogui.moveTo(x=349, y=444, duration=0)
    pyautogui.click(x=349, y=444)
    pyautogui.write("donnadio_mark@student.mahoningctc.com",)
    pyautogui.moveTo(x=325, y=518, duration=0)
    pyautogui.click(x=325, y=518)
    pyautogui.moveTo(x=328, y=833, duration=0)
    pyautogui.click(x=328, y=833)
    pyautogui.moveTo(x=356, y=279, duration=1)
    time.sleep(1)
    pyautogui.click(x=356, y=279)

# while True:
#     current_mouse_position = pyautogui.position()
#     time.sleep(0.5)
#     print(current_mouse_position)