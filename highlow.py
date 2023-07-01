def high_and_low(numbers):
    # split and convert
    numbers = [int(i) for i in numbers.split(" ")]
    # use min and max to return result
    return str(max(numbers)) + " " + str(min(numbers))