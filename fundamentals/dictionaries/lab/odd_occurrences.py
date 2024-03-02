words = input().split()
words_dict = {}

for word in words:
    word = word.lower()
    if word not in words_dict.keys():
        words_dict[word] = 0
    words_dict[word] += 1

for key, value in words_dict.items():
    if value % 2 != 0:
        print(key, end=" ")
