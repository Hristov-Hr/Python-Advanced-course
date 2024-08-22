def binary_search(lst, num):

    if num not in lst:
        return -1
    mid_lst = len(lst) // 2
    if lst[mid_lst] == num:
        return mid_lst
    elif lst[mid_lst] > num:
        return binary_search(lst[:mid_lst], num)
    else:
        return mid_lst + binary_search(lst[mid_lst:], num)


numbers = [int(n) for n in input().split()]
searched_number = int(input())
print(binary_search(numbers, searched_number))