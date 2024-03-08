strings = input().split()
repeated_string = [word * len(word) for word in strings]
print("".join(repeated_string))
