#Write a python program to find the sum of the first and last digit of an integer?
def sum_first_last_digit(nos):
    #TO make sure given number is positive
    nos = abs(nos)
    #Converting given number to string
    conv_num_str = str(nos)

    #Finding the first number using index and converting it to number
    first_digit = int(conv_num_str[0])
    print("first_digit ", first_digit)
    # Finding the last number using index and converting it to number
    last_digit = int(conv_num_str[-1])
    print("last_digit ", last_digit)

    #Adding first and last number and returning to function sum_first_last_digit
    return first_digit + last_digit

#Getting absolute number from user
val = int(input("Enter a absolute number: "))

result = sum_first_last_digit(val)
print(f"Sum of first and last digits are: {result}")