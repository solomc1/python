#A nested list of integers
#
# * an integer
# * a nested list of integers


def sum_numbers(nested_list: 'a nested list of integers'f) -> int:
    sum = 0

    for element in numlist:
        if type(element) == int:
            sum += element
        else:
            sum += sum_numbers(element)
    return sum
