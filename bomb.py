import time
import mouse
from pyautogui import press

# tempo trabalhando em segundos
time_work = 3600

def click_browser():
    mouse.move(150, 150, absolute=True, duration=0.1)
    mouse.click('left')
    time.sleep(5)

def click_connect_wallet():
    print('conectando sua carteira')
    connect_button_x = '950'
    connect_button_y = '650'

    mouse.move(connect_button_x, connect_button_y, absolute=True, duration=0.1)
    mouse.click('left')

    time.sleep(10)

def click_metamask():
    print('solicitação de assinatura do bombcrypto')
    metamask_subcribe_x = 1800
    metamask_subcribe_y = 550

    mouse.move(metamask_subcribe_x, metamask_subcribe_y, absolute=True, duration=0.1)
    mouse.click('left')

    # waiting load game
    time.sleep(15)

def click_heroes():
    print('entrando na listagem de bombers')
    heroes_x = 1370
    heroes_y = 690

    mouse.move(heroes_x, heroes_y, absolute=True, duration=0.1)
    mouse.click('left')

    time.sleep(5)

def click_work_all():
    print('colocando todos os bombers para trabalhar')
    work_all_x = 880
    work_all_y = 330

    mouse.move(work_all_x, work_all_y, absolute=True, duration=0.1)
    mouse.click('left')

    time.sleep(5)

def click_home():
    print('voltando para home')
    work_back_x = 1015
    work_back_y = 283

    mouse.move(work_back_x, work_back_y, absolute=True, duration=0.1)
    mouse.click('left')

    time.sleep(5)

def click_mining():
    miner_x = 1015
    miner_y = 383

    mouse.move(miner_x, miner_y, absolute=True, duration=0.1)
    mouse.click('left')
    print('iniciando a mineração')

def rotine():    
    click_connect_wallet()

    click_metamask()

    click_heroes()

    click_work_all()

    click_home()

    click_mining()

while True:
    print('deixe o navegador aberto no site do bombcrypto')
    time.sleep(5)
    click_browser()

    press('f5')
    print('aguardando 15 segundos para começar')
    time.sleep(15)
    
    print('iniciando...')
    rotine()
    time.sleep(time_work)
