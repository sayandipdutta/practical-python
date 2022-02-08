# mortgage.py
#
# Exercise 1.7
principal = 500000.0
rate = 0.05
payment = 2684.11
extra_payment_start, extra_payment_end = 61, 108

def duration(principal,
             rate,
             payment,
             *,
             extra_payment=0,
             correct_overpaymnet=False):
    months_paid = 0
    total_paid = 0.00
    while principal > 0:
        if extra_payment_start <= months_paid <= extra_payment_end:
            monthly_payment = payment + extra_payment
        else:
            monthly_payment = payment
        principal = principal * (1 + rate / 12)
        if correct_overpaymnet and (principal - monthly_payment < 0):
            monthly_payment = principal
        principal -= monthly_payment
        total_paid += monthly_payment
        months_paid += 1
        print(months_paid, total_paid, principal)
    return months_paid, total_paid


months_paid, total_paid = duration(principal, rate, payment)
print(f"Without extra payments: {months_paid=}, {total_paid=}")

months_paid, total_paid = duration(principal,
                                   rate,
                                   payment,
                                   extra_payment=1000.00)
print(f"With extra payments: {months_paid=}, {total_paid=}")

months_paid, total_paid = duration(principal,
                                   rate,
                                   payment,
                                   correct_overpaymnet=True)
print(f"Without extra payments, and correction: {months_paid=}, {total_paid=}")

months_paid, total_paid = duration(principal,
                                   rate,
                                   payment,
                                   extra_payment=1000.00,
                                   correct_overpaymnet=True)
print(f"With extra payments, and correction: {months_paid=}, {total_paid=}")
