def count_characters(text: list):
    chars_dict = {}

    for word in text:
        for char in word:
            if char not in chars_dict.keys():
                chars_dict[char] = 0
            chars_dict[char] += 1

    return chars_dict


some_string = input().split()
characters_dictionary = count_characters(some_string)

for key, value in characters_dictionary.items():
    print(f"{key} -> {value}")
