def first_missing_positive(numbers):
    s = set(numbers)
    i = 1

    while i in s:
        i += 1
    
    return i


myArray = [1,2,4,-2, -5]
print(first_missing_positive(myArray))