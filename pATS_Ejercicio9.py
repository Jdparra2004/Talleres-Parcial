'''
Hacer un programa que simule un cajero automático con un saldo incicial de 1000 y tendrá el siguiente menú de opciones
'''

saldo_inicial = float(input("Ingrese el valor de saldo de su cuenta: "))

operacion = float(input(f"Seleccione la operación que quiera realizar:\n 1. Ingresar dinero\n 2. Retirar dinero\n 3. Mostrar dinero\n 4- Salir\n : "))

if operacion == 1:
    valor = float(input("Dígite el monto a ingresar en la cuenta: "))
    print(f"El valor ingresado es: ${valor}")
    
    mostrar_valor = input("Desea ver el monto total en la cuenta(si, no): ").lower()
    if mostrar_valor == 'si':
        suma = saldo_inicial + valor
        print(f"usted tiene ${suma} en su cuenta\n Fin de la transacción, vuelva pronto")
    else:
        print("Fin de la transacción, vuelva pronto")

elif operacion == 2:
    valor = float(input("Dígite el monto a retirar de la cuenta: "))
    print(f"El monto retirado es: {valor}")
    
    if saldo_inicial < valor:
        print("Fondos insuficientes")
    mostrar_valor = input("Desea ver el monto restante en la cuenta(si, no): ").lower()
    if mostrar_valor == 'si':
        resta = saldo_inicial - valor
        print(f"Tiene ${resta} en su cuenta")
        
elif operacion ==   3:
    print(f"El valor en la cuenta es {saldo_inicial}")
    
else:
    print("Transacción Finalizada, vuelva pronto")
    
