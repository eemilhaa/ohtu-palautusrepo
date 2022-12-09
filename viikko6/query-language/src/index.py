from statistics import Statistics
from player_reader import PlayerReader
# from matchers import And, HasAtLeast, PlaysIn, All, Not, HasFewerThan, Or
from query_builder import QueryBuilder


def main():
    url = "https://studies.cs.helsinki.fi/nhlstats/2021-22/players.txt"
    reader = PlayerReader(url)
    stats = Statistics(reader)

    # matcher = And(
    #     HasAtLeast(5, "goals"),
    #     HasAtLeast(5, "assists"),
    #     PlaysIn("PHI")
    # )

    # matcher_all = And(
    #     All()
    # )

    # matcher_not = And(
    #     Not(HasAtLeast(1, "goals")),
    #     PlaysIn("NYR")
    # )

    # matcher_fewer = And(
    #     HasFewerThan(1, "goals"),
    #     PlaysIn("NYR")
    # )

    # matcher_or = And(
    #     HasAtLeast(70, "points"),
    #     Or(
    #         PlaysIn("NYR"),
    #         PlaysIn("FLA"),
    #         PlaysIn("BOS")
    #     )
    # )

    query = QueryBuilder()
    matcher_builder = query.playsIn("NYR").build()

    for player in stats.matches(matcher_builder):
        print(player)


if __name__ == "__main__":
    main()
