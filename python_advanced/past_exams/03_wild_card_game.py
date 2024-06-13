def draw_cards(*args, **kwargs):
    monster_cards = []
    spell_cards = []
    result = ""

    for card in args:
        if card[1] == "monster":
            monster_cards.append(card[0])
        else:
            spell_cards.append(card[0])

    for name, card_type in kwargs.items():
        if card_type == "monster":
            monster_cards.append(name)
        else:
            spell_cards.append(name)

    if monster_cards:
        result += "Monster cards:\n"
        for card in sorted(monster_cards, reverse=True):
            result += f"  ***{card}\n"

    if spell_cards:
        result += "Spell cards:\n"
        for card in sorted(spell_cards):
            result += f"  $$${card}\n"

    return result


print(draw_cards(("brave attack", "spell"), ("freeze", "spell"), lightning_bolt="spell", fireball="spell",))
