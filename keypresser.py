import sys
from pynput.keyboard import Key, Controller

keyboard = Controller()

data = int(sys.argv[1])

if data == 8:
    keyboard.press(Key.backspace)
    keyboard.release(Key.backspace)
elif data == 32:
    keyboard.press(Key.space)
    keyboard.release(Key.space)
else:
    convertedChar = chr(data)

    keyboard.press(convertedChar)
    keyboard.release(convertedChar)
