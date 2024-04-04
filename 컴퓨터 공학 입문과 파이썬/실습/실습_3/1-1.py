student = [["학생1",90],["학생2",80],["학생3",55],["학생4",61],["학생5",59]]
for [student_name, grade] in student:
    if grade >= 60:
        print(f"{student_name}은 합격입니다")
    else:
        print(f"{student_name}은 불합격입니다")