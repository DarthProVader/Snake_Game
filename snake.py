def rady(pole):
    #funkce na převedení seznamů na string
    pole2 = []
    for seznam in pole:
        pole2.append("".join(seznam))
    return print("\n".join(pole2))

def nakresli_mapu(seznam):
    #přidá "X" na místo stanovené v seznamu
    hraci_pole = [['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],]
    for el in range(len(seznam)):
        hraci_pole[seznam[el][0]][seznam[el][1]] = "X"
    hraci_pole = rady(hraci_pole)
    return hraci_pole

def pohyb(seznam, kompas):
    #dostane souřadnice a světovou stranu, podle nich přidá "X" a odmaže poslední
    #pokud je již další souřadnice v seznamu vyhodí error, stejně tak pokud to bude záporné číslo = mimo mapu
    if kompas == "v":
        if (seznam[-1][0], seznam[-1][1] + 1) not in seznam and (seznam[-1][1] + 1) >= 0:
            souradnice.append((seznam[-1][0], seznam[-1][1] + 1))
        else:
            raise ValueError
    elif kompas == "j":
        if (seznam[-1][0] + 1, seznam[-1][1]) not in seznam and (seznam[-1][0] + 1)  >= 0:
            souradnice.append((seznam[-1][0] + 1, seznam[-1][1]))
        else:
            raise ValueError
    elif kompas == "s":
        if (seznam[-1][0] - 1, seznam[-1][1]) not in seznam and (seznam[-1][0] - 1) >= 0:
            souradnice.append((seznam[-1][0] - 1, seznam[-1][1]))
        else:
            raise ValueError
    elif kompas == "z":
        if (seznam[-1][0] , seznam[-1][1] - 1) not in seznam and (seznam[-1][1] - 1) >= 0:
            souradnice.append((seznam[-1][0] , seznam[-1][1] - 1))
        else:
            raise ValueError
    del souradnice[0]

souradnice = [(0, 0), (1, 0), (2, 0)]
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
