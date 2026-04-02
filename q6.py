def find_first_negative(lst):
    # Finds the first negative number in a list.
    # Returns the first negative number if found, otherwise returns "No negatives".
    
    i = 0  # start index
    
    # Using a while loop to loop through the list
    while i < len(lst):
        if isinstance(lst[i], (int, float)) and lst[i] < 0:
            return lst[i]  # return the first negative number
        i += 1  # move to the next element
    
    # If no negative number is found
    return "No negatives"

# Task 2
# Invoke the function "find_first_negative" using the following scenario:
# - [3, 5, -1, 7, -2, 8]
# - [2, 10, 7, 0]

print(find_first_negative([3, 5, -1, 7, -2, 8]))   # Output: -1
print(find_first_negative([2, 10, 7, 0]))     # Output: "No negatives"
