def display_players(players):
    sorted_players = sorted(players.items(), key=lambda x: (-sum(x[1].values()), x[0]))
    for player, positions in sorted_players:
        print(f"{player}: {sum(positions.values())} skill")
        sorted_positions = sorted(positions.items(), key=lambda x: (-x[1], x[0]))
        for position, skill in sorted_positions:
            print(f"- {position} <::> {skill}")


def process_duel(players_pool, first_user, second_user):
    common_position = [pos for pos in players_pool[first_user] if pos in players_pool[second_user]]
    if common_position:
        first_user_total_skill = sum(players_pool[first_user].values())
        second_user_total_skill = sum(players_pool[second_user].values())

        if first_user_total_skill > second_user_total_skill:
            del players_pool[second_user]
        elif first_user_total_skill < second_user_total_skill:
            del players_pool[first_user]


def add_player(players_pool, user, pos, skill_points):
    players_pool.setdefault(user, {})
    if pos not in players_pool[user]:
        players_pool[user][pos] = skill_points
    else:
        players_pool[user][pos] = max(players_pool[user][pos], skill_points)
    return players_pool


def main():
    players = {}

    while True:
        command = input().split(" -> ")

        if "Season end" in command:
            break

        elif len(command) == 3:
            player, position, skill = command
            skill = int(skill)
            players = add_player(players, player, position, skill)

        else:
            first_player, second_player = "".join(command).split(" vs ")
            if first_player in players and second_player in players:
                process_duel(players, first_player, second_player)

    display_players(players)


if __name__ == '__main__':
    main()
