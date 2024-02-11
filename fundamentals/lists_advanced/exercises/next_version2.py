version = input()
version = int(version.replace(".", ""))
version += 1
print(".".join(ch for ch in str(version)))
