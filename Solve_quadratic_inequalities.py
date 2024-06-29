import math
print("ham so co dang la: a*x^2 + b*x + c")
a = float(input("Enter a: "))
b = float(input("Enter b: "))
c = float(input("Enter c: "))
def solution_equation_less0(a, b, c):
    if a == 0 or b == 0:
        print("Nhap a va b khac 0")
        return
    else:
        delta = b*b - 4*a*c
        if a>0:
            if delta <= 0:
                print("Bat phuong trinh vo nghiem")
                return
            else:   
                x1 = (-b - math.sqrt(delta))/(2*a)
                x2 = (-b + math.sqrt(delta))/(2*a)
                print("Khoang nghiem cua bat phuong trinh la: (",x1,",",x2,")")
                return
        elif a<0:
            if delta < 0:
                print("(-vc; +vc)")
                return
            elif delta == 0:
                x = -b/(2*a)
                print("Khoang nghiem cua bat phuong trinh la: (-vc; ",x,") U (",x," ;vc)")
                return
            else :
                x1 = (-b + math.sqrt(delta))/(2*a)
                x2 = (-b - math.sqrt(delta))/(2*a)
                print("Khoang nghiem cua bat phuong trinh la: (-vc; ",x1,") U (",x2," ;vc)")
                return

def solution_equation_less_or_equal0(a, b, c):       
    if a == 0 or b == 0:
        print("Nhap lai a va b khac 0")
        return
    else:
        delta = b*b - 4*a*c
        if a>0:
            if delta < 0:
                print("Bat phuong trinh vo nghiem")
                return
            elif delta == 0:
                x = -b/(2*a)
                print("Nghiem cua bat phuong trinh la: ",x)
                return
            else:   
                x1 = (-b - math.sqrt(delta))/(2*a)
                x2 = (-b + math.sqrt(delta))/(2*a)
                print("Doan nghiem cua bat phuong trinh la: [",x1,",",x2,"]")
                return
        elif a<0:
            if delta < 0:
                print("(-vc; +vc)")
                return
            else :
                x1 = (-b + math.sqrt(delta))/(2*a)
                x2 = (-b - math.sqrt(delta))/(2*a)
                print("Doan nghiem cua bat phuong trinh la: [-vc; ",x1,"] U [",x2," ;vc]")
                return
            
def solution_equation_greater0(a, b, c):
    if a == 0 or b == 0:
        print("Nhap lai a va b khac khong")
        return 
    else:
        delta = b*b - 4*a*c
        if a>0:
            if delta < 0:
                print("(-vc; +vc)")
                return
            elif delta == 0:
                x = -b/(2*a)
                print("Khoang nghiem cua bat phuong trinh la: (-vc;",x,") U (",x,";vc)")
                return
            else:   
                x1 = (-b - math.sqrt(delta))/(2*a)
                x2 = (-b + math.sqrt(delta))/(2*a)
                print("Khoang nghiem cua bat phuong trinh la: (-vc;",x1,") U (",x2,";vc)")
                return
        elif a<0:
            if delta <= 0:
                print("Bat phuong trinh vo nghiem")
                return
            else :
                x1 = (-b + math.sqrt(delta))/(2*a)
                x2 = (-b - math.sqrt(delta))/(2*a)
                print("Khoang nghiem cua bat phuong trinh la: (",x1,",",x2,")")
                return

def solution_equation_greater_or_equal0(a, b, c):
    if a == 0 or b == 0:
        print("Nhap lai a va b khac khong")
        return
    else:
        delta = b*b - 4*a*c
        if a>0:
            if delta <= 0:
                print("(-vc; +vc)")
                return
            else:   
                x1 = (-b - math.sqrt(delta))/(2*a)
                x2 = (-b + math.sqrt(delta))/(2*a)
                print("Doan nghiem cua bat phuong trinh la: [-vc; ",x1,"] U [",x2," ;vc]")
                return
        elif a<0:
            if delta < 0:
                print("Bat phuong trinh vo nghiem")
                return
            elif delta == 0:
                x = -b/(2*a)
                print("Nghiem cua bat phuong trinh la: ",x)
                return
            else :
                x1 = (-b + math.sqrt(delta))/(2*a)
                x2 = (-b - math.sqrt(delta))/(2*a)
                print("Doan nghiem cua bat phuong trinh la: [",x1,",",x2,"]")
                return

def menu():
    print("ham so co dang la: ",a,"x^2 + ",b,"x + ",c)
    choice = int(input(f"Chọn bất phương trình: \n1: {a}x^2 + {b}x + {c} <= 0\n2: {a}x^2 + {b}x + {c} < 0\n3: {a}x^2 + {b}x + {c} > 0\n4: {a}x^2 + {b}x + {c} >= 0\nLựa chọn của bạn: "))
    if choice == 1:
        print(f"Bất phương trình đã chọn: {a}x^2 + {b}x + {c} <= 0")
        solution_equation_less_or_equal0(a, b, c)
    elif choice == 2:
        print(f"Bất phương trình đã chọn: {a}x^2 + {b}x + {c} < 0")
        solution_equation_less0(a, b, c)
    elif choice == 3:
        print(f"Bất phương trình đã chọn: {a}x^2 + {b}x + {c} > 0")
        solution_equation_greater0(a, b, c)
    elif choice == 4:
        print(f"Bất phương trình đã chọn: {a}x^2 + {b}x + {c} >= 0")
        solution_equation_greater_or_equal0(a, b, c)
    else:
        print("Lựa chọn không hợp lệ.")

menu()