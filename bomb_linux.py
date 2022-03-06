import time
import pyautogui

# tempo trabalhando em segundos
time_work = 3200

def click_connect():
    pyautogui.click(x=150, y=150)
    time.sleep(5)

def click_connect_metamask():
    print('conectando sua carteira')
    pyautogui.click(x=950, y=650)
    time.sleep(20)

def click_sign_metamask():
    print('conectando sua carteira - metamask')
    pyautogui.click(x=950, y=595)
    time.sleep(20)

def click_metamask():
    print('solicitação de assinatura do bombcrypto')
    pyautogui.click(x=1800, y=550)
    time.sleep(20)

def click_heroes():
    print('entrando na listagem de bombers')
    pyautogui.click(x=1370, y=690)
    time.sleep(5)

def click_work_all():
    print('colocando todos os bombers para trabalhar')
    pyautogui.click(x=870, y=330)
    time.sleep(5)

def click_close():
    print('voltando para home')
    pyautogui.click(x=1000, y=271)
    time.sleep(5)

def click_hunt():
    print('iniciando a mineração')
    pyautogui.click(x=962, y=450)

def rotine():    
    click_connect_metamask()
    
    click_sign_metamask()

    click_metamask()

    click_heroes()

    click_work_all()

    click_close()

    click_hunt()

while True:
    print('deixe o navegador aberto no site do bombcrypto')
    time.sleep(5)
    click_connect()

    pyautogui.hotkey('ctrl', 'r')
    print('aguardando 15 segundos para começar')
    time.sleep(15)
    
    print('iniciando...')
    rotine()
    time.sleep(time_work)
