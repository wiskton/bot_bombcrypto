import time
import pyautogui

# tempo trabalhando em segundos
time_work = 3200

def click_button(x, y, msg, second):
    print(msg)
    pyautogui.click(x=x, y=y)
    time.sleep(second)

def rotine():
    click_button(705, 626, 'connect', 5)
    
    click_button(691, 560, 'connect metamask', 30)

    click_button(1269, 593, 'sign metamask', 30)

    click_button(1094, 697, 'heroes', 5)

    click_button(599, 315, 'work all', 5)

    click_button(735, 265, 'close', 5)

    click_button(696, 442, 'hunt', 5)

while True:
    print('deixe o navegador aberto no site do bombcrypto')
    time.sleep(2)
    click_button(150, 150, 'selecting windows', 1)

    pyautogui.hotkey('ctrl', 'r')
    print('aguardando 20 segundos para começar')
    time.sleep(20)
    
    print('starting...')
    rotine()
    time.sleep(time_work)
