import re


with open("words.txt") as file:
    words = file.read()

words = words.split()

with open("input.txt") as file:
    text = file.read()

word_count = {}
for word in words:
    pattern = rf"\b{word}\b"
    occ = re.findall(pattern, text, re.IGNORECASE)
    word_count[word] = len(occ)

sorted_result = sorted(word_count.items(), key=lambda x: -x[1])

with open("output.txt", "w") as file:
    for key, value in sorted_result:
        file.write(f"{key} - {value}\n")
