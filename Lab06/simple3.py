def player(beans):
    if beans==16:
        return 3
    if beans==15:
        return 2
    if beans==14:
        return 1
    if beans==13:
        return 1

    if beans <=12 and beans >=10:
        return beans-9
    if beans==9:
        return 1

    if beans >=6 and beans<9:
        return beans -5
    if beans ==5:
        return 1

    else:
        if beans ==4:
            return 3
        elif beans ==3:
            return 2
        elif beans==2:
            return 1
        elif beans ==1:
            return 1