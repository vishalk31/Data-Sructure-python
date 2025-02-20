def binary_search_name(list_of_names, target_name):
    low = 0
    high = len(list_of_names) - 1

    while low <= high:
        mid = (low + high) // 2
        guess_name = list_of_names[mid]

        if guess_name == target_name:
            return mid

        # Lexicographical comparison (alphabetical order)
        if guess_name > target_name:  # guess_name comes *after* target_name alphabetically
            high = mid - 1
        else:  # guess_name comes *before* or is equal to target_name alphabetically
            low = mid + 1

    return None

# Example usage:
names = ["Alice", "Bob", "Charlie", "David", "Eve"]  # Must be sorted!
target = "Charlie"
result = binary_search_name(names, target)

if result is not None:
    print(f"{target} found at index {result}")
else:
    print(f"{target} not found")

target = "Frank"  # Not in the list
result = binary_search_name(names, target)

if result is not None:
    print(f"{target} found at index {result}")
else:
    print(f"{target} not found")
