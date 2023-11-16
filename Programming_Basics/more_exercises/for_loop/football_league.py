stadium_capacity = int(input())
total_fans = int(input())
sector_a_fans = 0
sector_b_fans = 0
sector_v_fans = 0
sector_g_fans = 0

for i in range(total_fans):
    sector = input()
    if sector == 'A':
        sector_a_fans += 1
    if sector == 'B':
        sector_b_fans += 1
    if sector == 'V':
        sector_v_fans += 1
    if sector == 'G':
        sector_g_fans += 1

sector_a_percentage = sector_a_fans / total_fans * 100
sector_b_percentage = sector_b_fans / total_fans * 100
sector_v_percentage = sector_v_fans / total_fans * 100
sector_g_percentage = sector_g_fans / total_fans * 100
total_fans_percentage = total_fans / stadium_capacity * 100

print(f'{sector_a_percentage:.2f}%')
print(f'{sector_b_percentage:.2f}%')
print(f'{sector_v_percentage:.2f}%')
print(f'{sector_g_percentage:.2f}%')
print(f'{total_fans_percentage:.2f}%')