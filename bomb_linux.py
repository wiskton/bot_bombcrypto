import time
import datetime
import pyautogui

# tempo trabalhando em segundos
time_work = 3200

def click_button(x, y, msg, second):
    print(msg)
    pyautogui.click(x=x, y=y)
    time.sleep(second)

def rotine():
    click_button(964, 682, 'connect', 5)
    
    click_button(978, 618, 'connect metamask', 20)

    click_button(1821, 631, 'sign metamask', 20)

    click_button(1363, 759, 'heroes', 5)

    click_button(864, 374, 'work all', 5)

    click_button(1005, 323, 'close', 5)

    click_button(943, 502, 'hunt', 5)

while True:
    print('deixe o navegador aberto no site do bombcrypto')
    time.sleep(2)
    click_button(250, 150, 'selecting windows', 1)

    pyautogui.hotkey('ctrl', 'r')
    print('aguardando 20 segundos para começar')
    time.sleep(20)
    
    print('starting...')
    rotine()
    print(datetime.datetime.today())
    time.sleep(time_work)
