deposit = float(input())
months = int(input())
annual_interest_percentage = float(input())

#сума = депозирана сума + срок на депозита * ((депозирана сума * годишен лихвен процент ) / 12)
annual_interest = deposit * annual_interest_percentage / 100
monthly_interest = annual_interest / 12
total_sum = deposit + (months * monthly_interest)
print(total_sum)