def howManyMonths(start, rate, spending, target):
    months = 0
    next_month_balance = start

    while (next_month_balance >= 0 and next_month_balance < target and months < 100):
        next_month_balance = next_month_balance * (1 + rate) - spending
        months += 1
    if next_month_balance >= target:
        return months
    else:
        return -1

print(howManyMonths(1000, 0.05, 0, 2000))
