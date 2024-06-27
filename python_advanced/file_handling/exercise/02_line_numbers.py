import os
from string import punctuation

path = os.path.join("text_files", "01_text.txt")
output_path = os.path.join("text_files", "02_output.txt")

with open(path) as file:
    text = file.readlines()

with open(output_path, "w") as output_file:
    for line in range(len(text)):
        letters, marks = 0, 0

        for symbol in text[line]:
            if symbol.isalpha():
                letters += 1
            elif symbol in punctuation:
                marks += 1

        output_file.write(f"Line {line + 1}: {text[line][:-1]} ({letters})({marks})\n")
