#1-Misol
def get_grades():
    grades = []
    for i in range(8):
        grade = int(input(f"{i + 1} Ball kiriting: "))
        grades.append(grade)
    return grades
def maximal_ball(grades):
    return max(grades)
def minimal_ball(grades):
    return min(grades)
def ortacha_ball(grades):
    return sum(grades) / len(grades)
def yuqori60(grades):
    soni = 0
    for b in grades:
        if b >= 60:
            soni += 1
    return soni
def ortachadan_yuqori(grades, avg):
    soni1 = 0
    for g in grades:
        if g > avg:
            soni1 += 1
    return soni1
grades = get_grades()
ortacha = ortacha_ball(grades)
print("Maximal ball:", maximal_ball(grades))
print("Minimal ball:", minimal_ball(grades))
print("O'rtacha ball:", ortacha)
print("O'tgan ballar:", yuqori60(grades))
print("O'rtachadan yuqori:", ortachadan_yuqori(grades, ortacha))
