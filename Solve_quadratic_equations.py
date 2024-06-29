import math
a = float(input("Enter a: "))
b = float(input("Enter b: "))
c = float(input("Enter c: "))

def solution_equation(a, b, c):
    if a == 0:
        if b == 0:
            if c == 0:
                print("Phuong trinh co vo so nghiem")
            else:
                print("Phuong trinh vo nghiem")
        else:
            print("Phuong trinh co 1 nghiem: ", -c/b)
    else:
        if b==0:
            if a*c == 0:
                x = 0
                print("x = ", x)
            elif a*c > 0:
                print("Phuong trinh vo nghiem")
            else:
                x1 = math.sqrt(-c/a)
                x2 = -math.sqrt(-c/a)
                print("x1 = ", x1)
                print("x2 = ", x2)
        else:
            delta = b*b - 4*a*c
            if delta < 0:
                print("Phuong trinh vo nghiem")
            elif delta == 0:
                x = -b/(2*a)
                print("x = ", x)
            else:
                x1 = (-b + math.sqrt(delta))/(2*a)
                x2 = (-b - math.sqrt(delta))/(2*a)
                print("x1 = ", x1)
                print("x2 = ", x2)
print("equation: ",a,"x^2 + ",b,"x + ",c," = 0")
solution_equation(a, b, c)