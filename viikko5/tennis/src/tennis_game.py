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
        self.score1 = 0
        self.score2 = 0

    def won_point(self, player_name):
        if player_name == "player1":
            self.score1 = self.score1 + 1
        else:
            self.score2 = self.score2 + 1

    def get_score(self):

        if self.score1 == self.score2:
            if self.score1 < 4:
                call = POINT_CALLS[self.score1]
                output = f"{call}-All"
            else:
                output = "Deuce"

        elif self.score1 >= 4 or self.score2 >= 4:
            point_difference = self.score1 - self.score2

            if point_difference == 1:
                output = "Advantage player1"
            elif point_difference == -1:
                output = "Advantage player2"
            elif point_difference >= 2:
                output = "Win for player1"
            else:
                output = "Win for player2"

        else:
            output = ""
            for i in range(1, 3):
                if i == 1:
                    temp_score = self.score1
                else:
                    output = output + "-"
                    temp_score = self.score2

                if temp_score == 0:
                    output = output + "Love"
                elif temp_score == 1:
                    output = output + "Fifteen"
                elif temp_score == 2:
                    output = output + "Thirty"
                elif temp_score == 3:
                    output = output + "Forty"

        return output
