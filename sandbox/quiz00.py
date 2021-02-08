"""Unstoppable Gamestop (stock symbol $GME)."""

gme: float = 30.0
print("01/13: " + str(gme))
fund_short: float = gme
reddit_share: float = gme

gme = gme + 130.0
print("01/26: " + str(gme))
print("fund: " + str(fund_short - gme))
print("reddit: " + str(gme - reddit_share))

gme = 200.0 + gme
print("01/27: " + str(gme))
print("fund: " + str(fund_short - gme))
print("reddit: " + str(gme - reddit_share))


x: int = 92
j: int = 94
round(x*.3 + j*.7)

int(1.0) + 2 / int("2")