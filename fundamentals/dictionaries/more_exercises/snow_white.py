def display_dwarves(dwarves):
    flat_list = [(name, color, physics, index) for color in dwarves for name, (physics, index) in
                 dwarves[color].items()]

    def sort_key(x):
        physics = -x[2]
        color_count = -sum(1 for _, color, _, _ in flat_list if x[1] == color)
        index = x[3]
        return (physics, color_count, index)

    sorted_dwarves = sorted(flat_list, key=sort_key)

    for name, color, physics, _ in sorted_dwarves:
        print(f"({color}) {name} <-> {physics}")


def add_info(dwarves, name, color, physics, index):
    if color not in dwarves:
        dwarves[color] = {}
    if name not in dwarves[color] or dwarves[color][name][0] < physics:
        dwarves[color][name] = (physics, index)

    return dwarves


dwarves_dict = {}
index = 0

while True:
    command = input().split(" <:> ")
    if "Once upon a time" in command:
        break
    dwarf_name, hat_color, dwarf_physics = command
    dwarf_physics = int(dwarf_physics)

    dwarves_dict = add_info(dwarves_dict, dwarf_name, hat_color, dwarf_physics, index)
    index += 1

display_dwarves(dwarves_dict)
