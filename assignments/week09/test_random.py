import random

def test_random():
    random_number = random.randint(1, 20)
    guess_number = int(input("Guess number : "))
    if random_number > guess_number:
        print("Too Low")
    elif random_number < guess_number:
        print("Too Much")
    else:
        print("Correct")

random_number = random.randint(1,20)
# attemp = 0
# while True:
#     guess = int(input("Typing Number between 1-20 : "))
#     attep += 1
#     if guess > random_number:
#         print("too high")
#     elif guess < random_number:
#         print("too low")
#     else:
#         print("correct") 
#         print(f"you attemped {attemp}")
#         break
attemp = 5
print(f"you attemped left {attemp}/5")
while True:
    guess = int(input("Typing Number between 1-20 : "))
    attemp -= 1
    if guess > random_number:
        print("too high")
        print(f"you attemped left {attemp}/5")
    elif guess < random_number:
        print("too low")
        print(f"you attemped left {attemp}/5")
    else:
        print("correct") 
        print(f"you attemped left {attemp}/5")
        print(f"you attemped {5-attemp}")
        break
    if attemp == 0:
        break