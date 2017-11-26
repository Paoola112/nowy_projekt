def wypisz_osobe (imie,nazwisko):
    print ("{0} {1}".format (imie,nazwisko))

def czy_emeryt(wiek):
    MAX = 65
    if wiek < MAX:
        return True
    else:
        return False

if __name__ == "__main__":
    imie = 'Paulina'
    nazwisko = 'W'
    wiek = 30
    print (nazwisko)

    wypisz_osobe (imie,nazwisko)
    if czy_emeryt(wiek):
        print('nie emeryt')
    else:
        print('emeryt')
