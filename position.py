import time
import pyautogui

while True:
    x, y = pyautogui.position()
    print("{},{}".format(x, y))
    time.sleep(1)
