



# 3. faili allalaadimine
try
    failiSusurus = int(input("Siseta faili suurus (MB): "))
    downKiirus = int(input("Sisesta allalaadimise kiirus (MB/s): "))
    aeg = failiSusurus / downKiirus
print(f"Allalaadimiseks kulub{aeg:0:2f} sekundit")
except:
    print("Tegid sisestamisel vea!")







