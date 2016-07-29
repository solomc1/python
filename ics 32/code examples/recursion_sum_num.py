def nested_sum(nested_list: 'nested list of integers')->int:
    '''Adds up the integers in a nested list of integers'''
    sum = 0
    for element in nested_list:
        if type(element) == list:
            sum += nested_sum(element)
        else:
            sum += element
    return sum

