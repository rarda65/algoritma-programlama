rastgelesayilist=[]
kucuktenbuyuge=[]
import random
index=0
index2=0
mahmut=0
sayitoplami=0
while mahmut<100:
  rastgelesayilist.append(random.randrange(0,200))
  sayitoplami+=rastgelesayilist[mahmut]
  mahmut+=1
buyuksayi=0
kucuksayi=200
while index<100:
  if buyuksayi<rastgelesayilist[index]:
    buyuksayi=rastgelesayilist[index]
  index+=1  
while index2<100:
  if kucuksayi>rastgelesayilist[index2]:
    kucuksayi=rastgelesayilist[index2]
  index2+=1  
sayiortalamasi=sayitoplami/len(rastgelesayilist)
index3=0
fark=0
mahmut2=0
while index3<100:
  fark=sayiortalamasi-rastgelesayilist[index3]
  fark**=2
  mahmut2+=fark
  index3+=1
a=mahmut2/100
b=a**0.5
print("rasgele sayı listesi")
print(rastgelesayilist)
print("sayı toplamı")
print(sayitoplami)
print("sayı ortalaması")
print(sayiortalamasi)
print("en büyük sayı")
print(buyuksayi)
print("en küçük sayı")
print(kucuksayi)
print("standart sapma")
print(b)
while len(rastgelesayilist)>0:
 kucuksayi=200
 mahmut3=0
 while mahmut3<len(rastgelesayilist):
  if kucuksayi>rastgelesayilist[mahmut3]:
   kucuksayi=rastgelesayilist[mahmut3]
  mahmut3+=1
 kucuktenbuyuge.append(kucuksayi)
 rastgelesayilist.remove(kucuksayi)
c=kucuktenbuyuge[49]+kucuktenbuyuge[50]
c/=2
print("küçükten büyüğe sıralaması")
print(kucuktenbuyuge)
print("medyanı")

print(c)
