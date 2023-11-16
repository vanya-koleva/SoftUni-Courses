inherited_money = float(input())
year_of_life = int(input())
money_spent = 0
age = 17

for year in range(1800, year_of_life + 1):
    age += 1
    if year % 2 == 0:
        money_spent += 12000
    else:
        money_spent += 12000 + 50 * age

difference = abs(money_spent - inherited_money)
if money_spent <= inherited_money:
    print(f'Yes! He will live a carefree life and will have {difference:.02f} dollars left.')
else:
    print(f'He will need {difference:.02f} dollars to survive.')