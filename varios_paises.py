def conversor(tipo_pesos, valor_dolar):
    pesos = input("¿Cuantos pesos" +tipo_pesos+"tienes?: ")
    pesos = float(pesos)
    dolares = pesos/valor_dolar 
    dolares = round(dolares, 2)
    dolares = str(dolares)
    print(f"tienes $ {dolares} dolares")

menu = """

    Bienvenido al conversor de monedas(❁´◡`❁)(●'◡'●)
    elige una opción:

    1- Pesos Colombianos
    2- Pesos argentinos
    3- Pesos mexicanos
"""
opcion = int(input(menu))

if opcion == 1:
    conversor("colombianos", 3875)
elif opcion == 2:
    conversor("Argentinos", 65)
elif opcion == 3:
    conversor("Mexicanos", 24)
    
else:
    print("Ingresa una opción correcta por favor ಥ_ಥ")