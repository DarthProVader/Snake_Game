from random import randint

def rady(pole):
    #funkce na převedení seznamů na string
    pole2 = []
    for seznam in pole:
        pole2.append(" ".join(seznam))
    return print("\n".join(pole2))

def nakresli_mapu(seznam):
    #přidá "X" na místo stanovené v seznamu
    for el in range(len(seznam)):
        hraci_pole[seznam[el][0]][seznam[el][1]] = "X"
    rady(hraci_pole)

def del_souradnice():
    hraci_pole[souradnice[0][0]][souradnice[0][1]] = "."
    del souradnice[0]

def pohyb(seznam, kompas):
    #dostane souřadnice a světovou stranu, podle nich přidá souřadnici a odmaže poslední
    #pokud je již další souřadnice v seznamu vyhodí error, stejně tak pokud to bude záporné číslo = mimo mapu
    if kompas == "v":
        vychod = (seznam[-1][0], seznam[-1][1] + 1) #proměnná na další políčko doprava
        if vychod not in seznam and vychod[1] >= 0:
            souradnice.append((seznam[-1][0], seznam[-1][1] + 1)) #pokud není v souřadnicích a není mimo mapu -> přidá se do souradnice
            try:
                if hraci_pole[vychod[0]][vychod[1]] != "?": #pokud je na políčku potrava prodlouží se
                    del_souradnice()
            except IndexError:
                pass
        else:
            raise ValueError
    elif kompas == "j":
        jih = (seznam[-1][0] + 1, seznam[-1][1]) #proměnná na další políčko dolu
        if jih not in seznam and jih[1] >= 0:
            souradnice.append((seznam[-1][0] + 1, seznam[-1][1]))
            try:
                if hraci_pole[jih[0]][jih[1]] != "?":
                    del_souradnice()
            except IndexError:
                pass
        else:
            raise ValueError
    elif kompas == "s": 
        sever = (seznam[-1][0] - 1, seznam[-1][1]) #proměnná na další políčko nahoru
        if sever not in seznam and sever[0] >= 0:
            souradnice.append((seznam[-1][0] - 1, seznam[-1][1]))
            try:
                if hraci_pole[sever[0]][sever[1]] != "?":
                    del_souradnice()
            except IndexError:
                pass
        else:
            raise ValueError
    elif kompas == "z":
        zapad = (seznam[-1][0] , seznam[-1][1] - 1) #proměnná na další políčko doleva
        if zapad not in seznam and zapad[1] >= 0:
            souradnice.append((seznam[-1][0] , seznam[-1][1] - 1))
            try:
                if hraci_pole[zapad[0]][zapad[1]] != "?":
                    del_souradnice()
            except IndexError:
                pass
        else:
            raise ValueError

souradnice = [(0, 0), (1, 0), (2, 0)] #had
hraci_pole = [['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],]
hraci_pole[randint(3, 10)][randint(0, 10)] = "?" #hadí potrava

while True:
    smer = "p"
    while smer not in ["s", "v", "j", "z"]:
        smer = input("Kam pojedem?('s'= sever, 'j'= jih, 'v'= východ, 'z'= západ): ")
    try:
        pohyb(souradnice, smer)
    except ValueError:
        #funguje u severu a západu
        print("Game Over")
        break
    try:
        nakresli_mapu(souradnice)
    except IndexError:
        #z nějakého důvodu jih a východ vyhodí IndexError u této funkce, ale funkčnost se tím nemění, proto jsem to ošetřil takto
        print("Game Over")
        break
