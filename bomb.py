import time
import datetime
import mouse
import keyboard

# url do game
# https://app.bombcrypto.io/webgl/

# tempo trabalhando em segundos
time_work = 4500


def click_button(x, y, msg, second):
    print(msg)
    mouse.move(x, y, absolute=True, duration=0.1)
    mouse.click("left")
    time.sleep(second)


def refresh_page():
    print("Clicando CTRL+R - recarregar a página")
    keyboard.press_and_release("ctrl + r")
    print("Aguardando 15 segundos para começar")
    time.sleep(15)


def rotine():
    print("iniciando rotina")

    click_button(950, 750, "abrindo o jogo", 5)

    click_button(950, 655, "conectando a metamask", 20)

    click_button(1800, 570, "solicitação de assinatura do bombcrypto", 20)

    click_button(1370, 800, "entrando na listagem de bombers", 5)

    click_button(880, 410, "colocando todos os bombers para trabalhar", 5)

    click_button(1010, 371, "voltando para home", 5)

    click_button(1015, 523, "iniciando a mineração", 5)


print("Deixe o navegador aberto no site do bombcrypto com a metamask logada")


while True:
    click_button(150, 150, "Selecionando o navegador", 5)
    refresh_page()
    rotine()
    print(datetime.datetime.today())
    time.sleep(time_work)
