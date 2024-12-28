number = int(input("Enter a number: "))

if 20 <= number <= 50:
    if number % 5 == 0:
        print(f"{number} is between 20 and 50 and divisible by 5.")
    else:
        print(f"{number} is between 20 and 50 but not divisible by 5.")
else:
    print(f"{number} is not between 20 and 50.")
