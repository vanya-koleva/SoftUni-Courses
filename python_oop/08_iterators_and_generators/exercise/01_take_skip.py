class take_skip:

    def __init__(self, step: int, count: int):
        self.step = step
        self.count = count
        self.current = -step

    def __iter__(self):
        return self

    def __next__(self):
        if self.count > 0:
            self.count -= 1
            self.current += self.step
            return self.current
        raise StopIteration


numbers = take_skip(2, 6)
for number in numbers:
    print(number)
