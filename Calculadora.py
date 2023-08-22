menu = """
Menu
==========================================
[1] Somar
[2] Subtrair
[3] Multiplicar
[4] Dividir
[5] Potência
==========================================
"""
n1, n2 = 0, 0
operacao = 0

print("Bem-Vindo!")
while True:
    print(f"{menu}")
    operacao = int(input("Escreva o número corespondente a opção desejada e pressione [Enter]: "))
    if (operacao == 1):
        print("Ok! Vamos somar!")
        n1 = int(input("Digite o primeiro número que deseja somar: "))
        n2 = int(input("Ok! Agora digite o segundo número: "))
        resultado = n1 + n2
        print(f"A soma entre {n1} e {n2} é: {resultado}")
    elif (operacao == 2):
        print("Ok! Vamos subtrair!")
        n1 = int(input("Digite o primeiro número que deseja subtrair: "))
        n2 = int(input("Ok! Agora digite o segundo número: "))
        resultado = n1 - n2
        print(f"A subtração entre {n1} e {n2} é: {resultado}")
    elif (operacao == 3):
        print("Ok! Vamos multiplicar!")
        n1 = int(input("Digite o primeiro número a ser multiplicado: "))
        n2 = int(input("Ok! Agora digite o segundo número: "))
        resultado = n1 * n2
        print(f"A multiplicação entre {n1} e {n2} é: {resultado}")
    elif (operacao == 4):
        print("Ok! Vamos dividir!")
        n1 = int(input("Digite o dividendo: "))
        n2 = int(input("Ok! Agora digite o divisor: "))
        if (n2 == 0):
            print("Ops! Não existe divisão por zero!")
        elif (n2 == 1):
            print(f"Qualquer número dividido por 1 resulta nele mesmo!\nLogo: {n1} dividido por {n2} é igual a {n1}")
        else: 
            resultado = n1 / n2
            print(f"A divisão de {n1} por {n2} é: {resultado}")
    elif (operacao == 5): 
        print("Ok! Vamos calcular a potência!")
        n1 = int(input("Digite o número correspondente a base: "))
        n2 = int(input("Ok! Agora o expoente: "))
        if (n2 == 0):
            print(f"Qualquer número quando elevado a 0 resulta em 1. \nLogo: {n1} elevado a {n2} é igual a 1.")
        elif (n2 == 1):
            print(f"Qualquer número elevado a 1 resulta nele mesmo. \nLogo: {n1} elevado a 1 é igual a {n1}")
        else:
            resultado = n1 ** n2
            print(f"{n1} elevado a {n2} é igual a: {resultado}")
    print(" Você deseja realizar uma nova operação? \n[1] SIM \n[0] NÃO")
    continuar = int(input())
    if (continuar == 0):
        print("Obrigado por utilizar nossa calculadora!")
        break
    elif ((continuar != 1) and (continuar != 0)):
        print("Tente novamente!")
    