k_first_digit_of_first_number = int(input())
l_second_digit_of_first_number = int(input())
m_first_digit_of_second_number = int(input())
n_second_digit_of_second_number = int(input())
valid_substitutes_counter = 0


for k in range(k_first_digit_of_first_number, 8 + 1):
    if k % 2 != 0:
        continue
    for l in range(9, l_second_digit_of_first_number - 1, - 1):
        if l % 2 == 0:
            continue
        for m in range(m_first_digit_of_second_number, 8 + 1):
            if m % 2 != 0:
                continue
            for n in range(9, n_second_digit_of_second_number -1, - 1):
                if n % 2 == 0:
                    continue
                if k == m and l == n:
                    print("Cannot change the same player.")
                else:
                    valid_substitutes_counter += 1
                    print(f"{k}{l} - {m}{n}")
                if valid_substitutes_counter == 6:
                    exit()