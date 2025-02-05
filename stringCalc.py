import re

class StringCalculator:
    def add(self, numbers: str) -> int:
        if not numbers:
            return 0
    
    # Split the string by commas and sum the numbers
        number_list = numbers.split(',')
        return sum(int(num) for num in number_list)

if __name__ == "__main__":
    calculator = StringCalculator()
    print(calculator.add(""))  # Expected output: 0
    print(calculator.add("1"))  # Expected output: 1
    print(calculator.add("1,5"))  # Expected output: 6