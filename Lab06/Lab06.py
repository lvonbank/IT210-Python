# Levi VonBank

from random import randint

## Play "Heap of Beans". Use the best strategy you can devise to beat an opponent.
# 1, 2, or 3 beans can be removed in a turn, but never more than the number of beans
# currently on the table.
# @param beans – the number of beans currently on the table
# @return – the number of beans to be removed this turn
#
def player(beans):
    if beans == 5: return randint(1,3)
    if beans == 4: return 3
    if beans == 3: return 2
    if beans == 2: return 1
    if beans == 1: return 1
    return player(beans - 4)