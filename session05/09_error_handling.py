def average(numbers):
    return sum(numbers) / len(numbers)


try:
    print(average([]))
    print(average([4, 8, 15, 16, 23, 42]))
    
    file = open("something.txt", "r")
except ZeroDivisionError:
    print("you should not divide a number by zero")
except FileNotFoundError:
    print("file not found")
