total_sum = 0
while True:
    deposit = input()
    if deposit == 'NoMoreMoney':
        break
    deposit = float(deposit)
    if deposit < 0:
        print("Invalid operation!")
        break
    print(f'Increase: {deposit:.2f}')
    total_sum += deposit

print(f'Total: {total_sum:.2f}')