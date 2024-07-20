class dictionary_iter:

    def __init__(self, dictionary: dict):
        self.dict_items = list(dictionary.items())
        self.idx = -1

    def __iter__(self):
        return self

    def __next__(self):
        self.idx += 1
        if self.idx < len(self.dict_items):
            return self.dict_items[self.idx]
        raise StopIteration


result = dictionary_iter({1: "1", 2: "2"})
for x in result:
    print(x)
