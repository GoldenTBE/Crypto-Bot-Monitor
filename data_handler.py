from get_requests import *


def change_to_price(curr_price,change):
    price = float(curr_price)
    amnt_changed = float(change)
    c_to_p = 0

    if amnt_changed < 0:
        c_to_p = price + abs(amnt_changed)
    else:
        c_to_p = price - amnt_changed

    convert = str(c_to_p)

    return convert



def graphing():
    pass






if __name__ == "__main__":
   pass
