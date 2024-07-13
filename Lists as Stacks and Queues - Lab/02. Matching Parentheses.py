text = input()
stack = []

for i in range(len(text)):
    if text[i] == '(':
        stack.append(i)
    elif text[i] == ')':
        start_index = stack.pop()
        end_index = i + 1
        print(text[start_index:end_index])