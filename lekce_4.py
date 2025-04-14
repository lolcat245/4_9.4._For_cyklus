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
# samohlasky = 'aeiouáéíóú'
# souhlasky = 'bcčdďfghjklmnňprřsštťvzžcdž'
# vysledky = {'souhlasky': 0, 'samohlasky': 0}
# veta = 'Zvuk řeči je produkován otevřenou konfigurací vokálního traktu'
# for znak in veta.lower():
#     if znak.isalpha():
#         if samohlasky.find(znak) != -1:
#             vysledky['samohlasky'] += 1
#             #print(znak, vysledky)
#         else:
#             vysledky['souhlasky'] += 1
#             #print(znak, vysledky)
#     #else:
#         #print(f"Znak je \'{znak}\'")
# print(f"Počet souhlásek: {vysledky['souhlasky']} | Počet samohlásek: {vysledky['samohlasky']}")

# cviceni: seznam zamestnancu a for smycka
zamestnanci_raw = """
Helena Vybíralová
Wendy Štrumlová
Marie Vybíralová
Stanislav Bechyňka
Zdeňka Urbánková
Lukáš Riečan
Veronika Koudelová
Františka Vorlová
Ilie Seleš
Martin Železný
Petra Niklesová
Bohumil Skok
Jakub Šmíd
Jarmila Procházková
Dagmar Hlavatá
Jiří Nguyen Thanh
Marie Franková
Dana Ulrichová
Jana Hranická
Hana Budošová
Ivan Široký
Květoslava Jiráčková
Pavel Przywara
Josef Umlauf
Tomáš Granzer
Miroslav Kuba
Miloslava Adámková
Marie Karlíková
Jaroslav Hronský
Vlasta Karlíková
Andrea Žatková
Zuzana Lokočová
Ondřej Ptáček
Zdeněk Najman
Tereza Šebešová
Antonie Skokánková
Jan Lion
Václav Vecko
František Vajgl
Adéla Kavková
Amália Vacková
Anna Pažická
Ivo Pustějovský
Antonín Pavela
Jitka Adamová
Libuše Hamroziová
Drahomíra Balzerová
Marek Suchánek
Petr Vavrinec
Jonáš Stuchlý
Jaromír Pecen
Markéta Kyliánková
Marina Pečenková
Ivana Perdochová
Michaela Drápalová
Michael Mentlík
Rudolf Špičák
Žaneta Holá
Blanka Lišková
Eva Svatoňová
Rostislav Hoang
Martina Kalivodová
Milan Hruška
Zdenka Marková
Lenka Schambergerová
Růžena Martinů
Věra Řezanková
Marie Pečenková
Miloš Váchal
Jaroslava Hrubá
Petr Pecen
Pavla Konvicová
Lucie Marešová
Květuše Zdráhalová
Vlastimila Svatošová
Zora Michalčíková
Daniel Švejnoha
Klára Brunclíková
Vladimír Bauer
Michal Slaný
Jiřina Novosadová
Karel Sršeň
Stanislava Lakosilová
Filip Černý
Alena Kubiková
Sára Kotrlová
Alois Rejlek
Božena Novotná
Maryana Nováková
Kateřina Máslová
Ladislav Dvořák
Radek Varga
Petr Dvořák
Ludmila Jaklová
Renáta Foubíková
Nikola Lehká
Dominika Riegerová
Patrik Polák
Soňa Štrbová
David Matoušek
Liubov Hollíková
Monika Poláková
Marie Jaklová
Aleš Svoboda
Roman Kolínský
Karolína Košiková
"""

zamestnanci = zamestnanci_raw.splitlines() # misto .split('\n')
dict1 = dict() # hlavni slovnik
dict2 = dict() # vnoreny slovnik

for zamestnanec in zamestnanci: # zamestnanec je promenna typu str v listu 
    if zamestnanec: # podivam se jestli zamestnanec je True a nemusim resit prazdne hodnoty ''
        jmeno_oddelene = zamestnanec.split(' ') # vytvorim ze stringu list se dvema polozkami
        dict2['mail'] = f'{zamestnanec[0]}.{jmeno_oddelene[1]}@firma.cz'.lower()
        dict2['jmeno'] = f'{jmeno_oddelene[0]}'
        dict2['prijmeni'] = f'{jmeno_oddelene[1]}'# vytvoren vnoreny slovnik, polozim ho do hlavniho slovniku
        dict1[f'{zamestnanec}'] = f'{dict2}'
print(dict1)