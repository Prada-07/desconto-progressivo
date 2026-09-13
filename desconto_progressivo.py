# O usuário irá colocar o valor da compra do cliente, em reais. Apenas valores númericos aceitos.
try:
    valor = float(input("Digite o valor da compra:\n-> "))
except ValueError:
    print("Valor inváĺıdo. Digite um número.")
    exit()


# Condiçııo se o valor for menor que 200, recebe um desconto de 5%.
if valor < 200.00:
    desconto = 0.05


# Condiçııo se o valor for maior ou igual a 200 e menor que 300, recebe um desconto de 10%.
elif 200 <= valor < 300:
    desconto = 0.1


# Condiçııo se o valor for maior que 300, recebe um desconto de 15%.
else:
    desconto = 0.15
    
valor_final = valor - (valor * desconto) # Operaçııo básica para realizar o desconto do valor do produto.


# Exibiçııo do valor original do produto, valor descontado e valor final.
print(f"VALOR DA COMPRA: R${valor:.2f}")
print(f"DESCONTO: R${valor * desconto:.2f}")
print(f"VALOR FINAL: R${valor_final:.2f}")