def tribonacci(num):
    if (num < 1):
        return

    trib = ""
    first = 1
    second = 1
    third = 2

    trib += f"{first} "
    if num > 1:
        trib += f"{second} "
    if num > 2:
        trib += f"{third} "
    if num > 3:
        for i in range(3, num):
            current = first + second + third
            first = second
            second = third
            third = current

            trib += f"{current} "

    return trib


number = int(input())
print(tribonacci(number))
