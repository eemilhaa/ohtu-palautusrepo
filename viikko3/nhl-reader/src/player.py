class Player:
    def __init__(
        self,
        name,
        nationality,
        assists,
        goals,
        penalties,
        team,
        games,
    ):
        self.name = name
        self.nationality = nationality
        self.assists = assists
        self.goals = goals
        self.penalties = penalties
        self.team = team
        self.games = games
        self.points = self.get_points()

    def get_points(self):
        return self.goals + self.assists

    def __str__(self):
        def format_number(number):
            return str(number).rjust(2)
        return (
            f"{self.name:22} {self.team} "
            f"{format_number(self.goals)} "
            f"+ {format_number(self.assists)} "
            f"= {format_number(self.points)}"
        )
