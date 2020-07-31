import requests
from pynput import keyboard

shiftPressed = False


def send(url):
    try:
        x = requests.post(url)
        print('Server: ' + x.text)
    except requests.exceptions.RequestException as e:
        print('connection failed')


def on_press(key):
    try:
        print('alphanumeric key {0} pressed'.format(
            key.char))

        char = key.char
        url = 'http://192.168.0.90:3000/send/' + str(ord(char))
        print('trying to send to ' + url)
        send(url)

    except AttributeError:
        print('special key {0} pressed'.format(
            key))

        url = ''

        if str(key) == 'Key.space':
            url = 'http://192.168.0.90:3000/send/32'
        elif str(key) == 'Key.backspace':
            url = 'http://192.168.0.90:3000/send/8'
        elif str(key) == 'Key.shift' or str(key) == 'Key.shift_r':
            url = 'http://192.168.0.90:3000/send/1'

        print('trying to send to ' + url)
        send(url)



def on_release(key):
    print('{0} released'.format(
        key))
    if key == keyboard.Key.esc:
        # Stop listener
        return False


# Collect events until released
with keyboard.Listener(
        on_press=on_press,
        on_release=on_release) as listener:
    listener.join()
