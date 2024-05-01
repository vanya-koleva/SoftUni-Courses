def decode_message(msg: list, code: dict) -> str:
    decoded_message = []

    for word in msg:
        decoded_word = ""
        letters = word.split()

        for letter in letters:
            decoded_word += code[letter]

        decoded_message.append(decoded_word)

    return " ".join(decoded_message)


morse_code = {
    ".-": "A", "-...": "B", "-.-.": "C", "-..": "D", ".": "E", "..-.": "F", "--.": "G", "....": "H",
    "..": "I", ".---": "J", "-.-": "K", ".-..": "L", "--": "M", "-.": "N", "---": "O", ".--.": "P",
    "--.-": "Q", ".-.": "R", "...": "S", "-": "T", "..-": "U", "...-": "V", ".--": "W", "-..-": "X",
    "-.--": "Y", "--..": "Z"
}
message = input().split(' | ')
print(decode_message(message, morse_code))
