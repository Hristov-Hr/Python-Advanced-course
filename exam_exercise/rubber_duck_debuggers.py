from collections import deque

programmer_times = deque(int(n) for n in input().split())
numbers_of_tasks = [int(n) for n in input().split()]

mapper = {60: 'Darth Vader Ducky',
          120: 'Thor Ducky',
          180: 'Big Blue Rubber Ducky',
          240: 'Small Yellow Rubber Ducky'
          }
created_duckies = {
    "Darth Vader Ducky": 0,
    "Thor Ducky": 0,
    "Big Blue Rubber Ducky": 0,
    "Small Yellow Rubber Ducky": 0
}

while programmer_times and numbers_of_tasks:
    time = programmer_times.popleft()
    task = numbers_of_tasks.pop()
    value = time * task

    for i in mapper.items():
        if value <= i[0]:
            created_duckies[i[1]] += 1
            break

    else:
        programmer_times.append(time)
        numbers_of_tasks.append(task - 2)

task_is_completed = all(d for d in created_duckies.values() if d > 0)
if task_is_completed:
    print("Congratulations, all tasks have been completed! Rubber ducks rewarded:")
[print(f"{k}: {v}") for k, v in created_duckies.items()]

