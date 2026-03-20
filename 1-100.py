import random

def spiel_starten():
    # ГАДНА ТАЛЫН ДАВТАЛТ: Тоглоомыг бүхэлд нь хариуцна
    while True:
        geheimzahl = random.randint(1, 100)
        versuche = 0
        
        print("\n--- WILLKOMMEN BEIM ZAHLENRATESPIEL! ---")
        print("Ich habe mir eine Zahl zwischen 1 und 100 ausgedacht.")

        # ДОТОР ТАЛЫН ДАВТАЛТ: Нэг тоог таах үйл явц
        while True:
            try:
                tipp = int(input("Dein Tipp: "))
                versuche += 1

                if tipp < geheimzahl:
                    print("Falsch! Meine Zahl ist GRÖSSER.")
                elif tipp > geheimzahl:
                    print("Falsch! Meine Zahl ist KLEINER.")
                else:
                    print(f"HERZLICHEN GLÜCKWUNSCH! Versuche: {versuche}")
                    break # Зөв таасан тул ДОТОР талын давталтаас гарна
            except ValueError:
                print("Fehler: Bitte gib eine gültige Zahl ein!")

        # Таасны дараа асуух хэсэг (Гадна талын давталт дотор байгааг анхаарна уу)
        nochmal = input("Möchtest du noch einmal spielen? (ja/nein): ").lower()
        if nochmal != "ja":
            print("Danke fürs Spielen! Auf Wiedersehen.")
            break # 'ja' биш бол ГАДНА талын давталтаас гарч программ зогсоно

if __name__ == "__main__":
    spiel_starten()