print("Задание 1") 
money=int(input("Введите оклад: ")) 
procent=int(input("Введите процент: ")) 
print("Сумма на руки: ", money-money/100*procent) 
print("Сумма налога: ", money-money/100*(100-procent)) 

print("Задание 2") 
hours=int(input("Сколько часов спит ночью? ")) 
minutes=int(input("Сколько минут спит днем? ")) 
print("Тимофей спит", hours*60+minutes, "минут в сутки") 

print ("Задание 3") 
X=int(input("Время сна в минутах: ")) 
hours=X//60 
minutes=X-hours*60 
print("Должны завести будильник на", hours, "часов и", minutes, "минут.") 

print ("Задание 4") 
X=int(input("Введите время сна в минутах: ")) 
H=int(input("Катя ложится спать в _ часов ")) 
M=int(input("Катя ложится спать в _ минут? ")) 
hours=X//60 
minutes=X-hours*60 
minutes += M 
h2=minutes//60 
m2=minutes-h2*60 
h3=H+hours+h2 
print("Катя должна завести будильник на", h3, "часов и", m2, "минут.") 

print("Задание 5") 
a=float(input("Введите а: ")) 
b=float(input("Введите b: ")) 
l=float(input("Введитt l: ")) 

import math 
F=(2*(1-math.pi))/(b**2+l**2-1)*math.cos(0.5) 
print("F=", F, sep="")