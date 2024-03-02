number_of_words = int(input())
dictionary = {}

for i in range(number_of_words):
    word = input()
    synonym = input()
    if word not in dictionary.keys():
        dictionary[word] = []
    dictionary[word].append(synonym)

for word in dictionary.keys():
    print(f"{word} - {', '.join(dictionary[word])}")
