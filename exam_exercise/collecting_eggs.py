from collections import deque

eggs_size = deque(int(n) for n in input().split(', '))
paper_size = [int(n) for n in input().split(', ')]
filled_boxes = 0

while eggs_size and paper_size:
    egg = eggs_size.popleft()
    if egg <= 0:
        continue
    if egg == 13:
        paper_size[0], paper_size[-1] = paper_size[-1], paper_size[0]
        continue
    paper = paper_size.pop()
    if egg + paper <= 50:
        filled_boxes += 1

print("Sorry! You couldn't fill any boxes!") if filled_boxes == 0 else print(f"Great! You filled {filled_boxes} boxes.")
if paper_size:
    print(f"Pieces of paper left: {', '.join(str(p) for p in paper_size)}")
if eggs_size:
    print(f"Eggs left: {', '.join(str(e) for e in eggs_size)}")