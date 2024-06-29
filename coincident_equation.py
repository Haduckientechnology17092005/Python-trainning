import math
print("Giai he phuong trinh trung phuong")
print("He phuong trinh co dang: ax^4 + bx^2 + c = 0")
print("Nhap he so:")
a = float(input("a = "))
b = float(input("b = "))
c = float(input("c = "))
def solution(a, b, c):
    if a == 0:
        if b==0:
            if c==0:
                print("Phuong trinh co vo so nghiem")
            else:
                print("Phuong trinh vo nghiem")
        else:
            if b*c > 0:
                print("phuong trinh vo nghiem")
            else:
                x1 = math.sqrt(-c/b)
                x2 = -math.sqrt(-c/b)
                print("x1 = ", x1)
                print("x2 = ", x2)
    else:
        delta = b*b - 4*a*c
        if delta < 0:
            print("Phuong trinh vo nghiem")
        elif delta == 0:
            t = -1*b/(2*a)
            if t < 0:
                print("Phuong trinh vo nghiem")
            elif t == 0:
                x1=x2=0
                print("x1 = ", x1)
                print("x2 = ", x2)
            else:
                x1 = math.sqrt(t)
                x2 = -math.sqrt(t)
                print("x1 = ", x1)
                print("x2 = ", x2)
        else:
            t1 = (-b + math.sqrt(delta))/(2*a)
            t2 = (-b - math.sqrt(delta))/(2*a)
            if t1 < 0 and t2 < 0:
                print("Phuong trinh vo nghiem")
            elif t1 == 0 and t2 == 0:
                x1 = x2 = 0
                print("x1 = ", x1)
                print("x2 = ", x2)
            elif t1 > 0 and t2 > 0:
                x1 = math.sqrt(t1)
                x2 = -math.sqrt(t1)
                x3 = math.sqrt(t2)
                x4 = -math.sqrt(t2)
                print("x1 = ", x1)
                print("x2 = ", x2)
                print("x3 = ", x3)
                print("x4 = ", x4)
            elif t1 > 0 and t2 < 0:
                x1 = math.sqrt(t1)
                x2 = -math.sqrt(t1)
                print("x1 = ", x1)
                print("x2 = ", x2)
            elif t1 < 0 and t2 > 0:
                x1 = math.sqrt(t2)
                x2 = -math.sqrt(t2)
                print("x1 = ", x1)
                print("x2 = ", x2)
            elif t1 == 0 and t2 < 0:
                x1 = 0
                print("x1 = ", x1)
            elif t1 == 0 and t2 > 0:
                x1 = 0
                x2 = math.sqrt(t2)
                x3 = -math.sqrt(t2)
                print("x1 = ", x1)
                print("x2 = ", x2)
                print("x3 = ", x3)
            elif t1 < 0 and t2 == 0:
                x1 = 0
                print("x1 = ", x1)
            elif t1 > 0 and t2 == 0:
                x1 = math.sqrt(t1)
                x2 = -math.sqrt(t1)
                x3 = 0
                print("x1 = ", x1)
                print("x2 = ", x2)
                print("x3 = ", x3)
                
def menu():
    print("He phuong trinh co dang: ",a,"x^4 + ",b,"x^2 + ",c," = 0")
    solution(a, b, c)

menu()