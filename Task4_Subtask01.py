#You have been given a python list [10, 501, 22, 37, 100, 999, 87, 351] your task is to create two list one which have all the Even Number and another list which will have all the ODD numbers in it?
numbers = [10, 501, 22, 37, 100, 999, 87, 351]
#Empty list to store even and odd number output
even_numbers = []
odd_numbers = []

#Loop to find even and odd numbers
for n in numbers:
    if n % 2 == 0:
        even_numbers.append(n)
    else:
        odd_numbers.append(n)

print(f"Even Numbers: {even_numbers}")
print(f"Odd numbers Count: {odd_numbers}")