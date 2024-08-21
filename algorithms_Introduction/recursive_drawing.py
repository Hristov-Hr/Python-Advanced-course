def recursive_drawing(num):

    print("*" * num)
    if num > 1:
        recursive_drawing(num - 1)
    print("#" * num)


recursive_drawing(int(input()))


# solution 2

# def recursive_drawing(num):
#     if num <= 0:
#         return
#
#     print("*" * num)
#     recursive_drawing(num - 1)
#     print("#" * num)