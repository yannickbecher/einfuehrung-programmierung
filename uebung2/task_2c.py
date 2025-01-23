from random import randint

def spiel() -> None:
    gedacht: int = randint(1, 10)
    versuche: int = 0
    max_versuche: int = 5
    letzter_versuche: int = 0

    print(f"Errate die Zahl zwischen 1 und 10! Du hast {max_versuche} Versuche.")

    while True and versuche < max_versuche:
        # Überprüfe, ob Input kein Int ist
        try:
            geraten: int = int(input("Dein Tipp: "))
        except ValueError:
            print("Gib eine Zahl zwischen 1 und 10 an!")
            continue

        # Zahlenbereich überprüfen
        if geraten not in range(1, 11):
            print("Die Zahl ist zwischen 1 und 10!")
            continue

        # Letzten Versuch vergleichen
        if geraten == letzter_versuche:
            print("Hattest du letztes mal schon!")
            continue

        if geraten > gedacht:
            print("Nein, ist kleiner!")
        elif geraten < gedacht:
            print("Nein, ist größer!")
        else:
            print(f"Genau! Du hast {versuche + 1} Versuch(e) benötigt.")
            break

        versuche += 1
        letzter_versuche = geraten
    else:
        print(f"Leider hast du alle Versuche ausgeschöpft. Die Zahl war {gedacht}.")

if __name__ == "__main__":
    spiel()