def print_results(key_materials, junk, legendary_item):
    print(f"{legendary_item} obtained!")

    for material, quantity in key_materials.items():
        print(f"{material}: {quantity}")

    for material, quantity in junk.items():
        print(f"{material}: {quantity}")


def process_materials(key_materials, junk, farmed_materials):
    for i in range(len(farmed_materials)):

        if i % 2 == 0:
            quantity = int(farmed_materials[i])
            material = farmed_materials[i + 1].lower()

            if material in key_materials.keys():
                key_materials[material] += quantity

                if key_materials[material] >= 250:
                    key_materials[material] -= 250
                    return key_materials, junk, material

            else:
                if material not in junk.keys():
                    junk[material] = 0
                junk[material] += quantity

    material = None
    return key_materials, junk, material


def main():
    key_materials = {"shards": 0, "fragments": 0, "motes": 0}
    junk = {}

    while True:
        farmed_materials = input().split()
        key_materials, junk, material = process_materials(key_materials, junk, farmed_materials)
        if material:
            break

    if material == "shards":
        legendary_item = "Shadowmourne"
    elif material == "fragments":
        legendary_item = "Valanyr"
    else:
        legendary_item = "Dragonwrath"

    print_results(key_materials, junk, legendary_item)


main()
