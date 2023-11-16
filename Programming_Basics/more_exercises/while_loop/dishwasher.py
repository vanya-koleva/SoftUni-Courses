number_of_bottles = int(input())
total_detergent = number_of_bottles * 750
detergent_is_enough = True
loading_counter = 0
number_of_washed_plates = 0
number_of_washed_pots = 0

command = input()
while command != "End":
    number_of_dishes = int(command)
    loading_counter += 1
    if loading_counter % 3 == 0:
        total_detergent -= number_of_dishes * 15
        number_of_washed_pots += number_of_dishes
    else:
        total_detergent -= number_of_dishes * 5
        number_of_washed_plates += number_of_dishes
    if total_detergent < 0:
        detergent_is_enough = False
        break
    command = input()

total_detergent = abs(total_detergent)
if detergent_is_enough:
    print("Detergent was enough!")
    print(f"{number_of_washed_plates} dishes and {number_of_washed_pots} pots were washed.")
    print(f"Leftover detergent {total_detergent} ml.")
else:
    print(f"Not enough detergent, {total_detergent} ml. more necessary!")
