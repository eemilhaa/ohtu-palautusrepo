class And:
    def __init__(self, *matchers):
        self._matchers = matchers

    def test(self, player):
        if not _check_matchers(player, self._matchers):
            return False
        return True


class Or:
    def __init__(self, *matchers):
        self._matchers = matchers

    def test(self, player):
        for matcher in self._matchers:
            if matcher.test(player):
                return True
        return False


class Not:
    def __init__(self, *matchers):
        self._matchers = matchers

    def test(self, player):
        if _check_matchers(player, self._matchers):
            return False
        return True


class PlaysIn:
    def __init__(self, team, *matchers):
        self._team = team
        self._matchers = matchers

    def test(self, player):
        if not _check_matchers(player, self._matchers):
            return False
        return player.team == self._team


class HasAtLeast:
    def __init__(self, value, attr, *matchers):
        self._value = value
        self._attr = attr
        self._matchers = matchers

    def test(self, player):
        if not _check_matchers(player, self._matchers):
            return False
        player_value = getattr(player, self._attr)
        return player_value >= self._value


class HasFewerThan:
    def __init__(self, value, attr, *matchers):
        self._value = value
        self._attr = attr
        self._matchers = matchers

    def test(self, player):
        if not _check_matchers(player, self._matchers):
            return False
        player_value = getattr(player, self._attr)
        return player_value < self._value


class All:
    def test(self, player):
        return True


def _check_matchers(player, matchers):
    for matcher in matchers:
        if not matcher.test(player):
            return False
    return True
