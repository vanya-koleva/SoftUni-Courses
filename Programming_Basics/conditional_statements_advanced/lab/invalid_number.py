number = int(input())
valid = True

if 100 <= number <= 200 or number == 0:
    valid = False
if valid != True:
    pass
else:
    print('invalid')