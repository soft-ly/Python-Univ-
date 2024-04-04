a = int(input("정수하나 입력"))
b = int(input("정수하나 입력"))

if a<b:
    c=0
    d=b
    while a<d:
        d=d-a
        c+= 1
    print(f"{b}을(를) {a}(으)로 나눴을 때의 몫: {c}")
    print(f"{b}을(를) {a}(으)로 나눴을 때의 나머지: {d}")

elif b<a:
    c=0
    d=a
    while b<d:
        d=d-b
        c+= 1
    print(f"{a}을(를) {b}(으)로 나눴을 때의 몫: {c}")
    print(f"{a}을(를) {b}(으)로 나눴을 때의 나머지: {d}")
    