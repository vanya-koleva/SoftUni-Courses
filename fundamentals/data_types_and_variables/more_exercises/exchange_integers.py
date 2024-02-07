a = int(input())
b = int(input())

print("Before:")
print(f"a = {a}")
print(f"b = {b}")

a, b = b, a

# c = a
# a = b
# b = c

print("After:")
print(f"a = {a}")
print(f"b = {b}")
