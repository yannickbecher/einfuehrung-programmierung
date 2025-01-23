from random import randint

def spiel() -> None:
    gedacht: int = randint(1, 10)
    versuche: int = 0
    print("Errate die Zahl zwischen 1 und 10!")

    while True:
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

        versuche += 1
        if geraten > gedacht:
            print("Nein, ist kleiner!")
        elif geraten < gedacht:
            print("Nein, ist größer!")
        else:
            break

    print(f"Genau! Du hast {versuche} Versuch(e) benötigt.")

if __name__ == "__main__":
    spiel()