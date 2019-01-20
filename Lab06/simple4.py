## Play "Heap of Beans". Use the best strategy you can devise to beat an opponent.
# 1, 2, or 3 beans can be removed in a turn, but never more than the number of beans
# currently on the table.
# @param beans – the number of beans currently on the table
# @return – the number of beans to be removed this turn
#

def player(beans):
    return max(1,(beans-1)%4)