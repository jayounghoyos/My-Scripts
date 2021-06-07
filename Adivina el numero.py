print("""

    Bienvenido al juego, Adivina el número.

    La computadora pensará un número del uno al cien y tu debes adivinarlo

    Vamos a adivinar!
""")
numero_bot = range(1, 100)

elección = int(input("Cual es?: "))

if numero_bot <= elección:
    print(numero_bot-elección)
else:
    print("Error")