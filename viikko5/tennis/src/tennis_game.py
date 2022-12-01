POINT_CALLS = {
    0: "Love",
    1: "Fifteen",
    2: "Thirty",
    3: "Forty",
    4: "Game",
}


class TennisGame:
    def __init__(self, player1_name, player2_name):
        self.player1 = player1_name
        self.player2 = player2_name
        self._points = {
            self.player1: 0,
            self.player2: 0,
        }

    def won_point(self, player_name):
        self._points[player_name] += 1

    def get_score(self):
        player1_points = self._get_points(self.player1)
        player2_points = self._get_points(self.player2)

        if player1_points == player2_points:
            output = self._get_even_score(player1_points)

        elif max([player1_points, player2_points]) >= 4:
            output = self._get_score_over_4_points(
                player1_points, player2_points
            )

        else:
            output = ""
            for i in range(1, 3):
                if i == 1:
                    temp_score = player1_points
                else:
                    output = output + "-"
                    temp_score = player2_points

                if temp_score == 0:
                    output = output + "Love"
                elif temp_score == 1:
                    output = output + "Fifteen"
                elif temp_score == 2:
                    output = output + "Thirty"
                elif temp_score == 3:
                    output = output + "Forty"

        return output

    def _get_even_score(self, points):
        if points < 4:
            call = POINT_CALLS[points]
            return f"{call}-All"
        else:
            return "Deuce"

    def _get_score_over_4_points(self, player1_points, player2_points):
        leading_player = self._player_with_most_points()
        point_difference = abs(player1_points - player2_points)

        if point_difference == 1:
            return f"Advantage {leading_player}"
        elif point_difference >= 2:
            return f"Win for {leading_player}"

    def _get_points(self, player):
        return self._points[player]

    def _player_with_most_points(self):
        return max(self._points, key=self._points.get)
