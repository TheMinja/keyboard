import sys
from pynput.keyboard import Key, Controller

keyboard = Controller()

# char = sys.argv[1]
char = 97
convertedChar = chr(int(char))

keyboard.press(convertedChar)
keyboard.release(convertedChar)
