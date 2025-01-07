# Darion Pukk 07.01.2024

# # Harjutus 2

# sisend = input("Sisesta tekst: ")

# muudetud_sisend = sisend.replace(" ", "...")

# print("Muudetud tekst: ", muudetud_sisend)

# # Harjutus 8

# def aeg_und_eks(aeg):

#     tund, minut = map(int, aeg.split(":"))

#     return tund + minut / 60


# aeg = input("Sisesta aeg (24-tunnises formaadis, näiteks 7:30): ")

# aeg_f = aeg_und_eks(aeg)


# if 7 <= aeg_f <= 8:

#     print("On hommikusöögi aeg!")

# elif 12 <= aeg_f <= 13:

#     print("On lõunasöögi aeg!")

# elif 18 <= aeg_f <= 19:

#     print("On õhtusöögi aeg!")

# # Harjutus 9

# def coca_automaat():

#     hind = 50  # Coca-Cola hind sentides

#     summa = 0  # Alguses on raha null



#     while summa < hind:

#         munt = int(input("Sisesta münt (25, 10 või 5 senti): "))

        

#         if munt in [25, 10, 5]:

#             summa += munt

#             if summa < hind:

#                 print(f"Puudu on {hind - summa} senti.")

#         else:

#             print("Kehtetu münt, palun sisesta 25, 10 või 5 senti.")



#     print(f"Tagasimakse on {summa - hind} senti." if summa > hind else "Täpselt 50 senti, tagasimakset pole.")


# coca_automaat()
