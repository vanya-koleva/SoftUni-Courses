hour = int(input())
day = input()

if not day == 'Sunday' and 10 <= hour <= 18:
    print('open')
else:
    print('closed')