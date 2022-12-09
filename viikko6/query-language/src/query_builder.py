from matchers import And, All, PlaysIn, HasAtLeast, HasFewerThan


class QueryBuilder:
    def __init__(self, matcher=All()):
        self.matcher = matcher

    def playsIn(self, team):
        return QueryBuilder(PlaysIn(team, self.matcher))

    def hasAtLeast(self, value, attr):
        return QueryBuilder(HasAtLeast(value, attr, self.matcher))

    def hasFewerThan(self, value, attr):
        return QueryBuilder(HasFewerThan(value, attr, self.matcher))

    def build(self):
        return self.matcher
