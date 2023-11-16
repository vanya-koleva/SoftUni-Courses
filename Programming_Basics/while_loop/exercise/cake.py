width = int(input())
length = int(input())
available_pieces = width * length
there_are_pieces_left = True

command = input()
while command != 'STOP':
    pieces_taken = int(command)
    available_pieces -= pieces_taken
    if available_pieces <= 0:
        there_are_pieces_left = False
        break
    command = input()

available_pieces = abs(available_pieces)
if there_are_pieces_left:
    print(f"{available_pieces} pieces are left.")
else:
    print(f"No more cake left! You need {available_pieces} pieces more.")