def softuni_students(*args, **kwargs):
    student_data = {}
    invalid_name = []

    for course_id, username in args:
        course_name = kwargs.get(course_id)
        if course_name:
            student_data[username] = course_name
        else:
            invalid_name.append(username)

    sorted_student = sorted(student_data.items(), key=lambda x: x[0])
    result = []
    for k, v in sorted_student:
        result.append(f"*** A student with the username {k} has successfully finished the course {v}!")
    if invalid_name:
        result.append(f"!!! Invalid course students: {', '.join(sorted(invalid_name))}")

    return "\n".join(result)


print(softuni_students(
    ('id_1', 'Kaloyan9905'),
    id_1='Python Web Framework',
))
print(softuni_students(
    ('id_7', 'Silvester1'),
    ('id_32', 'Katq21'),
    ('id_7', 'The programmer'),
    id_76='Spring Fundamentals',
    id_7='Spring Advanced',
))
print(softuni_students(
    ('id_22', 'Programmingkitten'),
    ('id_11', 'MitkoTheDark'),
    ('id_321', 'Bobosa253'),
    ('id_08', 'KrasimirAtanasov'),
    ('id_32', 'DaniBG'),
    id_321='HTML & CSS',
    id_22='Machine Learning',
    id_08='JS Advanced',
))
