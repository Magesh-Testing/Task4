#Given a list [4, 2, -3, 1, 6] write a python program to find if there is a sub-list with sum equal to zero?
def contains_zero_sum_sublist(arr):
    found_sums = set()
    curr_sum = 0

    for num in arr:
        curr_sum += num
        if curr_sum == 0 or curr_sum in found_sums:
            return True
        found_sums.add(curr_sum)

    return False

# Input Values
arr = [4, 2, -3, 1, 6]
if contains_zero_sum_sublist(arr):
    print("Found a sub-list with sum equal to zero.")
else:
    print("No sub-list with sum equal to zero.")
