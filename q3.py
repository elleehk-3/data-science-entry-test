def update_dictionary(dct, key, value):
    # Check if dct is a dictionary
    if not type(dct).__name__ == 'dict':
        return -1
    
    # If the key already exists, print the original value
    if key in dct:
        print("Original value for key '{}': {}".format(key, dct[key]))
    
    # Update or add the key-value pair
    dct[key] = value
    
    # Return the updated dictionary
    return dct

# Task 2
# Invoke the function "update_dictionary" using the following scenarios:
# - {}, "name", "Alice"
# - {"age": 25}, "age", 26

print(update_dictionary({}, "name", "Alice"))
print(update_dictionary({"age": 25}, "age", 26))
