registeration_num = "920825-1185642"
seperated_register_num = registeration_num.split("-")
state = "unidentified"
yy=0
mm=0
dd=0
birthd=int(seperated_register_num[0])
private=int(seperated_register_num[1])
dd = birthd % 100
birthd //= 100
mm = birthd % 100
birthd //= 100
yy = birthd
if private // 1000000 <= 2:
    state = "before 2000"
else:
    state = "after 2000"
day=str(dd)
month=str(mm)
year=str(yy)
if mm <10:
    month= "0"+month
if state == "before 2000":
    year= "19" + year
    print("주민번호 연월일 :", year+month+day)
    print("주민번호 뒷번호 :", private)
else:
    year= "20" + year
    print("주민번호 연월일 :", year+month+day)
    print("주민번호 뒷번호 :", private)

