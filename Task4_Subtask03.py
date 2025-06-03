#Given a Python List [10, 501, 22, 37, 100, 999, 87, 351] Find out how many numbers are there in the given Python List which are Happy Numbers?
numbers = [10, 501, 22, 37, 100, 999, 87, 351]

#Empty list to store happy numbers
happynos = []

# Simple function to check happy number
def check_happy(n):
    seen = []
    while n != 1 and n not in seen:
        seen.append(n)
        tot = 0
        for digit in str(n):
            tot += int(digit) ** 2
        n = tot
    return n == 1

# Check each number in the list
for num in numbers:
    if check_happy(num):
        happynos.append(num)

print(f"Happy Numbers:{happynos}")
print(f"Count of Happy Numbers: {len(happynos)}")