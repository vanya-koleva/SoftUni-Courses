class Party:
    def __init__(self):
        self.people = []

    def add_person(self, name):
        self.people.append(name)

    def display_party_info(self):
        return f"Going: {', '.join(party.people)}\nTotal: {len(party.people)}"


party = Party()

while True:
    person_name = input()
    if person_name == "End":
        break

    party.add_person(person_name)

print(party.display_party_info())
