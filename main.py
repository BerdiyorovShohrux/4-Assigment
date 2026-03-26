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









#2-Misol
balans = 50000
pin = 1103
xatolik = 0

def view():
    global balans
    return f"Sizning balansingiz {balans}so'm"


def yechamiz():
    global balans
    return f"Sizning balansingiz {balans-yechish} so'm"


def jonat():
    global balans
    return f"Sizning balansingiz {balans - summa} so'm"



def yangi_pin():
    global pin
    return pin == yangi_pin


print("Salom Pinkodni kiriting")
pinkod = int(input(''))

while True:
    if pinkod == pin:
        print("1.Balans \n2. Pul yechish \n3.Pul jo'natish \n4.Pinkodni almashtirish \n5.Chiqish")
        tanlash = int(input())
        if tanlash == 1:
            print(view())
        elif tanlash == 2:
            print("Qancha pul yechasiz")
            yechish = int(input())
            if yechish <= balans and 0<yechish:
                print(yechamiz())
        elif tanlash == 3:
            print("Qancha pul jo'natasiz")
            summa = int(input())
            if summa <= balans and 0<summa:
                print(jonat())
        elif tanlash == 4:
            print("Yangi pinkodni kiriting")
            yangi_pin = int(input())
        elif tanlash == 5:
            break 
#Bu misolni ishlagandim qo'shilgan narsalar -->>  xatolikni aniqlash va summa yechish va jo'natishdagi miqdori 0dan va asosiy balansdan kichik yoki kattaligini tekshirib funksiya ishlashini davom ettirish
        else:
            xatolik += 1

        if xatolik == 3:
            print("Dastur to'xtadi, chunki bir nechta noto'g'ri tanlov qildingiz")
            break
    else:
        xatolik += 1
        print("Pinkodni kiriting")
        continue




#4-Misol

ism = []
ball = []
for i in range(5):
    name = input(f"{i+1}.Ism: ")
    score = int(input(f"{i+1}.Ball: "))
    ism.append(name)
    ball.append(score)
  

def ball_darajasi(ball):
    if ball >= 90:
        return "A"
    elif ball >= 70:
        return "B"
    elif ball >= 60:
        return "C"
    else:
        return "F"

#
def ismi_bali(ism, ball): #AI
    for i in range(len(ism)): #AI
        grade = ball_darajasi(ball[i]) #AI
        print(ism[i], ball[i], grade) #AI
#

def top_student(names, scores):
    max_ball = max(scores)
    belgilash = scores.index(max_ball) #AI
    return names[belgilash] #AI
ismi_bali(ism, ball)
print("Top student:", top_student(ism, ball))

    

    
