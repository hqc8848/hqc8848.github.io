MIRRORING_DIRECTION = "left"

string = input()
if MIRRORING_DIRECTION == "left":
    print(string + string[::-1][1:])
else:
    print(string[1:][::-1] + string)
