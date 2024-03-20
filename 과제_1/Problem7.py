names = [
    [95, "파이썬"], 
    [85, "이산수학"], 
    [35, "확률과 통계"], 
    [46, "일본어"],
    [87, "컴퓨팅적 사고"],
    [49, "인간과 철학"]
    ]
max_score = float('-inf')
max_sub = "N"
min_score = float('inf')
avg_score = 0
min_sub = "N"
for score, subject in names:
    if score > max_score:
        max_score = score
        max_sub = subject
    avg_score = avg_score + score
    if score < min_score:
        min_score = score
        min_sub = subject
avg_score = avg_score/len(names)

print("평균 점수 :", round(avg_score, 2), "\n", f"{max_sub},", max_score, "\n", f"{min_sub},", min_score)

