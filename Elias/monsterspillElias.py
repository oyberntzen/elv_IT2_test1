from ast import Str
from multiprocessing.sharedctypes import Value
import random 

print(random.randint(0,25))
class Monster:
    def __init__(self, navn:str, hp:int = 0, skade_per_slag_maks:int = 0, liv:bool=True):
        self.navn = navn
        self.hp=hp
        self.skade_per_slag_maks=skade_per_slag_maks
        self.liv= liv

        if self.hp<0:
            liv=False
            print("Du doede")
        
    def gjooreSkade(self, Spiller):
        skade = random.randint(0, self.skade_per_slag_maks)
        Spiller.hp-=skade
        print(f"{navn_spiller} Du ble truffet av monsteret")
        print(f"{navn_spiller} mistet {skade} hp, så spilleren har nå {spiller.hp} hp igjen!")

class Spiller:
    def __init__(self, navn:str, hp:int = 0, gjenstander:list = []):
        self.navn = navn
        self.hp = hp
        self.gjenstander = gjenstander
    def spillerPotionofhealing(self):
        self.hp*=2 
    def printEgenskap(self):
        tekst=""
        for i in self.gjenstander:
            tekst+=f"\nGjenstanden {i.navn} gjoer {i.skade}"
        print(tekst)

print("Velkommen til dette spillet")
print("Maalet med spillet er å komme deg gjennom et hus")
print("I huset kan du finne vaapen, gjenstander, og monster :o")
print("For å bevege deg skriver du enten inn opp, ned, hoeyre, venstre")
print("Dersom du kommer i et rom med en gjenstand kan du skrive 'grip' for å plukke det opp eller bruke det")
print("I rom med monster foelger egen instruks")
navn_spiller = "Roger"#input("\nFoer du begynner må du skrive inn navnet ditt: ")


class Vaapen():
    def __init__(self, navn, skade):
        self.navn=navn
        self.skade=skade

#setter startverdier for spiller
start_hp_spiller = 100
spiller = Spiller(navn_spiller, start_hp_spiller,[Vaapen("knyttneve", 20)])

#lager monstere
monster1 = Monster("Peder", 50, 40)


class Rom:
    def __init__ (self, romnummer):
        self.romnummer = romnummer

rom_liste = [[],[],[]]

tall=1
for i in range(3):
    rom_liste.append
    for j in range(3):
        rom = "rom"
        rom += str(tall)
        rom = Rom(tall)
        rom_liste[i].append(rom)
        tall+=1

"""
#romplassering
    |  [2][0] nr=7 |  [2][1] nr=8 |  [2][2] nr=9 |
    |  [1][0] nr=4 |  [1][1] nr=5 |  [1][2] nr=6 |
    |  [0][0] nr=1 |  [0][1] nr=2 |  [0][2] nr=3 |  
"""

rom_liste[0][0].kiste=True
rom_liste[0][1].felle=True
rom_liste[0][2].gjenstand=Vaapen("sverd",40)
rom_liste[1][0].monster=monster1
rom_liste[1][1].gjenstand=Vaapen("tazer",50)
rom_liste[2][0].gjenstand = "potion of healing"
rom_liste[2][2].monster = True

naa_rom = rom_liste[1][0]


valg_muligheter=[]

rad_nr=0
kolonne_nr=0

def finnretning():
    mulige_retninger = f"{navn_spiller} kan bevege deg "
    global rad_nr, kolonne_nr
    for i in range(3):
        for j in range(3):
            if naa_rom == rom_liste[i][j]:
                rad_nr = i 
                kolonne_nr = j
                break
   
    if rad_nr == 0 or 1:
        mulige_retninger+="opp"
        valg_muligheter.append("opp")
        if kolonne_nr<2:
            mulige_retninger+=", til hoeyre"
            valg_muligheter.append("hoeyre")
        if kolonne_nr > 0:
            mulige_retninger+=" eller til venstre"
            valg_muligheter.append("venstre")
    print(mulige_retninger)
    
sant = True

def finnVariabel():
    liste=dir(naa_rom)
    for i in liste:
        if "_" not in i and i != "romnummer":
            verdi = i
            return verdi

