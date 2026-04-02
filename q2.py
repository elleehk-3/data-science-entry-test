def find_and_replace(lst, find_val, replace_val):
    # Check if type of lst is a list
    if not type(lst).__name__ == 'list':
        return -1
    # Replace all occurrences of find_val with replace_val
    for i in range(len(lst)):
        if lst[i] == find_val:
            lst[i] = replace_val
    return lst

# Task 2
# Invoke the function "find_and_replace" using the following scenarios:
# - [1, 2, 3, 4, 2, 2], 2, 5
# - ["apple", "banana", "apple"], "apple", "orange"

print(find_and_replace([1, 2, 3, 4, 2, 2], 2, 5))
print(find_and_replace(["apple", "banana", "apple"], "apple", "orange"))      
