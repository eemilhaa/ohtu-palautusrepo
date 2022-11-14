import requests
from player import Player


def main():
    url = "https://studies.cs.helsinki.fi/nhlstats/2021-22/players"
    response = requests.get(url).json()

    print("JSON-muotoinen vastaus:")
    print(response)

    players = []

    for player_dict in response:
        player = Player(
            player_dict["name"],
            player_dict["nationality"],
            player_dict["assists"],
            player_dict["goals"],
            player_dict["penalties"],
            player_dict["team"],
            player_dict["games"],
        )
        if player.nationality == "FIN":
            players.append(player)

    print("Oliot:")
    players_sorted = sorted(
        players,
        key=lambda player: player.points,
        reverse=True
    )
    for player in players_sorted:
        print(player)


if __name__ == "__main__":
    main()
