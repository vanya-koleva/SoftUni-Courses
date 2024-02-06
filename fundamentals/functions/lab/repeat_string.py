some_string = input()
counter = int(input())

new_string = lambda text, counter: text * counter

print(new_string(some_string, counter))
