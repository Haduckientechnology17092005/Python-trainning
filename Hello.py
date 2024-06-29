sum_math = float(input("Nhap diem trung binh mon toan: "))
sum_physics = float(input("Nhap diem trung binh mon ly: "))
sum_chemistry = float(input("Nhap diem trung binh mon hoa: "))
sum = sum_math + sum_physics + sum_chemistry
tb =  sum/3
print("Tong diem: ", sum)
print("Diem trung binh: ", round(tb, 1))
if tb <=2.5:
    print("Kem")
elif (tb>2.5) and (tb<5.0):
    print("Yeu")
elif (tb>=5.0) and (tb<6.5):
    print("Trung binh")
elif (tb>=6.5) and (tb<8.0):
    print("Kha")
elif (tb>=8.0) and (tb<9.0):
    print("Gioi")
else:
    print("Xuat sac")

