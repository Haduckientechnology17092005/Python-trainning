year = int(input("Enter year: "))
def check_year(year):
    if year%400==0 or (year%4==0 and year%100!=0):
        print("Leap year")
    else:
        print("Not leap year")

check_year(year)