def plukkOppGjenstand():
    if finnVariabel()=="gjenstand":
        spiller.gjenstander.append(naa_rom.gjenstand)
        print(f"{naa_rom.gjenstand.navn} er plukket opp")

def aapneKiste(): #fiks på den her
    return

def printVaapen():
    liste=[]            
    for i in spiller.gjenstander:
        liste.append(i.navn)
    return liste


def monsterKamp():
    print(f'Du har kommet i et rom med et monster med navnet {naa_rom.monster.navn}')
    print(f'Du kan velge å loope eller å sloss!')
    fightorflight = input("Ja eller nei?: ").lower().replace(" ", "")

    if fightorflight == "ja":
        while spiller.hp >=0 or naa_rom.monster.hp<=0:
            print("Kampen har begynt!")
            print(f"\nDu tar det foorste slaget!")
            printVaapen()
            

            if printVaapen()[-1] == "knyttneve": 
                print("Du har dessverre ingen vaapen så du maa klare deg med knyttnevene. Skriv 'knyttneve' for aa slaa")
            else:
                print(f"Du kan bruke {', '.join(printVaapen())}. Faar aa bruke gjenstanden skriver du bare inn navnet paa gjenstanden")
                spiller.printEgenskap()

            print(f"Monsteret har {naa_rom.monster.hp} hp og du har {spiller.hp} liv!")
            slaa_valg=input("Hva velger du?: ")
            

    else: 
        print("\nNeivel, kanskje en annen gang")



def kjoor():
    global naa_rom, rad_nr, kolonne_nr
    while sant==True:
        print(f"\n{navn_spiller} har kommet inn i rom nr {naa_rom.romnummer}")
        
        if finnVariabel()!=None:
            if finnVariabel()=="gjenstand":
                if naa_rom.gjenstand=="potion of healing":
                    print(f"Dette rommet har en/et {naa_rom.gjenstand}")
                    print("Dersom du drikker den har faar du doblet livet ditt")
                    print("For aa drikke den maa du skrive 'drikk'")
                    valg_muligheter.append("drikk")
                if naa_rom.gjenstand.navn == "tazer":
                    print(f"Dette rommet har en tazer, som gir 40 skade per treff")
                    print("For aa plukke den opp maa du skriv 'plukk opp'")
                    valg_muligheter.append("plukkopp")
                if naa_rom.gjenstand.navn == "sverd":
                    print(f"Dette rommet har et sverd, som gir 50 skade per treff")
                    print("For aa plukke det opp maa du skrive 'plukk opp'")   
                    valg_muligheter.append("plukkopp")
                    
            if finnVariabel()=="kiste":
                print(f"Dette rommet har en/et {finnVariabel()}")
                valg_muligheter.append("aapne")
                print("For aa aapne kisten skriver du inn aapne")
            if finnVariabel()=="felle":
                print(f"ooups, {navn_spiller} traakket i en felle og mistet halve livet")
                spiller.hp = spiller.hp/2
                print(f'{navn_spiller} har naa {spiller.hp} liv')
            if finnVariabel()=="monster":
                monsterKamp()

        else:
            print("Dette rommet har ingenting!")

        finnretning()

        valg = input(f"Hva vil {navn_spiller} gjøre: ").lower().replace(" ", "")
        
        if valg not in valg_muligheter:
            print("\nSkriv inn et gyldig alternativ")

            
        else:
            if valg == "opp":
                rad_nr +=1
            elif valg == "hoeyre":
                kolonne_nr +=1
            elif valg == "venstre":
                kolonne_nr -=1

            if valg == "plukkopp":
                plukkOppGjenstand()
                delattr(naa_rom, "gjenstand")
                valg_muligheter.remove("plukkopp")
            
            if valg == "aapne":
                aapneKiste()
                print("kisten er aapnet")
                delattr(naa_rom, "kiste")
                valg_muligheter.remove("aapne")

            if valg == "drikk":
                spiller.spillerPotionofhealing()
                print(f"{navn_spiller} har nå {spiller.hp} liv!")
                delattr(naa_rom, "gjenstand")
                valg_muligheter.remove("drikk")

        naa_rom=rom_liste[rad_nr][kolonne_nr]

kjoor()
