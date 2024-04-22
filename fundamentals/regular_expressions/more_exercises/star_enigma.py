import re


def display_results(attacked: list, destroyed: list):
    print(f"Attacked planets: {len(attacked)}")
    for planet in sorted(attacked):
        print(f"-> {planet}")
    print(f"Destroyed planets: {len(destroyed)}")
    for planet in sorted(destroyed):
        print(f"-> {planet}")


def process_message(msg: str, attacked: list, destroyed: list):
    pattern = r"[^@\-!:>]*@([A-Za-z]+)[^@\-!:>]*:([0-9]+)[^@\-!:>]*!(A|D)![^@\-!:>]*->([0-9]+)"
    matches = re.search(pattern, msg)
    if matches:
        planet = matches.group(1)
        attack_type = matches.group(3)
        if attack_type == "A":
            attacked.append(planet)
        else:
            destroyed.append(planet)
    return attacked, destroyed


def main():
    attacked_planets = []
    destroyed_planets = []
    num = int(input())

    for _ in range(num):
        message = input()
        key = sum(message.lower().count(ch) for ch in "star")
        decrypted_message = "".join([chr(ord(ch) - key) for ch in message])
        attacked_planets, destroyed_planets = process_message(
            decrypted_message, attacked_planets, destroyed_planets
        )
    display_results(attacked_planets, destroyed_planets)


if __name__ == '__main__':
    main()
