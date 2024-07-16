# my_first_solution:

#from collections import deque

# def time_convertor(time, seconds):
#     h, m, s = time.split(':')
#     sec = (int(s) + seconds) % 60
#     min_ = ((int(s) + seconds) // 60 + int(m)) % 60
#     h = int(h) + ((int(s) + seconds) // 60 + int(m)) // 60
#     if h >= 24:
#         h -= 24
#     return f"{h:02}:{min_:02}:{sec:02}"
#
#
# robots = deque(r.split('-') for r in input().split(';'))
# start_time = input()
# details = deque()
#
# while True:
#     detail = input()
#     if detail == 'End':
#         break
#     details.append(detail)
#
# current_second = 0
# working_robots = {}
#
# while details:
#     current_second += 1
#     if len(robots) > 0:
#         current_robot = robots.popleft()
#         time = time_convertor(start_time, current_second)
#         print(f"{current_robot[0]} - {details.popleft()} [{time}]")
#         working_robots[(current_robot[0], current_robot[1])] = int(current_robot[1])
#     else:
#         details.rotate(-1)
#     copied_working_robots = working_robots.copy()
#     for k, v in copied_working_robots.items():
#         working_robots[k] -= 1
#         if working_robots[k] == 0:
#             robots.append(k)
#             del working_robots[k]


#second solution:

# from collections import deque
# from datetime import datetime, timedelta
#
# robots = deque(r.split('-') for r in input().split(';'))
# time = datetime.strptime(input(), '%H:%M:%S')
# details = deque()
#
# while True:
#     detail = input()
#     if detail == 'End':
#         break
#     details.append(detail)
#
# working_robots = {}
#
# while details:
#     time += timedelta(seconds=1)
#     current_detail = details.popleft()
#     if len(robots) > 0:
#         current_robot = robots.popleft()
#         print(f"{current_robot[0]} - {current_detail} [{time.strftime('%H:%M:%S')}]")
#         working_robots[(current_robot[0], current_robot[1])] = int(current_robot[1])
#     else:
#         details.append(current_detail)
#     copied_working_robots = working_robots.copy()
#     for k, v in copied_working_robots.items():
#         working_robots[k] -= 1
#         if working_robots[k] == 0:
#             robots.append(k)
#             del working_robots[k]


#third solution -> 100/100 in judge

from collections import deque
from datetime import datetime, timedelta

robots = {}

for r in input().split(';'):
    name, time = r.split('-')
    robots[name] = [int(time), 0]

time = datetime.strptime(input(), '%H:%M:%S')
product = deque()

while True:
    command = input()
    if command == 'End':
        break
    product.append(command)

while product:
    time += timedelta(seconds=1)
    current_product = product.popleft()
    free_robots = deque()
    for k, v in robots.items():
        if robots[k][1] == 0:
            free_robots.append(k)
    if free_robots:
        robot_name = free_robots.popleft()
        robots[robot_name][1] = robots[robot_name][0]
        print(f"{robot_name} - {current_product} [{time.strftime('%H:%M:%S')}]")
    else:
        product.append(current_product)
    for k, v in robots.items():
        if robots[k][1] != 0:
            robots[k][1] -= 1