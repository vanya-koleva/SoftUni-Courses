def list_roman_emperors(*args, **kwargs):
    successful_emperors = {}
    unsuccessful_emperors = {}

    for emperor, success in args:
        if success:
            successful_emperors[emperor] = kwargs[emperor]
        else:
            unsuccessful_emperors[emperor] = kwargs[emperor]

    sorted_successful_emperors = sorted(
        successful_emperors.items(), key=lambda x: (-x[1], x[0])
    )
    sorted_unsuccessful_emperors = sorted(
        unsuccessful_emperors.items(), key=lambda x: (x[1], x[0])
    )

    result = [f"Total number of emperors: {len(kwargs)}"]

    if successful_emperors:
        result.append(f"Successful emperors:")
        for emperor, years in sorted_successful_emperors:
            result.append(f"****{emperor}: {years}")

    if unsuccessful_emperors:
        result.append(f"Unsuccessful emperors:")
        for emperor, years in sorted_unsuccessful_emperors:
            result.append(f"****{emperor}: {years}")

    return "\n".join(result)


# print(list_roman_emperors(("Augustus", True), ("Nero", False), Augustus=40, Nero=14,))
# print(list_roman_emperors(("Augustus", True), ("Trajan", True), ("Nero", False), ("Caligula", False), ("Pertinax", False), ("Vespasian", True), Augustus=40, Trajan=19, Nero=14, Caligula=4, Pertinax=4, Vespasian=19,))
print(list_roman_emperors(("Augustus", True), ("Trajan", True), ("Claudius", True), Augustus=40, Trajan=19, Claudius=13,))
