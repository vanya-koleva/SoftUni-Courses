import re

pattern = r"(w{3}\.[A-Za-z0-9\-]+(\.[a-z]+)+)"
while True:
    sentence = input()
    if not sentence:
        break

    matches = re.search(pattern, sentence)
    if matches:
        print(matches.group(1))
