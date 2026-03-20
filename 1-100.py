import random
def spiel_starten():
    geheimzahl = random.randint(1, 100)
    versuche = 0

    print("--- WILKOMMEN BEIM ZAHLENRATESPIEL! ---")
    print("Ich habe mir eine Zahl zwischen 1 und 100 ausgedacht. Rate mal!")

    while True:
        try:
            tipp = int(input("Dein Tipp: "))
            versuche += 1

            if tipp < geheimzahl:
                print("Falsch! Meine Zahl ist GRÖSSER.")

            elif tipp > geheimzahl:
                print("Falsch! Meine Zahl ist KLEINER.")
            else:
                print(f"HERZLICHEN GLÜCKWUNSCH! Du hast die Zahl in {versuche} Versuchen erraten.")
                break
        except ValueError:
            print("Fehler: Bitte gib eine gültige ganze Zahl ein!")

if __name__ == "__main__":
    spiel_starten()