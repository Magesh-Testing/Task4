#You have been given a Python list [10, 20, 30, 9] and a value of 59. Write a python program to find the triplet in the list whose sum is equal to the given value?
def find_triplet_with_sum(arr, target):
    triplet_count = 0
    final_temp_lst = []

    for i in range(0, len(arr) - 1):

        s = set()
        temp_lst = []

        # Adding first element
        temp_lst.append(arr[i])

        curr_k = target - arr[i]

        for j in range(i + 1, len(arr)):

            if (curr_k - arr[j]) in s:
                triplet_count += 1

                # Adding second element
                temp_lst.append(arr[j])

                # Adding third element
                temp_lst.append(curr_k - arr[j])

                # Appending tuple to the final list
                final_temp_lst.append(tuple(temp_lst))
                temp_lst.pop(2)
                temp_lst.pop(1)
            s.add(arr[j])

    return final_temp_lst


# Driver Code
arr = [10, 20, 30, 9]
target = 59
print(find_triplet_with_sum(arr, target))