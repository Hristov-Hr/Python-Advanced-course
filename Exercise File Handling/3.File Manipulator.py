import os

while True:
    command = input().split('-')
    if command[0] == 'End':
        break

    elif command[0] == 'Create':
        with open(command[1], "w") as file:
            file.write('')

    elif command[0] == 'Add':
        with open(command[1], "a") as file:
            file.write(f"{command[2]}\n")

    elif command[0] == 'Replace':
        file_name, old, new = command[1], command[2], command[3]
        try:
            with open(file_name, "r+") as file:

                text = file.read()
                text = text.replace(old, new)
                file.seek(0)
                file.write(text)
                file.truncate()

        except FileNotFoundError:
            print("An error occurred")

    elif command[0] == 'Delete':
        try:
            os.remove(command[1])

        except FileNotFoundError:
            print("An error occurred")



