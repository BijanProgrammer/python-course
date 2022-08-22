def print_numbers(lower_bound=0, upper_bound=10, step=1):
    i = lower_bound
    while i <= upper_bound:
        print(i)
        i += step


print_numbers(23, 108, 15)
print()
print_numbers()
print()
print_numbers(23, 42)
print()
print_numbers(step=2)
