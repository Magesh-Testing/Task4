#Write a python program to find the minimum element in a rated and sorted list?
def find_min_number(nos):
    if not nos:
        return None  # Handle empty list

    min = nos[0]
    for num in nos:
        if num < min:
            min = num
    return min

# Example usage
nos = [10, 20, 30, 9, 2]
print("Minimum element is:", find_min_number(nos))