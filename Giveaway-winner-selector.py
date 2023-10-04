# Importing Packages
import random

# Code
user_list = []
name = ''

print("--- Giveaway winner selector! ---")

while(1):
    name = input("Enter a name (-1 to stop): ")
    if name=='-1':
        break

    user_list.append(name)


winner = random.choice(user_list)
print("||| >> The Winner is ", winner, " << |||")


while(1):
    print("\n1. Re-Roll\n2. Exit")
    choice = input("Enter option number :")
    if choice == '1':
        winner = random.choices(user_list, k=2)
        print("\n||| >> The Winner is ", winner, " << |||")

    elif choice == '2':
        break

    else:
        print("Invalid Option!")

