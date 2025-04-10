# print("uiiauuuiiiai")
# print("silly")
# print("miau")

# cisla = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15)
# for cislo in cisla:
#     if cislo % 3 == 0 and cislo % 5 == 0:
#         print("FizzBuzz")
#     elif cislo % 3 == 0:
#         print("Fizz")
#     elif cislo % 5 == 0:
#         print("Buzz")
#     else:
#         print(cislo)

# content = [
#     ['jmeno;prijmeni;email;projekt', 'plat'],
#     ['Matous;Holinka;m.holinka@firma.cz;hr', '1000'],
#     ['Petr;Svetr;p.svetr@firma.cz;devops','2000']
# ]
# for item in content:
#     for subitem in item:
#         for subsubitem in subitem.split(";"):
#             print(subsubitem)

# a = ['a', 'b', 'c']
# print(*a)
# print(a[0], a[1], a[2])
# print('miau')

# cviceni: samohlasky a souhlasky
samohlasky = 'aeiouáéíóú'
souhlasky = 'bcčdďfghjklmnňprřsštťvzžcdž'
vysledky = {'souhlasky': 0, 'samohlasky': 0}
veta = 'Zvuk řeči je produkován otevřenou konfigurací vokálního traktu'
for znak in veta.lower():
    if znak.isalpha():
        if samohlasky.find(znak) != -1:
            vysledky['samohlasky'] += 1
            #print(znak, vysledky)
        else:
            vysledky['souhlasky'] += 1
            #print(znak, vysledky)
    #else:
        #print(f"Znak je \'{znak}\'")
print(f"Počet souhlásek: {vysledky['souhlasky']} | Počet samohlásek: {vysledky['samohlasky']}")