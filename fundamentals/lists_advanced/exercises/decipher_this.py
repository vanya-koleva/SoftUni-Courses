message = input().split()
deciphered_message = []

for word in message:
    number = [x for x in word if x.isdigit()]
    number = ''.join(number)
    letter = chr(int(number))
    letters = [x for x in word if x.isalpha()]
    letters[0], letters[-1] = letters[-1], letters[0]
    letters.insert(0, letter)
    final_word = "".join(letters)
    deciphered_message.append(final_word)

print(" ".join(deciphered_message))
