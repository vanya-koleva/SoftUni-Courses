starting_index = int(input())
ending_index = int(input())

for index in range(starting_index, ending_index +1):
    symbol = chr(index)
    print(symbol, end=" ")
