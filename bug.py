def function_with_uncommon_bug(input_list):
    result = []
    for i in range(len(input_list)):
        if input_list[i] % 2 == 0:
            result.append(input_list[i] * 2)
        else:
            result.append(input_list[i] / 2)
    return result

my_list = [1, 2, 3, 4, 5, 6]
output = function_with_uncommon_bug(my_list) 
print(output) # Output: [0.5, 4, 1.5, 8, 2.5, 12] 

#The bug is subtle: when dealing with integers and performing division, the result is automatically converted to a float, even if the numbers used in the division are integers that would result in an integer division.This can lead to unexpected results in cases where we expect to get integers and this bug is not directly obvious if you are not paying enough attention to it. 