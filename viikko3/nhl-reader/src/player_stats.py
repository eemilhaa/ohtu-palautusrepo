class PlayerStats:
    def __init__(self, reader):
        self.players = reader.get_players()

    def top_scorers_by_nationality(self, nationality):
        filtered_players = self.filter_by_nationality(nationality)
        return sorted(
            filtered_players,
            key=lambda player: player.points,
            reverse=True
        )

    def filter_by_nationality(self, nationality):
        return filter(
            lambda player: player.nationality == nationality,
            self.players,
        )
