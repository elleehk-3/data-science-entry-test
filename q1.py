def swap(x, y):
    # Check if both inputs are numeric (int or float)
    if not (isinstance(x, (int, float)) and isinstance(y, (int, float))):
        return -1

    # Swapping logic using arithmetic
    x = x + y  # x now holds the sum of both
    y = x - y  # y is now (original x + original y) - original y = original x
    x = x - y  # x is now (original x + original y) - original x = original y

    print(f"Swapped values: x = {x}, y = {y}")
    return x, y
