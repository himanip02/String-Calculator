def add(numbers):
    if not numbers:
        return 0
    delimiter = ","
    if numbers.startswith("//"):
        parts = numbers.split("\n", 1)
        delimiter = parts[0][2:]
        numbers = parts[1]
    numbers = numbers.replace("\n", delimiter)
    num_list = list(map(int, numbers.split(delimiter)))
    negative_num = [num for num in num_list if num < 0]
    if negative_num:
        raise ValueError(f"Negative numbers are not allowed: {', '.join(map(str, negative_num))}")
    return sum(num_list)
