ClockH= 6
ClockM= 52
ClockS= 00
RunSlowS = 15
RunSlowM = 8
RunFastS = 12
RunFastM = 7
ClockM += RunSlowM*2 + RunFastM*3
ClockS += RunSlowS*2 + RunFastS*3
if ClockM >60:
    ClockH += 1
    ClockM -= 60
if ClockS >60:
    ClockM += 1
    ClockS -= 60
print("집에 도착 시간: ", ClockH, "시 ", ClockM, "분 ", ClockS, "초")
