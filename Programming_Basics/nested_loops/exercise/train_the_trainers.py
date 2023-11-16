jury_number = int(input())
number_of_presentations = 0
total_average = 0
name_of_the_presentation = input()

while name_of_the_presentation != "Finish":
    number_of_presentations += 1
    presentation_total_grade = 0
    for _ in range(jury_number):
        current_grade = float(input())
        presentation_total_grade += current_grade
    presentation_average = presentation_total_grade / jury_number
    total_average += presentation_average
    print(f"{name_of_the_presentation} - {presentation_average:.2f}.")
    name_of_the_presentation = input()
else:
    average_grade = total_average / number_of_presentations
    print(f"Student's final assessment is {average_grade:.2f}.")