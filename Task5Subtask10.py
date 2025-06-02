def contains_zero_sum_sublist(arr):
    found_sums = set()
    current_sum = 0

    for num in arr:
        current_sum += num
        if current_sum == 0 or current_sum in found_sums:
            return True
        found_sums.add(current_sum)

    return False

# Example usage
arr = [4, 2, -3, 1, 6]
if contains_zero_sum_sublist(arr):
    print("Found a sub-list with sum equal to zero.")
else:
    print("No sub-list with sum equal to zero.")
