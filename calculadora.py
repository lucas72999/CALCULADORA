print("========== calculadora ==========")

operaçoes = input("escolha uma operaçao:") 

num1 = float(input("Digite o primeiro numero:"))
num2 = float(input("Digite o segundo numero:"))

if operaçoes == "SOMA":
    print(num1 + num2)

if operaçoes == "SUBTRAÇAO":
    print(num1 - num2)

