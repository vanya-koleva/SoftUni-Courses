def to_do_list():
    all_notes = []
    while True:
        note = input()
        if note == "End":
            break
        all_notes.append(note)

    all_notes = sorted(all_notes, key=lambda x: int(x.split("-")[0]))
    all_notes = [x.split("-")[1] for x in all_notes]
    return all_notes


print(to_do_list())
