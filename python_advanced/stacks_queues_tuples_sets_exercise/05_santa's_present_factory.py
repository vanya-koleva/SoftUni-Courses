from collections import deque

materials = [int(x) for x in input().split()]
magic = deque(int(x) for x in input().split())

crafted = []
presents = {
    150: "Doll",
    250: "Wooden train",
    300: "Teddy bear",
    400: "Bicycle",
}

while magic and materials:
    curr_material = materials.pop() if magic[0] or not materials[-1] else 0
    curr_magic = magic.popleft() if curr_material or not magic[0] else 0

    if not curr_magic:
        continue

    total_magic_level = curr_magic * curr_material

    if presents.get(total_magic_level):
        crafted.append(presents[total_magic_level])
    else:
        if total_magic_level < 0:
            materials.append(curr_material + curr_magic)
        if total_magic_level > 0:
            materials.append(curr_material + 15)

if {"Doll", "Wooden train"}.issubset(crafted) or {"Teddy bear", "Bicycle"}.issubset(crafted):
    print("The presents are crafted! Merry Christmas!")
else:
    print("No presents this Christmas!")

if materials:
    print(f"Materials left: {', '.join(str(x) for x in materials[::-1])}")

if magic:
    print(f"Magic left: {', '.join(str(x) for x in magic)}")

[print(f"{toy}: {crafted.count(toy)}") for toy in sorted(set(crafted))]
