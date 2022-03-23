import time
import datetime
import pyautogui

# tempo trabalhando em segundos
time_work = 4500


def click_button(x, y, msg, second):
    print(msg)
    pyautogui.click(x=x, y=y)
    time.sleep(second)


def rotine():

    click_button(964, 682, "carregando jogo", 5)

    click_button(978, 618, "conectando na metamask", 20)

    click_button(1821, 621, "assinando carteira", 20)

    click_button(1363, 759, "selecionando herois", 5)

    click_button(864, 374, "colocando todos herois para trabalhar", 5)

    click_button(1005, 323, "fechando janela de herois", 5)

    click_button(943, 502, "começando a mineração", 5)


while True:
    print("deixe o navegador aberto no site do bombcrypto")
    time.sleep(2)
    click_button(150, 250, "selecionando o navegador", 1)

    pyautogui.hotkey("ctrl", "r")
    print("aguardando 20 segundos para começar")
    time.sleep(20)

    print("iniciando...")
    rotine()
    print(datetime.datetime.today())
    time.sleep(time_work)
