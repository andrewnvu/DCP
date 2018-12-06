#Find the first missing positive in a an array of integers


def first_missing_positive(numbers):
    #gets rid of negative numbers
    s = set(numbers)
    i = 1

    #if 1 is in the set, increment it until i is not in s
    while i in s:
        i += 1
    
    return i


myArray = [1,2,4,-2, -5]
print(first_missing_positive(myArray))