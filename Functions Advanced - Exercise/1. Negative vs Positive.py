def sort_numbers(*args):

    positive_numbers = [int(num) for num in args if int(num) > 0]
    negative_numbers = [int(num) for num in args if int(num) < 0]
    stronger_num = 'positives' if sum(positive_numbers) > abs(sum(negative_numbers)) else 'negatives'
    weaker_num = 'positives' if sum(positive_numbers) < abs(sum(negative_numbers)) else 'negatives'

    return f"{sum(negative_numbers)}\n{sum(positive_numbers)}\nThe {stronger_num} are stronger than the {weaker_num}"


print(sort_numbers(*input().split()))