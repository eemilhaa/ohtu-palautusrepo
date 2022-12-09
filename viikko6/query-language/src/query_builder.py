from matchers import All, PlaysIn


class QueryBuilder:
    def __init__(self, query=All()):
        self.query = query

    def playsIn(self, team):
        return QueryBuilder(PlaysIn(team))

    def build(self):
        return self.query
