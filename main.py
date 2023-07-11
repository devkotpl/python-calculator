from calculator import Calculator
from console import Console


def print_options(console: Console):
    console.writeLine('')
    console.writeLine("Dostępne opcje:")
    console.writeLine("1 - Dodawanie")
    console.writeLine("2 - Odejmowanie")
    console.writeLine("3 - Mnożenie")
    console.writeLine("4 - Dzielenie")
    console.writeLine("5 - Wyłącz")
    console.writeLine('')


shouldExit = False
console = Console()
calculator = Calculator()

console.writeLine("Pierwsze koty za płoty - Python - Kalkulator")

while not shouldExit:
    print_options(console)

    try:
        option = console.read_number_from_console("Wybierz opcję: ")

        if option == 5:
            shouldExit = True
            break

        a = console.read_number_from_console("Podaj liczbę: ")
        b = console.read_number_from_console("Podaj kolejną liczbę: ")
        result = 0
        if option == 1:
            result = calculator.add(a, b)
        elif option == 2:
            result = calculator.subtract(a, b)
        elif option == 3:
            result = calculator.multiply(a, b)
        elif option == 4:
            result = calculator.divide(a, b)
        else:
            console.writeLine("Błedny wybór spróbój ponownie")
            continue

        console.writeLine(f"Wynik to: {result}")
    except ValueError:
        console.writeLine("Wybrałeś nieprawidłową opcję. Uruchom program ponownie")
    except Exception:
        console.writeLine("Nieznany błąd, spróbuj uruchomić program ponownie")
