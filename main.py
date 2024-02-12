


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

while True:
    choice = input("Iveskite pasirinkima(1/2/3/4): ")

    if choice in ('1', '2', '3', '4'):
        try:
            num1 = float(input("Iveskite pirma skaiciu: "))
            num2 = float(input("Iveskite antra skaiciu: "))
        except ValueError:
            print("Blogai. Bandykite dar karta.")
            continue

        if choice == '1':
            print(num1, "+", num2, "=", add(num1, num2))

        elif choice == '2':
            print(num1, "-", num2, "=", subtract(num1, num2))

        elif choice == '3':
            print(num1, "*", num2, "=", multiply(num1, num2))

        elif choice == '4':
            print(num1, "/", num2, "=", divide(num1, num2))
        
        next_calculation = input("Skaiciuojam dar karta? (taip/ne): ")
        if next_calculation == "ne":
          break
    else:
        print("Error. Bandom dar karta.")
