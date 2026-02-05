string = ['L', "E", "B", "R", "O", "S"]

target_ch = input()

if target_ch in string:
    print(string.index(target_ch))
else:
    print(0)