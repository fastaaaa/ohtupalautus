import requests
from player import Player

def main():
    url = "https://studies.cs.helsinki.fi/nhlstats/2023-24/players"
    response = requests.get(url).json()

    players = []

    for player_dict in response:
        if player_dict.get("nationality") == "FIN":
            player = Player(player_dict)
            players.append(player)

    players2 = sorted(players, key=lambda x: x.get_points(), reverse=True)

    print("Players from FIN:\n")

    for player in players2:
        print(player)

if __name__ == "__main__":
    main()
