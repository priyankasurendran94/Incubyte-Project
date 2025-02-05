import re

class StringCalculator:
    def add(self, numbers: str) -> int:
        if not numbers:
            return 0

        custom_delimiters = [",", "\n"]  # Default delimiters
        delimiter_pattern = r"^//(.+?)\n"

        # Check for custom delimiter
        match = re.match(delimiter_pattern, numbers)
        if match:
            delimiter_section = match.group(1)
            numbers = numbers[len(match.group(0)):]  # Remove delimiter declaration from input

            if delimiter_section.startswith("[") and delimiter_section.endswith("]"):
                # Handle multiple or multi-character delimiters: //[*][%%]\n
                custom_delimiters = re.findall(r"\[(.*?)\]", delimiter_section)
            else:
                # Handle single-character delimiter: //;\n
                custom_delimiters = [delimiter_section]

        # Create regex pattern for splitting using multiple delimiters
        delimiter_regex = "|".join(map(re.escape, custom_delimiters))
        num_list = re.split(delimiter_regex, numbers)
        int_list = []
        for num in num_list:
            if num:
                try:
                    value = int(num)
                    int_list.append(value)
                except ValueError:
                    continue
        return sum(int_list)
    
if __name__ == "__main__":
    calculator = StringCalculator()
    print(calculator.add(""))  # Expected output: 0
    print(calculator.add("1"))  # Expected output: 1
    print(calculator.add("1,5"))  # Expected output: 6
    print(calculator.add("1\n2,3"))  # Expected output: 6

    print(calculator.add("//;\n1;2"))  # Expected output: 3
    print(calculator.add("//[]\n1*2**3"))  # Expected output: 6
    print(calculator.add("//[*][%]\n1*2%3"))  # Expected output: 6