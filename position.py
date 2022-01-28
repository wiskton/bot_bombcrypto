import time
import pyautogui

while True:
    x, y = pyautogui.position()
    print("x={},Y={}".format(x,y))
    time.sleep(1)
