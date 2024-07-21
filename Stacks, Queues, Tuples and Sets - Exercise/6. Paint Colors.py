from collections import deque

main_colors = ("red", "yellow", "blue")

substrings_sequence = deque(input().split())

while substrings_sequence:
    first_substring = substrings_sequence.popleft()
    second_substring = substrings_sequence.pop()
