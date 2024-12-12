# Harjutus 16
# Darion Pukk
# 20.11.24

import os
import datetime

# Skript tervitab kasutajat tema operatsioonisüsteemi sisselogimisnime alusel

nimi = os.getlogin()
print(f"Tere {nimi}!")

# Skript kuvab kasutajale praeguse töökataloogi tee

print(f"Sa oled: {os.getcwd()}")

# Kataloogide loomine:
# Skript küsib kasutajalt, mitu kataloogi ta soovib luua
# Kataloogid luuakse praegusesse töökataloogi kuupäevaga märgistatud kataloogi sees, nummerdatuna (nt “1”, “2”)

kokku = 3
print(datetime.datetime.now())
try:
    for i in range(kokku):
    os.mkdir(str(i+1))
except:
    print("Sul on juba need kataloogid!")


# Kataloogi kustutamine:
# Pärast kataloogide loomist küsib skript kasutajalt, millist äsja loodud või olemasolevat kataloogi soovitakse kustutada, esitades kataloogi nime 1, 2 jne
# Kui sisestatud kataloogi nimi eksisteerib, kustutatakse see
# Kuva kuupäeva kasutas olevad kataloogid