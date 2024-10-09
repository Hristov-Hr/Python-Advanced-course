def students_credits(*args):
    course_data = {}
    total_credits = 0

    for a in args:
        course, *data = a.split('-')
        credit, max_points, points = [int(n) for n in data]
        current_credits = credit / (max_points / points) if points > 0 else 0
        course_data[course] = current_credits
        total_credits += current_credits

    sorted_data = sorted(course_data.items(), key=lambda x: -x[1])
    result = [f"Diyan gets a diploma with {total_credits:.1f} credits."] if total_credits >= 240 else \
        [f"Diyan needs {240 - total_credits:.1f} credits more for a diploma."]
    for k, v in sorted_data:
        result.append(f"{k} - {v:.1f}")

    return '\n'.join(result)




print(
    students_credits(
        "Computer Science-12-300-250",
        "Basic Algebra-15-400-200",
        "Algorithms-25-500-490"
    )
)
print(
    students_credits(
        "Discrete Maths-40-500-450",
        "AI Development-20-400-400",
        "Algorithms Advanced-50-700-630",
        "Python Development-15-200-200",
        "JavaScript Development-12-500-480",
        "C++ Development-30-500-405",
        "Game Engine Development-70-100-70",
        "Mobile Development-25-250-225",
        "QA-20-300-300",
    )
)
print(
    students_credits(
        "Python Development-15-200-200",
        "JavaScript Development-12-500-480",
        "C++ Development-30-500-405",
        "Java Development-10-300-150"
    )
)
