import requests
from player import Player


class PlayerReader:
    def __init__(self, url):
        self.url = url

    def get_players(self):
        response_json = self._get_response_json()
        return self._make_player_list(response_json)

    def _get_response_json(self):
        return requests.get(self.url).json()

    def _make_player_list(self, response_json):
        player_list = []
        for player_info_dict in response_json:
            player_list.append(
                self._make_player(player_info_dict)
            )
        return player_list

    def _make_player(self, player_info_dict):
        return Player(
            player_info_dict["name"],
            player_info_dict["nationality"],
            player_info_dict["assists"],
            player_info_dict["goals"],
            player_info_dict["penalties"],
            player_info_dict["team"],
            player_info_dict["games"],
        )
