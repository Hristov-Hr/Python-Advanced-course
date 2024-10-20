from collections import deque

strength_of_kicks = [int(n) for n in input().split()]
accuracies = deque(int(n) for n in input().split())
goals_scored = 0

while strength_of_kicks and accuracies:

    strength = strength_of_kicks.pop()
    accuracy = accuracies.popleft()

    if strength + accuracy == 100:
        goals_scored += 1
        continue

    if strength + accuracy > 100:
        strength -= 10
        accuracies.append(accuracy)
        strength_of_kicks.append(strength)
        continue

    if accuracy > strength:
        accuracies.appendleft(accuracy)
    else:
        if accuracy == strength:
            strength += accuracy
        strength_of_kicks.append(strength)

goals = {
    4: "Paul performed remarkably well!",
    3: "Paul scored a hat-trick!",
    1: "Paul failed to make a hat-trick.",
    0: "Paul failed to score a single goal."
}

for goal in goals:
    if goals_scored >= goal:
        print(goals[goal])
        break
if goals_scored:
    print(f"Goals scored: {goals_scored}")
if strength_of_kicks:
    print(f"Strength values left: {', '.join(str(x) for x in strength_of_kicks)}")
if accuracies:
    print(f"Accuracy values left: {', '.join(str(x) for x in accuracies)}")
