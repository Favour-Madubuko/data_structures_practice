'''
Review the map function in Python and in Java. Using hashmaps to solve 
problems related to list and list comprehension
'''
def plusOne(self, digits):
    digits = [1,2,3,4]
    convert = int(''.join(map(str,digits))) + 1
    return list(map(int,str(convert)))