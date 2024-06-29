thunhap = float(input("nhap thunhap: "))
if thunhap <= 6000000:
    thue = 0
elif (thunhap > 6000000) and (thunhap < 9000000):
    thue = 0.02*thunhap
elif (thunhap >= 9000000) and (thunhap < 12000000):
    thue = 0.05*thunhap
elif (thunhap >= 12000000) and (thunhap < 21000000):
    thue = 0.07*thunhap
elif (thunhap >= 21000000) and (thunhap < 38400000):
    thue = 0.1*thunhap
elif (thunhap >= 38400000) and (thunhap < 62400000):
    thue = 0.15*thunhap
else:
    thue = 0.2*thunhap
print("Ban phai dong thue thu nhap: ",thue)