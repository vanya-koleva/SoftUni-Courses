weather = float(input())
if 5 <= weather < 12:
    print("Cold")
elif 12 <= weather < 15:
    print("Cool")
elif 15<= weather <= 20:
    print("Mild")
elif 20.1 <= weather < 26:
    print("Warm")
elif 26 <= weather <35:
    print("Hot")
else:
    print("unknown")