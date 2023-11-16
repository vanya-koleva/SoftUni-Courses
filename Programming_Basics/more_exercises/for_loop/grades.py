number_of_students = int(input())
total_grade = 0
fail = 0
between_3_4 = 0
between_4_5 = 0
top_students = 0

for i in range(number_of_students):
    grade = float(input())
    total_grade += grade
    if grade < 3:
        fail += 1
    elif 3 <= grade < 4:
        between_3_4 += 1
    elif 4 <= grade < 5:
        between_4_5 += 1
    else:
        top_students += 1

average_grade = total_grade / number_of_students
fail_percentage = fail / number_of_students * 100
between_3_4_percentage = between_3_4 / number_of_students * 100
between_4_5_percentage = between_4_5 / number_of_students * 100
top_students_percentage = top_students / number_of_students * 100

print(f"Top students: {top_students_percentage:.02f}%")
print(f"Between 4.00 and 4.99: {between_4_5_percentage:.02f}%")
print(f"Between 3.00 and 3.99: {between_3_4_percentage:.02f}%")
print(f"Fail: {fail_percentage:.02f}%")
print(f"Average: {average_grade:.02f}")