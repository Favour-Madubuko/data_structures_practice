#This is a binary search question
the_requested_value = int(input("Input a number:\n"))
def searchInsertPosition():
    array = [10,12,17,20,21,23,32,33,37,38,90,100,102]
    lower_bound = 0
    upper_bound = len(array)- 1
    the_value_at_midpoint = array[midpoint]

    while lower_bound <= upper_bound:
        midpoint = (lower_bound+upper_bound)/2
        if the_requested_value == the_value_at_midpoint:
            return midpoint
        elif the_requested_value < the_value_at_midpoint:
            upper_bound = midpoint - 1
        elif the_requested_value > the_value_at_midpoint:
            lower_bound = midpoint + 1
    return -1
