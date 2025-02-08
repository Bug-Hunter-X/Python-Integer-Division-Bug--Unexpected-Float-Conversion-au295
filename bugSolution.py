def function_with_uncommon_bug_solution(input_list):
    result = []
    for i in range(len(input_list)):
        if input_list[i] % 2 == 0:
            result.append(input_list[i] * 2)
        else:
            result.append(input_list[i] // 2) # Use floor division to get integer result
    return result

my_list = [1, 2, 3, 4, 5, 6]
output = function_with_uncommon_bug_solution(my_list) 
print(output) # Output: [0, 4, 1, 8, 2, 12]

#The solution is to use floor division (//) instead of standard division (/) when dealing with integers and expecting integer results. This will ensure that the result of the division is always an integer, avoiding the unexpected float conversion. 