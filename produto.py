from biblioteca import *

nome = input("Nome do produto: ")
quantidade = int(input("Quantidade no estoque: "))
valorunitario = float(input("Valor de cada unidade: "))

print(f"Valor total do estoque do produto {nome}: {estoque(nome,quantidade,valorunitario)}")