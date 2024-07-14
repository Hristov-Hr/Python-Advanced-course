parentheses_sequence = input()

parentheses_stack = []
is_balanced = 'YES'

for char in parentheses_sequence:
    if char in '([{':
        parentheses_stack.append(char)
    else:
        if len(parentheses_stack) == 0:
            is_balanced = 'NO'
            break
        last_char = parentheses_stack.pop()
        if last_char + char in '(),{},[]':
            continue
        is_balanced = 'NO'
        break
if len(parentheses_stack) > 0:
    is_balanced = 'NO'
print(is_balanced)