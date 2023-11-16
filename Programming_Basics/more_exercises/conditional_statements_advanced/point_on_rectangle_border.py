x1 = float(input())
y1 = float(input())
x2 = float(input())
y2 = float(input())
x = float(input())
y = float(input())
border = False

if (x == x1 or x == x2) and y1 <= y <=y2:
    border = True
elif (y == y1 or y == y2) and x1 <= x <= x2:
    border = True
if border == True:
    print('Border')
else:
    print('Inside / Outside')