door = int(input("Enter door: "))
if door == 1:
    print("treasure found!")
    print("You win!")
elif door == 2:
    print("Have monster attack you!")
    print("You lose!")
elif door == 3:
    print("Have Dragon attack you!")
    print("You die")
else:
    print("Invalid input")