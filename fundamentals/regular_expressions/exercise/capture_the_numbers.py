import re

text = input()
while text:
    matches = re.findall(r"\d+", text)
    if matches:
        print(" ".join(matches), end=" ")
    text = input()
