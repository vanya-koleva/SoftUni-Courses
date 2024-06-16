def accommodate_new_pets(capacity, max_weight, *pets):
    pet_types = {}
    result = ''

    for pet_type, pet_weight in pets:
        if capacity == 0:
            result += "You did not manage to accommodate all pets!\n"
            break
        if pet_weight <= max_weight:
            if pet_type not in pet_types.keys():
                pet_types[pet_type] = 0
            pet_types[pet_type] += 1
            capacity -= 1

    else:
        result += f"All pets are accommodated! Available capacity: {capacity}.\n"

    result += "Accommodated pets:\n"
    for pet_type, number in sorted(pet_types.items()):
        result += f"{pet_type}: {number}\n"

    return result


print(accommodate_new_pets(
    10,
    15.0,
    ("cat", 5.8),
    ("dog", 10.0),
))
print(accommodate_new_pets(
    10,
    10.0,
    ("cat", 5.8),
    ("dog", 10.5),
    ("parrot", 0.8),
    ("cat", 3.1),
))
print(accommodate_new_pets(
    2,
    15.0,
    ("dog", 10.0),
    ("cat", 5.8),
    ("cat", 2.7),
))
