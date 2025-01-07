# Darion Pukk 18.12.2024 "8, 11, 7, 4, 2"

# Harjutus 2

# Vanuse loendi loomine
# vanused = []

# # Kasutaja sisestab vanuseid
# n = int(input("Sisesta, mitu vanust soovid sisestada: "))
# for i in range(n):
#     vanus =  int(input(f"Sisesta vanus (i + 1): "))
#     vanused.append(vanus)

# #Leiame suurima ja väikseima arvu
# suurim = max(vanused)
# vähim = min(vanused)

# # Arvutame kogusumma ja keskmise
# kogusumma = sum(vanused)
# keskmine = kogusumma / len(vanused)

# # Tulemuste vormistamine
# print("\nVanuste loend:", vanused)
# print("Suurim vanus:", suurim)
# print("Väikseim vanus:", vähim)
# print("Vanuste kogusumma:", kogusumma)
# print("Vanuste keskmine:", round(keskmine, 2))

# # Harjutus 8

# import random



# # Tervitus ja mängu selgitus

# print("Tere tulemast täringumängu!")

# print("Sina ja arvuti viskate mõlemad kaks täringut. Suurima punktisummaga võitja saab kogu laual oleva raha.")

# print("Teeme panuse!")



# # Kasutajalt küsitakse panust

# try:

#     panus = int(input("Sisesta oma panus (eurodes): "))

    

#     if panus <= 0:

#         print("Panus peab olema positiivne number. Alusta uuesti.")

#     else:

#         # Täringute viskamise funktsioon

#         def viska_täringut():

#             return random.randint(1, 6) + random.randint(1, 6)



#         # Kasutaja ja arvuti visked

#         kasutaja_tulemus = viska_täringut()

#         arvuti_tulemus = viska_täringut()



#         # Tulemuste kuvamine

#         print(f"Sinu tulemus kahe täringuga: {kasutaja_tulemus}")

#         print(f"Arvuti tulemus kahe täringuga: {arvuti_tulemus}")



#         # Võitja määramine

#         if kasutaja_tulemus > arvuti_tulemus:

#             print(f"Palju õnne! Sa võitsid {panus} eurot!")

#         elif kasutaja_tulemus < arvuti_tulemus:

#             print(f"Kahjuks sa kaotasid. Arvuti võitis sinu {panus} eurot.")

#         else:

#             print("Viik! Keegi ei kaotanud ega võitnud raha.")

# except ValueError:

#     print("Viga: palun sisesta kehtiv arv.")



#Harjutus 7



# Konstandid valuuta teisendamiseks

EUR_TO_EEK = 15.6466  # 1 EUR = 15.6466 EEK

EEK_TO_EUR = 1 / EUR_TO_EEK  # 1 EEK = ~0.064 EUR



# Tervitus ja kasutaja valiku küsimine

print("Tere tulemast eurokalkulaatorisse!")

print("Vali, mida soovid teha:")

print("1 - Teisenda EUR -> EEK")

print("2 - Teisenda EEK -> EUR")



try:

    # Kasutaja valik

    valik = int(input("Sisesta oma valik (1 või 2): "))



    if valik == 1:

        # EUR -> EEK teisendus

        eur = float(input("Sisesta eurode kogus: "))

        eek = eur * EUR_TO_EEK

        print(f"{eur:.2f} EUR on võrdne {eek:.2f} EEK-ga.")

    elif valik == 2:

        # EEK -> EUR teisendus

        eek = float(input("Sisesta kroonide kogus: "))

        eur = eek * EEK_TO_EUR

        print(f"{eek:.2f} EEK on võrdne {eur:.2f} EUR-ga.")

    else:

        # Vigase valiku korral

        print("Viga: vale valik. Palun vali 1 või 2.")

except ValueError:

    # Kui sisend ei ole number

    print("Viga: palun sisesta kehtiv arv.")



