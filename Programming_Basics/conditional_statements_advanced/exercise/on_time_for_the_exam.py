exam_hour = int(input())
exam_minute = int(input())
arrival_hour = int(input())
arrival_minute = int(input())

time_of_exam = exam_hour * 60 + exam_minute
time_of_arrival = arrival_hour * 60 + arrival_minute
difference = abs(time_of_exam - time_of_arrival)

if time_of_exam < time_of_arrival:
    print('Late')
elif time_of_exam - 30 <= time_of_arrival <= time_of_exam:
    print('On time')
else:
    print('Early')

hours = difference // 60
minutes = difference % 60

if time_of_exam - 60 < time_of_arrival < time_of_exam:
    print(f'{minutes} minutes before the start')
elif time_of_arrival <= time_of_exam - 60:
    print(f"{hours}:{minutes:02d} hours before the start")
elif time_of_exam < time_of_arrival < time_of_exam +60:
    print(f"{minutes} minutes after the start")
elif time_of_arrival >= time_of_exam + 60:
    print(f"{hours}:{minutes:02d} hours after the start")