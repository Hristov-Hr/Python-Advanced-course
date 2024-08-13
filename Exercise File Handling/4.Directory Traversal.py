import os


def save_extensions(directory):

    for file_name in os.listdir(directory):
        file = os.path.join(directory, file_name)

        if os.path.isfile(file):
            extension = file_name.split('.')[-1]
            if extension not in extensions:
                extensions[extension] = []
            extensions[extension].append(file_name)
        elif os.path.isdir(file):
            save_extensions(file)


extensions = {}
directory_name = input()
report = []

try:
    save_extensions(directory_name)
except FileNotFoundError:
    print('Directory not found!')

extensions = sorted(extensions.items(), key=lambda x: x[0])

for ext, name in extensions:
    report.append(f".{ext}")
    for file_ in sorted(name):
        report.append(f"- - - {file_}")

with open('report.txt', 'w') as report_file:
    report_file.write('\n'.join(report))


