n = int(input("n: "))

numbers = []

i = 1
while i <= n:
    numbers.append(int(input(f"number {i}: ")))
    i += 1

print(numbers)
