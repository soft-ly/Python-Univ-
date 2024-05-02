from pathlib import Path
scores_10m = []
with open(Path()/"diving_result.txt", 'r', encoding='utf-8') as f:
    for line in f:
        s_10m = line.split()[2]
        try:
            scores_10m.append(float(s_10m))
        except:
            continue
print(scores_10m)
