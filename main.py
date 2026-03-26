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





#3-Misol
Kitoblar = {
    "matematika": 5,
    "ona tili": 6,
    "tarix": 4,
    "fizika": 0,
}
def ruyhat():
    for nomi, soni in Kitoblar.items():
        print(nomi, soni, "ta")
def qidirish1(qidirish):
    if qidirish in Kitoblar:
        if Kitoblar[qidirish] > 0:
            print(f"Topildi: {qidirish} — {Kitoblar[qidirish]} ta bor")
        else:
            print("Hozir mavjud emas")
    else:
        print("Topilmadi")

while True:
  print("___________________")
  print("1.Kitoblar ro'yhati")
  print("2.Kitob qidirish")
  print("3.Chiqish")
  tanlash = int(input())
  if tanlash == 1:
    ruyhat()
  elif tanlash == 2:
    n = input("Kitob nomini kiriting: ").lower()
    qidirish1(n)
  elif tanlash == 3:
    break
  else:
    print("Xatolik")





#6-Misol
sonlar = []

for i in range(10):
  son = int(input("Son kiriting: "))
  sonlar.append(son)

kvadrat = list(map(lambda x: x*x, sonlar))
juft_sonlar = list(filter(lambda x: x % 2 == 0, sonlar))
musbat_sonlar = list(filter(lambda x: x > 0, sonlar))
katta50 = list(filter(lambda x: x > 50, sonlar))
juft_kvadrat=(list(map(lambda x: x*x, juft_sonlar)))

print(kvadrat)
print(juft_sonlar)
print(musbat_sonlar)
print(katta50)
print(juft_kvadrat)




#8-Misol
maxsulotlar = ["sumka", "telefon", "kitob", "noutbuk"]
narxlar = [50000, 3000000, 15000, 8000000]
data = list(zip(maxsulotlar, narxlar))

def qimmat(data):
    return list(filter(lambda x: x[1] > 20000, data))


def chegirma(narxlar):
    return list(map(lambda x: x * 0.9, narxlar))


def eng_qimmat_narx(data):
    return max(data, key=lambda x: x[1]) #AI

print("Qimmat mahsulotlar:", qimmat(data))
print("Chegirmali narxlar:", chegirma(narxlar))
print("Eng qimmat:", eng_qimmat_narx(data))



#10-Misol
names = ["Ali", "Vali", "Aziz", "Lola"]
math = [80, 60, 90, 40]
english = [70, 75, 85, 50]

def urtachasi(names, math, english):
    urtacha = list(map(lambda x, y: (x + y) / 2, math, english))
    data = list(zip(names, urtacha))
    return data

def otgan_talabalar(data):
    return list(filter(lambda x: x[1] > 70, data))

def max_ball(data):
    return max(data, key=lambda x: x[1])

def info(data):
    for student in data:
        print(student[0], "average:", student[1])

data = urtachasi(names, math, english)
info(data)
print("Passed: ", otgan_talabalar(data))
print("Top: ", max_ball(data))
  



    

    
