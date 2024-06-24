path = "numbers.txt"
total_sum = 0

try:
    file = open(path, "r")
    lines = file.readlines()
    for line in lines:
        num = int(line[:-1])
        total_sum += num
    print(total_sum)
    file.close()

except FileNotFoundError:
    print("File not found")
