def imprime_nome(nome):
    print(f"Nome: {nome}")

def imprime_piramide(quantidade):
    for x in range(1, quantidade + 1):
        for j in range(0, x):
            print(x, end="")
        print()

def contarVogais(texto):
    contador = 0
    for x in range (len(texto)):
        if texto[x] in "aeiouAEIOU":
            contador += 1
    print(f"Quantidades de vogais no texto: {contador}")

def estoque(produto,quantidade,valorunidade):
    valorTotal = quantidade * valorunidade
    return valorTotal

def argumento(valor):
        if valor > 0:
            return "P"
        elif valor < 0:
            return "N"
        else:
            return "Z"

def soma(valor1,valor2):
    result = valor1 + valor2
    print(f"{valor1} + {valor2} = {result}")

def somatupla(*args):
    result = 0
    for x in range(len(args)):
      result += args[x]

    print(f"Resultado da soma dos numeros: {result}")

def texto_contratio (texto):
    cont = 0
    print("Texto ao contrario: ", end="")
    for x in range (len(texto)-1,-1,-1):
        if texto[x] != " ":
            cont += 1
        print(texto[x], end="")
    print(f"\nQuantidade de letras: {cont}")

def lista_argumento(lista):
    listanova = []
    for x in lista:
        if x not in listanova:
            listanova.append(x)

    print(listanova)