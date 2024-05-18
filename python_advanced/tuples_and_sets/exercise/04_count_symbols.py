text = input()
occ = {}

for ch in text:
    occ[ch] = occ.get(ch, 0) + 1

for ch, count in sorted(occ.items()):
    print(f"{ch}: {count} time/s")
