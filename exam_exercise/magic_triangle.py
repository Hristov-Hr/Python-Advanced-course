def get_magic_triangle(n):

    triangle = [[1], [1, 1]]
    idx = 1

    while len(triangle) < n:
        next_row = [1]
        for i in range(len(triangle[idx]) - 1):
            num = triangle[idx][i] + triangle[idx][i + 1]
            next_row.append(num)
        next_row.append(1)
        triangle.append(next_row)
        idx += 1
    return triangle


get_magic_triangle(5)