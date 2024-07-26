rows, columns = [int(x) for x in input().split()]
for r in range(rows):
    palindromes = []
    for c in range(columns):
        palindromes.append(chr(97 + r) + chr(97 + r + c) + chr(97 + r))
    print(*palindromes)
