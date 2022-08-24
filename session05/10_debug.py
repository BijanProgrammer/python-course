def add(numbers):
    result = 0
    
    for number in numbers:
        result += number
    
    return result


def average(numbers):
    add_result = add(numbers)
    count = len(numbers)
    
    return add_result / count


numbers = []
numbers.append(4)
numbers.append(8)
numbers.append(15)
numbers.append(16)
numbers.append(23)
numbers.append(42)

average_result = average(numbers)
print(average_result)
