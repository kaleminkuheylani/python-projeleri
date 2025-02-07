import random

def sifre_kir(sifre):
   
    kirilmis_sifre=""
    count=0
    for i in sifre:
        while True:
            liste=["a","b","c","d","e","f","g","h",
                   "ı","i","j","k","l","m","n","o","p","r",
                   "s","t","u","v","y","z"]
            rnd=random.choice(liste)
            count+=1
            print(count)
            if i==rnd:
                kirilmis_sifre+=rnd    
                break
    with open("sifre.txt","w+") as dosya:
        dosya.write("sifre:"+kirilmis_sifre+" "+str(count))

sifre="emine"

sifre_kir(sifre)




    
