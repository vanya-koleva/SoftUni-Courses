text = input()
text = [x for x in text if x.lower() not in ['a', 'o', 'u', 'e', 'i']]
print("".join(text))
