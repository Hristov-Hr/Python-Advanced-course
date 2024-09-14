chars = input()

result = {}

for x in chars:
    result[x] = chars.count(x)

[print(f"{k}: {v} time/s") for k, v in sorted(result.items())]