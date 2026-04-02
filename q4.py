def string_reverse(s):
    # Check if s is a string
    if not type(s).__name__ == 'str':
        return -1
    
    # Reverse the string
    reversed_s = s[::-1]
    
    # Return the reversed string
    return reversed_s

# Task 2
# Invoke the function "string_reverse" using the following scenarios:
# - "Hello World"
# - "Python"

print(string_reverse("Hello World"))
print(string_reverse("Python"))
