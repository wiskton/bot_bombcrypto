import time
from pynput.mouse import Controller, Button
from pyautogui import press

# segundos para voltar a trabalhar
time_work = 60

connect_button_x = 950
connect_button_y = 650

metamask_subcribe_x = 1800
metamask_subcribe_y = 600

heroes_x = 1370
heroes_y = 690

work_all_x = 880
work_all_y = 330

work_back_x = 1015
work_back_y = 283

miner_x = 1015
miner_y = 483

mouse = Controller()

def reset_position():
    mouse.move(-10000, -10000)
    time.sleep(0.2)

def join():

    # click connect
    reset_position()
    mouse.move(connect_button_x, connect_button_y)
    time.sleep(0.5)
    mouse.click(Button.left)

    # waiting load metamask
    time.sleep(10)

    # subcribe metamask
    reset_position()
    mouse.move(metamask_subcribe_x, metamask_subcribe_y)
    time.sleep(0.5)
    mouse.click(Button.left)

    # waiting load game
    time.sleep(15)

    # select heroes
    reset_position()
    mouse.move(heroes_x, heroes_y)
    time.sleep(0.5)
    mouse.click(Button.left)

    time.sleep(1)

    # ALL HEROES FOR WORK
    reset_position()
    mouse.move(work_all_x, work_all_y)
    time.sleep(0.5)
    mouse.click(Button.left)

    time.sleep(1)

    # BACK HOME
    reset_position()
    mouse.move(work_back_x, work_back_y)
    time.sleep(0.5)
    mouse.click(Button.left)

    time.sleep(1)

    # INITIAL MINING BOMBERS
    reset_position()
    mouse.move(miner_x, miner_y)
    time.sleep(0.5)
    mouse.click(Button.left)

while True:
    join()
    time.sleep(time_work)
    press('f5')
    time.sleep(10)
