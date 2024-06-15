from collections import deque

amounts_of_fuels = [int(x) for x in input().split()]
consumption_indices = deque(int(x) for x in input().split())
quantities_needed = deque(int(x) for x in input().split())
counter = 0

while quantities_needed:
    fuel = amounts_of_fuels.pop()
    additional_consumption = consumption_indices.popleft()
    altitude = quantities_needed.popleft()

    total_fuel = fuel - additional_consumption
    counter += 1

    if total_fuel >= altitude:
        print(f"John has reached: Altitude {counter}")
    else:
        print(f"John did not reach: Altitude {counter}")
        counter -= 1

        if counter > 0:
            print("John failed to reach the top.")
            result = []
            for a in range(counter):
                result.append(f"Altitude {a + 1}")
            print(f"Reached altitudes: {', '.join(result)}")

        else:
            print("John failed to reach the top.")
            print("John didn't reach any altitude.")
        break

else:
    print("John has reached all the altitudes and managed to reach the top!")
