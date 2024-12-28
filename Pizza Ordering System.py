print("Welcome to the Pizza Ordering System!")


print("\nPizza Menu:")
print("Small Pizza: Rs.150")
print("Medium Pizza: Rs.200")
print("Large Pizza: Rs.250")
print("Extras:")
print("Pepperoni for Small Pizza: Rs.20")
print("Pepperoni for Medium or Large Pizza: Rs.30")
print("Extra cheese for any size pizza: Rs.10")

size = input("\nEnter the size of pizza you want (S for Small, M for Medium, L for Large): ").upper()

bill = 0

if size == 'S':
    bill += 150
elif size == 'M':
    bill += 200
elif size == 'L':
    bill += 250
else:
    print("Invalid choice! Please restart the program and select a valid size.")
    exit()

pepperoni = input("Do you want pepperoni? (Y for Yes, N for No): ").strip().upper()

if pepperoni == 'Y':
    if size == 'S':
        bill += 20
    else:
        bill += 30

extra_cheese = input("Do you want extra cheese? (Y for Yes, N for No): ").strip().upper()

if extra_cheese == 'Y':
    bill += 10

print(f"\nYour total bill is: Rs.{bill}")
print("Thank you for your order!")
