import re


def find_cool_emojis(text):
    cool_threshold = 1
    for char in text:
        if char.isdigit():
            cool_threshold *= int(char)

    pattern = r"(\*\*[A-Z][a-z]{2,}\*\*|::[A-Z][a-z]{2,}::)"
    emojis = re.findall(pattern, text)

    print(f"Cool threshold: {cool_threshold}")
    print(f"{len(emojis)} emojis found in the text. The cool ones are:")

    for emoji in emojis:
        coolness = sum([ord(char) for char in emoji if char.isalpha()])
        if coolness > cool_threshold:
            print(emoji)


some_string = input()
find_cool_emojis(some_string)
