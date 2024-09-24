def find_second_smallest(arr):
    if len(arr) < 2:
        return "Array must contain at least two elements."

    first = second = float('inf')

    for num in arr:
        if num < first:
            second = first
            first = num
        elif first < num < second:
            second = num

    if second == float('inf'):
        return "There is no second smallest element."

    return second

array = [12, 13, 1, 10, 34, 1]
result = find_second_smallest(array)
print(f"The second smallest element is: {result}")
