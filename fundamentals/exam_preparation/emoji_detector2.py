import re
from functools import reduce

text = input()
digits = re.findall("\d", text)
cool_threshold = reduce(lambda x, y: x * y, [int(digit) for digit in digits])
pattern = r"((:{2}|\*{2})([A-Z][a-z}]{2,})\2)"
matches = re.findall(pattern, text)

print(f"Cool threshold: {cool_threshold}")
print(f"{len(matches)} emojis found in the text. The cool ones are:")

for match in matches:
    coolness = sum([ord(letter) for letter in match[2]])
    if coolness > cool_threshold:
        print(match[0])
