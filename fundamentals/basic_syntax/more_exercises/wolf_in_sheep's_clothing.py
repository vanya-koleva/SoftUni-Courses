animals = input()
animals = animals.split(", ")
wolf = animals.index("wolf")

if wolf == len(animals) - 1:
    print("Please go away and stop eating my sheep")
else:
    animals = animals[::-1]
    for i in range(len(animals)):
        if animals[i] != "sheep":
            print(f"Oi! Sheep number {i}! You are about to be eaten by a wolf!")

'''
animals = input()
animals = animals.split(", ")
animals.reverse()

for index, animal in enumerate(animals):
    if animal == 'wolf' and index == 0:
        print('Please go away and stop eating my sheep')
    elif animal == 'wolf':
        print(f'Oi! Sheep number {index}! You are about to be eaten by a wolf!')
'''
