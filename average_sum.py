first_number = float(input("Enter first number: "))
second_number = float(input("Enter second number: "))
third_number = float(input("Enter third number: "))
fourth_number = float(input("Enter fourth number: "))
if (first_number>=-3 and first_number<=3) and (second_number>=-3 and second_number<=3) and (third_number>=-3 and third_number<=3) and (fourth_number>=-3 and fourth_number<=3):
    sum = first_number + second_number + third_number + fourth_number
    average = sum / 4
    print("The sum is: ", sum)
    print("The average is: ", average)
else:
    print("Invalid input")