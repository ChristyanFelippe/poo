from icecream import ic

def xpto():
    ic()
    x = 1
    if True:
        ic()
        x = 2
    else:
        ic()
        x = 3

xpto()

ic(1)

ic.disable()

ic(2)

ic.enable()

ic(3)
        