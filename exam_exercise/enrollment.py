def gather_credits(needed_credits, *args):
    earned_credits = 0
    courses = []

    for course, current_credits in args:
        if earned_credits >= needed_credits:
            break
        if course not in courses:
            earned_credits += current_credits
            courses.append(course)

    if earned_credits < needed_credits:
        return f"You need to enroll in more courses! You have to gather {needed_credits - earned_credits} credits more."

    result = [f"Enrollment finished! Maximum credits: {earned_credits}.", f"Courses: {', '.join(sorted(courses))}"]
    return '\n'.join(result)



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
