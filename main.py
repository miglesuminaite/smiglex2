


kintamasis = 1
kintamasis2 = 2

def funkcija ():
    print(kintamasis)
    print(kintamasis2)
    print(f'test:{kintamasis2}{kintamasis}')
    print('test:{}{}'.format(kintamasis2, kintamasis))

    #Komentaras 

    def sudetis(pirmas,antras):
        return pirmas+antras
    
    def atimtis(pirmas,antras):
        return pirmas-antras

    def daugyba(pirmas,antras):
        return pirmas*antras

    def dalyba(pirmas,antras):
        return pirmas/antras

    print("Pasirinkite norima veiksma:")
    print("[1] Sudetis")
    print("[1] Atimtis")
    print("[1] Daugyba")
    print("[1] Dalyba")