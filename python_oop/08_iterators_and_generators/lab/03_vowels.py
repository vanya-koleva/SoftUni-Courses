class vowels:
    ALL_VOWELS = ["a", "o", "u", "e", "i", "y"]

    def __init__(self, string):
        self.string = string
        self.vowels = [el for el in self.string if el.lower() in self.ALL_VOWELS]
        self.current = -1

    def __iter__(self):
        return self

    def __next__(self):
        self.current += 1
        if self.current < len(self.vowels):
            return self.vowels[self.current]
        raise StopIteration


my_string = vowels('Abcedifuty0o')
for char in my_string:
    print(char)
