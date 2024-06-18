def gather_credits(needed_credits, *courses):
    taken_courses = []
    acquired_credits = 0

    for course, course_credits in courses:
        if acquired_credits < needed_credits:
            if course not in taken_courses:
                taken_courses.append(course)
                acquired_credits += course_credits
        else:
            break

    if needed_credits <= acquired_credits:
        return f"Enrollment finished! Maximum credits: {acquired_credits}.\n" \
               f"Courses: {', '.join(sorted(taken_courses))}"
    return f"You need to enroll in more courses! " \
           f"You have to gather {needed_credits - acquired_credits} credits more."


print(gather_credits(
    80,
    ("Basics", 27),
))
print(gather_credits(
    80,
    ("Advanced", 30),
    ("Basics", 27),
    ("Fundamentals", 27),
))
print(gather_credits(
    60,
    ("Basics", 27),
    ("Fundamentals", 27),
    ("Advanced", 30),
    ("Web", 30)
))
