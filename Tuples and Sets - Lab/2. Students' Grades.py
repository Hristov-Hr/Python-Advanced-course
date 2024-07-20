grades = {}

for _ in range(int(input())):
    name, grade = input().split()
    if name not in grades:
        grades[name] = []
    grades[name].append(float(grade))

for k, v in grades.items():
    print(f"{k} -> {' '.join([f'{x:.2f}' for x in v])} (avg: {sum(v) / len(v):.2f})")