def get_integer_input(prompt, min_value, max_value):
    """
1) Loote oma mustri
2) Mustrit saab genereerida sisendinfo alusel. nt. Mitu rida: 2, Mitu tulpa: 3
3) Sisendinfo on kontrollitud. nt. "A" - ei sobi. nt. 4.5 muudetakse täisarvuks
4) Sisendinfo piirang - jaburaid numbreid ei saa panna n.t. -30, 666
5) Enne algust annate juhised kasutajale:
    "Programm genereerib mustri, kui sisestada koordinaadid"
6) Kui sisend ei vasta nõuetele, annate ka märku
7) Genereerite vastava mustri, kui kõik sobib
8) Muster on eristatav. Plokkide piirid on näha.

Testimiseks:
input.isdigit()
input.isalpha()
input.isspace()
neid on veel

piiranguteks tingimuslaused
mustrite jaoks tsükleid
korduvad osad koodis, siis funktsioonid

"""
    while True:
        try:
            value = input(prompt)
            if '.' in value:
                value = int(float(value))  # Muudame komakohaga arvu täisarvuks
            else:
                value = int(value)
            if min_value <= value <= max_value:
                return value
            else:
                print(f"Palun sisesta number vahemikus {min_value} kuni {max_value}.")
        except ValueError:
            print("Palun sisesta sobiv täisarv.")


def display_pattern_samples():
    """
    Näitab kasutajale kahte mustri näidist:
    1) Telliskivimuster
    2) Poolplokkide muster
    """
    print("\nMustri näidised:")
    print("1. Telliskivimuster:")
    print("|[]| |[]| ")
    print("|[]| |[]| ")
    print("\n2. Poolplokkide muster:")
    print("▄▄ ▀▀ ▄▄ ")
    print("▀▀ ▄▄ ▀▀ ")


def get_pattern_choice():
    """
    Küsib kasutajalt, millist mustrit nad soovivad kasutada.
    Kuvatakse mõlemad mustri näidised enne valikut.
    """
    display_pattern_samples()

    while True:
        choice = input("Vali muster (1 - Telliskivimuster, 2 - Poolplokkide muster): ")
        if choice in ['1', '2']:
            return choice
        else:
            print("Vigane sisend. Palun vali 1 või 2.")


def generate_block_pattern(rows, cols, choice):
    """
    Genereerib plokkidega eristatava mustri vastavalt kasutaja sisestatud ridade ja veergude arvule.
    Kui valitakse 1, kasutatakse telliskivimustrit.
    Kui valitakse 2, kasutatakse vaheldumisi poolplokke.
    """
    print("\nGenereeritud muster:\n")
    if choice == '1':
        # Telliskivimuster
        for row in range(rows):
            for col in range(cols):
                print("|[]|", end=" ")  # Telliskivide muster
            print()  # Uus rida
    elif choice == '2':
        # Poolplokkide muster
        for row in range(rows):
            for col in range(cols):
                if (row + col) % 2 == 0:
                    print("▄▄", end=" ")  # Alumine poolplokk
                else:
                    print("▀▀", end=" ")  # Ülemine poolplokk
            print()  # Uus rida


def main():
    print("Programm genereerib mustri plokkidega, kui sisestada ridade ja veergude arv.")
    print("Valige sobiv muster ja mõõtmed (read ja tulbad) vastavalt juhistele.\n")

    # Küsime kasutajalt ridade ja veergude arvu
    rows = get_integer_input("Mitu rida? (1-20): ", 1, 20)
    cols = get_integer_input("Mitu tulpa? (1-20): ", 1, 20)

    # Valime mustri
    pattern_choice = get_pattern_choice()

    # Genereerime mustri vastavalt kasutaja valikule
    generate_block_pattern(rows, cols, pattern_choice)


if __name__ == "__main__":
    main()
