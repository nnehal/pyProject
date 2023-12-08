import random as rand

def guess(x):
    low = 0
    high = x
    feedback = ""
    count = 0
    while feedback != "c":
        if low != high:
            guess =rand.randint(low,high)
        else:
            guess = low

        feedback = input(f"Computer guessed {guess} Enter higher or lower than {guess}: ").lower()
        if (feedback == "h"):
            low += 1
        elif (feedback == "l"):
            high -= 1

        count += 1
    print(f"Comp guessed correctly in {count} many tries")

guess(10)