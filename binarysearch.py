#Binary search for an ordered array
the_requested_value = int(input("Input a number:\n"))
def binarysearch():
    the_array = [10,12,17,20,21,23,32,33,37,38,90,100,102]
    lower_bound = 0
    upper_bound = len(the_array)- 1

    midpoint = (lower_bound+upper_bound)/2

    the_value_at_midpoint = the_array[midpoint]

    while lower_bound <= upper_bound:
        if the_requested_value == the_value_at_midpoint:
            return midpoint
        elif the_requested_value < the_value_at_midpoint:
            upper_bound = midpoint - 1
        elif the_requested_value > the_value_at_midpoint:
            lower_bound = midpoint + 1
    return -1

