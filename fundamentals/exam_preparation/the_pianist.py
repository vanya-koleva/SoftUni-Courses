def change_key(pieces_dict, split_command):
    piece_, new_key = split_command[1], split_command[2]
    if piece_ in pieces_dict.keys():
        pieces_dict[piece_]["key"] = new_key
        print(f"Changed the key of {piece_} to {new_key}!")
    else:
        print(f"Invalid operation! {piece_} does not exist in the collection.")
    return pieces_dict


def remove_piece(pieces_dict, split_command):
    piece_ = split_command[1]
    if piece_ in pieces_dict.keys():
        del pieces_dict[piece_]
        print(f"Successfully removed {piece_}!")
    else:
        print(f"Invalid operation! {piece_} does not exist in the collection.")
    return pieces_dict


def add_piece(pieces_dict, split_command):
    piece_, composer_, key_ = split_command[1], split_command[2], split_command[3]
    if piece_ in pieces_dict.keys():
        print(f"{piece_} is already in the collection!")
    else:
        pieces_dict[piece_] = {"composer": composer_, "key": key_}
        print(f"{piece_} by {composer_} in {key_} added to the collection!")
    return pieces_dict


pieces = {}
number_of_pieces = int(input())

for i in range(number_of_pieces):
    piece, composer, key = input().split("|")
    pieces[piece] = {"composer": composer, "key": key}

while True:
    command = input().split("|")
    if "Stop" in command:
        break

    elif "Add" in command:
        pieces = add_piece(pieces, command)
    elif "Remove" in command:
        pieces = remove_piece(pieces, command)
    else:
        pieces = change_key(pieces, command)

for piece, info in pieces.items():
    print(f"{piece} -> Composer: {info['composer']}, Key: {info['key']}")
