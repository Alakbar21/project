import random
import time

from pandas.core.roperator import rand_

print("""
Sayi tahmin oyunu3
1 ile 40 arasinda sayiyi tahmin edin 

""")
rastgele_sayi=random.randint(1,40)
tahmin_haqqi=7
while(True):
    tahmin=int(input("Tahmininiz:"))
    if(tahmin<rastgele_sayi):
        print("Bilgiler sorgulaniyor ......")
        time.sleep(1)
        print("Daha yuksek sayi girin.")
        tahmin_haqqi-=1
    elif(tahmin>rastgele_sayi):
        print("Bilgiler sorgulaniyor ......")
        time.sleep(1)
        print("Daha kucuk sayi girin.")
        tahmin_haqqi -= 1
    else:
        print("Bilgiler sorgulaniyor...")
        time.sleep(1)
        print("Tebrikler",rastgele_sayi)
        break
    if(tahmin_haqqi==0):
        print("Tahmin haqqiniz bitdi")
        print("Sayiniz",rastgele_sayi)
        break











