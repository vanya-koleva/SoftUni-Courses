phonebook = {}
searched_contacts = 0

while True:
    entry = input().split("-")

    if len(entry) == 1:
        searched_contacts = int("".join(entry))
        break

    name, number = entry

    phonebook[name] = number

for i in range(searched_contacts):
    contact = input()
    if contact in phonebook.keys():
        print(f"{contact} -> {phonebook[contact]}")
    else:
        print(f"Contact {contact} does not exist.")
