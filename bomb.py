import time
import mouse
from pyautogui import press

# segundos para voltar a trabalhar
time_work = 3600

def connect():
    print('connecting')
    connect_button_x = '950'
    connect_button_y = '650'

    mouse.move(connect_button_x, connect_button_y, absolute=True, duration=0.1)
    mouse.click('left')

    time.sleep(8)

def metamask():
    print('metamask')
    metamask_subcribe_x = 1800
    metamask_subcribe_y = 550

    mouse.move(metamask_subcribe_x, metamask_subcribe_y, absolute=True, duration=0.1)
    mouse.click('left')

    # waiting load game
    time.sleep(15)

def heroes():
    print('selecting heroes')
    heroes_x = 1370
    heroes_y = 690

    mouse.move(heroes_x, heroes_y, absolute=True, duration=0.1)
    mouse.click('left')

    time.sleep(1)

def work():
    print('work all')
    work_all_x = 880
    work_all_y = 330

    mouse.move(work_all_x, work_all_y, absolute=True, duration=0.1)
    mouse.click('left')

    time.sleep(1)

def home():
    print('backing home...')
    work_back_x = 1015
    work_back_y = 283

    mouse.move(work_back_x, work_back_y, absolute=True, duration=0.1)
    mouse.click('left')

    time.sleep(1)

def mining():
    miner_x = 1015
    miner_y = 483

    mouse.move(miner_x, miner_y, absolute=True, duration=0.1)
    mouse.click('left')
    print('mining...')

def rotine():
    # CONNECTING GAME
    connect()

    # METAMASK
    metamask()

    # SELECTING HEROES
    heroes()

    # ALL HEROES FOR WORK
    work()

    # HOME
    home()

    # MINING
    mining()

while True:
    time.sleep(5)
    press('f5')
    time.sleep(10)
    print('starting...')
    rotine()
    time.sleep(time_work)
