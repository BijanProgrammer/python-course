import random

n = int(random.random() * 100)
print(n)

while True:
    guess = int(input("guess a number from 0 to 99: "))
    
    if guess == -1:
        print("Bye!")
        break
    
    if guess == n:
        print("YES!")
        break
    elif guess < n:
        print("guess higher")
    else:
        print("guess lower")
