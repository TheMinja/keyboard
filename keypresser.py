import sys

char = sys.argv[1]

f = open("tempOutput.txt", "a")
f.write("character is: " + chr(int(char)))
f.close()

