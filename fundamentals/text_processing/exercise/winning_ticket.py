def check_ticket(ticket: str) -> str:
    if len(ticket) != 20:
        return "invalid ticket"

    left_side = ticket[:10]
    right_side = ticket[10:]
    winning_symbols = ['@', '#', '$','^']
    for match_symbol in winning_symbols:
        for uninterrupted_match_length in range(10, 5, - 1):
            winning_symbol_repetition = match_symbol * uninterrupted_match_length
            if winning_symbol_repetition in left_side and winning_symbol_repetition in right_side:
                if uninterrupted_match_length == 10:
                    return f'ticket "{ticket}" - {uninterrupted_match_length}{match_symbol} Jackpot!'
                return f'ticket "{ticket}" - {uninterrupted_match_length}{match_symbol}'

    return f'ticket "{ticket}" - no match'


tickets = [ticket.strip() for ticket in input().split(", ")]
for ticket_ in tickets:
    print(check_ticket(ticket_))
