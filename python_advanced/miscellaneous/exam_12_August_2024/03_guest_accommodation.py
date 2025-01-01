def accommodate(*guest_groups, **kwargs):
    accommodations = {}
    failed_acc = 0
    rooms = sorted(kwargs.items(), key=lambda x: (x[1], x[0]))

    for guests in guest_groups:
        is_accommodated = False

        for room, capacity in rooms:
            if capacity >= guests:
                room_number = room[5:]
                accommodations[room_number] =guests
                rooms.remove((room, capacity))
                is_accommodated = True
                break

        if not is_accommodated:
            failed_acc += guests

    if accommodations:
        result = [f"A total of {len(accommodations)} accommodations were completed!"]
        for room_number in sorted(accommodations.keys()):
            result.append(f"<Room {room_number} accommodates {accommodations[room_number]} guests>")
    else:
        result = ["No accommodations were completed!"]

    if failed_acc:
        result.append(f"Guests with no accommodation: {failed_acc}")

    if rooms:
        result.append(f"Empty rooms: {len(rooms)}")

    return "\n".join(result)

# print(accommodate(5, 4, 2, room_305=6, room_410=5, room_204=2))
# print(accommodate(10, 9, 8, room_307=6, room_802=5))
print(accommodate(1, 2, 4, 8, room_102=3, room_101=1, room_103=2))
