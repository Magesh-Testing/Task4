#You have been given three lists. Your task is to find the duplicates in the three lists. Write a python program for the same. You can use your own python lists?

def find_common_element_in_three_list(list1, list2, list3):
    # Convert lists to sets
    set1 = set(list1)
    set2 = set(list2)
    set3 = set(list3)

    common = set1 & set2 & set3
    return list(common)


list1 = [1, 2, 3, 4, 5, 6]
list2 = [6, 7, 8, 9, 10, 11, 2]
list3 = [0, 2,  7, 5, 6, 12, 13]
#find duplicates in list
duplicates = find_common_element_in_three_list(list1, list2, list3)
print(f"Duplicates in all three lists are: {duplicates}")