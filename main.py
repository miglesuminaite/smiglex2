from flask import Flask, request
app = Flask(__name__)


def sudetis(pirmas,antras):
        return pirmas+antras

def atimtis(pirmas,antras):
        return pirmas-antras

def daugyba(pirmas,antras):
        return pirmas*antras

def dalyba(pirmas,antras):
        if antras !=0:
            return pirmas/antras
        else:
             return "Dalyba is nulio negalima."

@app.route("/") # Route 1
def hello_world():

    return "Labas" """
                <form action="/skaicius">
                    <label for="test">skaicius 1</label><br>
                        <input type="text" id="test" name="test" value="0"><br>
                        </br></br>

                    <label for="test2">skaicius 2</label><br>
                        <input type="text" id="test2" name="test2" value="0"><br><br>
                        </br></br>
                        
                    <input type="submit" value="Submit">
                </form> 
            """

@app.route("/labas")  # Route 2
def sakyk_labas():
    global skaicius ## Naudoju globalu kintamaji
    skaicius = skaicius +1 ## kaskart atidare pridedam 1
    return f"Labas {skaicius}"


    '''
        /skaicius?test=100
        /skaicius?test=0  &  test2=0
    '''

@app.route("/skaicius") # Route 3
def skaiciavimo():
    if not request.args.get("test") or not request.args.get("test2"):
         return "Nera argumento."
    skaicius = request.args.get("test") ### Pasiimam argumenta is URL pvz.: /skaicius?test=100
    skaicius2 = request.args.get("test2") ### Pasiimam argumenta 2 is URL pvz.: /skaicius?test2=100

    suma = sudetis(int(skaicius2),int(skaicius))

    return f"Gauta suma: {suma}"

if __name__ == "__main__":
    app.run()


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
            print(num1, "+", num2, "=", sudetis(num1, num2))

        elif choice == '2':
            print(num1, "-", num2, "=", atimtis(num1, num2))

        elif choice == '3':
            print(num1, "*", num2, "=", daugyba(num1, num2))

        elif choice == '4':
            print(num1, "/", num2, "=", dalyba(num1, num2))
        
        kitas_skaiciavimas = input("Skaiciuojam dar karta? (taip/ne): ")

        if kitas_skaiciavimas == "taip":
          continue
        else: break
    else:
        print("Blogai. Iveskite dar karta")
