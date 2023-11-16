period = int(input())
capacity = 7
treated_patients = 0
untreated_patients = 0
difference = 0
counter = 0

for i in range(1, period + 1):
    counter += 1
    if counter % 3 == 0:
        if untreated_patients > treated_patients:
            capacity += 1
    number_of_patients = int(input())
    if number_of_patients <= capacity:
        treated_patients += number_of_patients
    else:
        difference = number_of_patients - capacity
        untreated_patients += difference
        treated_patients += capacity

print(f'Treated patients: {treated_patients}.')
print(f'Untreated patients: {untreated_patients}.')