a = float(input("Enter a: "))
b = float(input("Enter b: "))

def solution_equation(a, b):
    if a == 0:
        if b < 0:
            print("Phuong trinh co vo so nghiem")
        else:
            print("Phuong trinh co vo nghiem")
    elif a > 0:
        print("x <", -b/a)
    elif a < 0:
        print("x >" , -b/a)

print("equation: ",a,"x + ",b," <0")
solution_equation(a, b)