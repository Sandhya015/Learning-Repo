def sum_binary_digits(binary_number):
    binary_string = str(binary_number)

    binary_sum = sum(int(digit) for digit in binary_string)

    return binary_sum

binary_num = '110101'  
print(f"Sum of binary digits: {sum_binary_digits(binary_num)}")
