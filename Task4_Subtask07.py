#Write a python program to find the first non-repeating elements in a given list of integers?
def first_nonrepeating_number(nums):
    count = {}
    #Count the frequency of each number
    for num in nums:
        count[num] = count.get(num, 0) + 1
    #Find first element with frequency 1
    for num in nums:
        if count[num] == 1:
            return num

    return None #if no non repeating numbers found

nums = [4, 5, 2, 4, 5, 2, 8, 10]
solution = first_nonrepeating_number(nums)

if solution is not None:
    print(f"First non repeating number in list: {solution}")
else:
    print("No non-repeating numbers fount in list")
