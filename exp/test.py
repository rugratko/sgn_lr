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