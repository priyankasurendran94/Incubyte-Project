def add(numbers: str) -> int:
    # If the string is empty, return 0
    if not numbers:
        return 0
    
    # Split the string by commas and sum the numbers
    number_list = numbers.split(',')
    return sum(int(num) for num in number_list)

# Example tests:
print(add(""))  # Expected output: 0
print(add("1"))  # Expected output: 1
print(add("1,2"))  # Expected output: 3