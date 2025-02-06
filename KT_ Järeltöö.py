# import requests

# url = "https://dummy-json.mock.beeceptor.com/users"

# username = input("Sisesta kasutajanimi: ")

# response = requests.get(url)

# if response.status_code == 200:

#     users = response.json()

#     for user in users:

#         if user['username'].lower() == username.lower():

#             print("Kasutaja leitud:", user)

#             break
#     else:

#         print("Kasutajat ei leitud.")
# else:

#     print("Viga andmete allalaadimisel:", response.status_code)


import requests

url = "https://dummy-json.mock.beeceptor.com/users"

username = input("Sisesta nimi või osa nimest, mida otsida: ")

response = requests.get(url)

if response.status_code == 200:

    users = response.json()

    found = False  

    for user in users:

        if username.lower() in user['username'].lower():

            print("Leitud kasutaja:", user)

            found = True
            
    if not found:

        print("Ühtegi vastust ei leitud.")
else:
    print("Andmete sisestusel tekkis viga:", response.status_code)

