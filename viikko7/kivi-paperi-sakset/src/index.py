from luo_peli import luo_peli, PELITYYPIT


def main():
    while True:
        print(
            "Valitse pelataanko"
            "\n (a) Ihmistä vastaan"
            "\n (b) Tekoälyä vastaan"
            "\n (c) Parannettua tekoälyä vastaan"
            "\nMuilla valinnoilla lopetetaan"
        )

        vastaus = input()
        if vastaus not in PELITYYPIT.keys():
            break
        print(
            "Peli loppuu kun pelaaja antaa virheellisen siirron eli jonkun"
            "muun kuin k, p tai s"
        )
        peli = luo_peli(vastaus)
        peli.pelaa()


if __name__ == "__main__":
    main()
