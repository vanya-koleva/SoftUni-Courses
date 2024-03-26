import re

text = input()
mirror_words = []
pattern = r"([@#])([A-Za-z]{3,})\1\1([A-Za-z]{3,})\1"
matches = re.findall(pattern, text)

if matches:
    print(f"{len(matches)} word pairs found!")
    for match in matches:
        if match[1] == match[2][::-1]:
            mirror_words.append(match)
else:
    print("No word pairs found!")

if mirror_words:
    print("The mirror words are:")
    for i in range(len(mirror_words)):
        word = mirror_words[i]
        if i < len(mirror_words) - 1:    #if it is not the last iteration
            print(f"{word[1]} <=> {word[2]}, ", end="")
        else:
            print(f"{word[1]} <=> {word[2]}")
else:
    print("No mirror words!")
