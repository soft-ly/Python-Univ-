ansmonth=0
def IsYoon(x):
    if x % 4 ==0:
        if x % 100 == 0:
            if x % 400 != 0:
                return "YoonX"
            else:
                return "IsYoon"
        else:
            return "IsYoon"
    else:
        return "YoonX"
month31 = [1,3,5,7,8,10,12]
year = int(input("년도: "))
month = int(input("월: "))
for i in month31:
    if i == month:
        ansmonth=1
if ansmonth == 1:
    print("31")
elif IsYoon(year) == "IsYoon" and ansmonth == 0:
    if month == 2:
        print("29")
    else:
        print("30")
elif IsYoon(year) == "YoonX" and ansmonth == 0:
    if month == 2:
        print("28")
    else:
        print("30")