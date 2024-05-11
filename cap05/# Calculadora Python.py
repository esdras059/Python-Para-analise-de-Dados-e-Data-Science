# Calculadora Python
print("********************** Calculadora em Python ********************\n")

opcao = int(input("Escolha a operação (1/2/3/4): "))
a = int(input("Digite o primeiro valor: "))
b = int(input("Digite o segundo valor: "))
if opcao == 1:
    print(a , " + " , b , " = " , a+b)
elif opcao == 2:
    print(a , " - " , b , " = " , a-b)
elif opcao == 3:
    print(a , " * " , b , " = " , a*b)
elif opcao == 4:
    print(a , " / " , b , " = " , a/b)
else:
    print("Valor não válido.")