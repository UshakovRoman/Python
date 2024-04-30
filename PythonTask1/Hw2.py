n = int(input("Введите число:"))
mas=[]
for n in range(-n,n+1):
    mas.append(n)
    n=list()
    sum1=sum2=0
print(mas)
t=0

while t < len(mas):
    if mas[t] < 0:
        sum1 += mas[t]
    else:
        sum2 += mas[t]
    t += 1
  
print ("Сумма отрицательных чисел:",sum1)
print ("Сумма положительных чисел:",sum2)        


