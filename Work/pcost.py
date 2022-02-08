# pcost.py
#
# Exercise 1.27
from os import PathLike
from pathlib import Path
from typing import Iterator

def iterate_lines(file_it: Iterator):
    for line in file_it:
        if line := line.strip():
            yield line


def calculate_tot_value(datafile: PathLike[str]):
    total_price = 0.00
    with open(datafile, "rt") as f:
        headers = next(f)
        print(*headers.split(','), sep='\t')
        for line in iterate_lines(f):
            name, shares, price = line.split(",")
            print(name, shares, price, sep='\t')
            shares, price = float(shares), float(price)
            stock_value = shares * price
            total_price += stock_value
    return total_price


if __name__ == "__main__":
    DATAFILE: PathLike[str] = Path("Data/portfolio.csv")
    total_price = calculate_tot_value(DATAFILE)
    print("Total price:", total_price)
