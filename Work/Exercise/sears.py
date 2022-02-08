from typing import overload

bill_thickness = 0.11 * 0.001  # Meters (0.11 mm)
sears_height = 442  # Height (meters)
num_bills = 1
day = 1

@overload
def double(value: int) -> int:
    pass

@overload
def double(value: float) -> float:
    pass

def double(value: int | float) -> int | float:
    return value * 2


while num_bills * bill_thickness <= sears_height:
    print(
        f"{day=}",
        f"{num_bills=}",
        f"bill_height={num_bills * bill_thickness}",
        f"{sears_height=}"
    )
    num_bills = double(num_bills)
    day += 1

print(
    f"{day=}",
    f"{num_bills=}",
    f"bill_height={num_bills * bill_thickness}",
    f"{sears_height=}"
)

# Alternate methods
from math import log2

day = 1
num_bills = 1

days = int(log2(sears_height / bill_thickness)) + 1
num_bills <<= days
bill_height = num_bills * bill_thickness


print(
    f"days={days+1}",
    f"{num_bills=}",
    f"{bill_height=}",
    f"{sears_height=}"
)
