def sum_of_arrays(arr1, arr2):
    if len(arr1) != len(arr2):
        return "Arrays must have the same length"

    result = []
    
    for i in range(len(arr1)):
        result.append(arr1[i] + arr2[i])
    
    return result


array1 = [1, 2, 3, 4]
array2 = [5, 6, 7, 8]


sum_result = sum_of_arrays(array1, array2)
print("Sum of the arrays:", sum_result)
