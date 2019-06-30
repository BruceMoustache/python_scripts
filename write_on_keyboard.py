import keyboard


def keyboardText(text):
    return '+'.join(list(text))

text = input('Texto para digitar no teclado: ')
sleepTime = input('Tempo de espera: ')

teclas = keyboardText(text)
keyboard.press_and_release(teclas)

