import time
import mouse
import keyboard


# tempo trabalhando em segundos
time_work = 4000


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

    click_button(950, 650, "conectando jogo", 5)

    click_button(950, 595, "conectando sua carteira - metamask", 20)

    click_button(1800, 550, "solicitação de assinatura do bombcrypto", 20)

    click_button(1370, 690, "entrando na listagem de bombers", 5)

    click_button(880, 330, "colocando todos os bombers para trabalhar", 5)

    click_button(1000, 271, "voltando para home", 5)

    click_button(1015, 383, "iniciando a mineração", 5)


print("Deixe o navegador aberto no site do bombcrypto com a metamask connectada")


while True:
    click_button(150, 150, "clicando x=150 e y=150 para selecionar o navegador", 5)
    refresh_page()
    rotine()
    time.sleep(time_work)
