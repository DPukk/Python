# Darion Pukk 29.11.24

# Sinu ülesandeks on kirjutada Pythoni skript, mis loeb andmeid failist pangakonto.txt. Fail sisaldab eraldi ridadel pangatehingute summasid: positiivsed summad tähistavad sissetulekuid ja negatiivsed summad väljaminekuid. Skript peab arvutama ja väljastama:
# kogu tehingute arvu
# positiivsete tehingute arvu
# positiivsete tehingute kogusumma
# Tulemused tuleb väljastada konsooli

"""
fail = open("pangakonto.txt")

loend = fail.readlines()
positiivsed = []
print(fail.readlines())

print(f"Tehinguid kokku {len(loend)}")


for i in loend:
    if float(i)>=0:
        positiivsed.append(float(i))
    
    
print(f"Tehinguid kokku {len(positiivsed)}")
print(f"Tehingute summa kokku {sum(positiivsed)}")

"""
fail = open("palgad.txt")
loend = fail.readlines()
print(loend)

for i in loend:
    
