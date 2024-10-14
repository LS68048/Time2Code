# Egyptian multiplication program

# Subprograms
def input_numbers():
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))

    return [num1,num2]

#Ok but what is the point
def mul(nums):
    first_number = nums[0]
    second_number = nums[1]
    column1 = []
    column1.append(first_number)
    while first_number > 1:
        first_number = first_number // 2
        column1.append(first_number)
        
    column2 = []
    column2.append(second_number)
    for i in range(0,len(column1)-1):
        second_number = second_number * 2
        column2.append(second_number)

    column2_counter = 0
    
    for i in range(0,len(column1)-1):
        if column1[i] % 2 == 0:
            column2.pop(column2_counter)
        else:
            column2_counter += 1
    
    total = 0
    for number in column2:
        total += number

    return total
    



# Main program
numbers = input_numbers()

print(mul(numbers))
