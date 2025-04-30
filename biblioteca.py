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