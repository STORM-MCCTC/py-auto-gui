import pyautogui
import time
loop = False
pyautogui.moveTo(348, 1060, 0.1)
pyautogui.click(348, 1060)
pyautogui.moveTo(234, 951, 0.1)
pyautogui.click(234, 951)
pyautogui.moveTo(736, 596, 0.1)
# loop = True
while loop == True:
    pyautogui.click(736, 596)
    pyautogui.write("Donnadio Mark", interval=0.1)
    pyautogui.moveTo(716, 746, 0.1)
    pyautogui.write("donnadio_mark@student.mahoningctc.com", interval=0.1)
    pyautogui.moveTo(675, 911, 0.1)
    pyautogui.click(675, 911)
    pyautogui.scroll(100)
    pyautogui.moveTo(685, 864, 0.1)
    pyautogui.click(685, 864,)
    pyautogui.moveTo(707, 452)
    pyautogui.click(707, 452)

while True:
    current_mouse_position = pyautogui.position()
    time.sleep(1)
    print(current_mouse_position)