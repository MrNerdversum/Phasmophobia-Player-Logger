


file = open(r"C:\Users\Username\AppData\LocalLow\Kinetic Games\Phasmophobia\Player.log",encoding="mbcs")

#file1 = open('myfile.txt', 'r')
string = " Player Connected"
count = 0
# Strips the newline character
for line in file:
    if string in "Line{}: {}".format(count, line.strip()):
            print("Line{}: {}".format(count, line.strip()))
