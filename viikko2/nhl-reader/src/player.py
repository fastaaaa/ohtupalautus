import requests

class Player:
    def __init__(self, dict):
        self.name = dict['name']
        self.team = dict['team']
        self.goals = dict['goals']
        self.assists = dict['assists']
        self.nationality = dict['nationality']
        self.points = self.goals + self.assists

    def get_points(self):
        return self.points

    def __str__(self):
        return f"{self.name:20} {self.team} {self.goals} + {self.assists} = {self.points}"

class PlayerReader:
    def __init__(self, url):
        self.url = url

    def get_players(self):
        response = requests.get(self.url).json()
        players = []

        for player_dict in response:
            player = Player(player_dict)
            players.append(player)
        
        return players
    
class PlayerStats:
    def __init__(self, reader):
        self.reader = reader
        self.players = reader.get_players()

    def top_scorers_by_nationality(self, nationality):

        players_nationality = []
        for player in self.players:
            if player.nationality == nationality:
                players_nationality.append(player)
        players_points = sorted(players_nationality, key=lambda x: x.get_points(), reverse=True)

        print(f"Players from {nationality}:\n")
        return players_points