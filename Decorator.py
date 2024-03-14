"""
Decorator's Calculator
"""


def area_to_cover(x, y):
    area = x * y
    return area


def paint_req(x, y):
    z = 0
    if x == y:
        z += 1
        return z
    elif int(x / y) < 1:
        z += 1
        return z
    else:
        return int(x / y)


def cost(x, y):
    z = float(x * y)
    return z


def dec_calc():
    length = int(input("Give the length in metres: "))
    width = int(input("Give the width in metres: "))
    coverage = area_to_cover(length, width)
    paint_pots_available = int(input("How many paint pots do you have?: "))
    paint_pots_required = paint_req(coverage, paint_pots_available)
    if paint_pots_required <= paint_pots_available:
        paint_pots_required = 0
    cost_per_tin = float(input("How much is a tin of paint?: £"))
    final_cost = round(cost(cost_per_tin, paint_pots_required), 2)
    print(f"\nYou will need to purchase {paint_pots_required} paint pots at a total cost of £{final_cost} "
          f"for your project covering {coverage}m^2")


if __name__ == "__main__":
    dec_calc()
