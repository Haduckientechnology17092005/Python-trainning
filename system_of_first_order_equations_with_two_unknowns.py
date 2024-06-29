print("Giai he phuong trinh bac nhat 2 an")
print("ax + by = m")
print("cx + dy = n")
a = float(input("Enter a: "))
b = float(input("Enter b: "))
c = float(input("Enter c: "))
d = float(input("Enter d: "))
m = float(input("Enter m: "))
n = float(input("Enter n: "))
def solution_equation(a, b, c, d, m, n):
    det1 = a * d - b * c
    det2 = m * d - n * c
    det3 = a * n - m * c

    if det1 == 0:
        if det2 == 0 and det3 == 0:
            print("Phương trình có vô số nghiệm")
        else:
            print("Phương trình vô nghiệm")
    else:
        x = det2 / det1
        y = det3 / det1
        print(f"Phương trình có nghiệm duy nhất: x = {x}, y = {y}")

solution_equation(a, b, c, d, m, n)