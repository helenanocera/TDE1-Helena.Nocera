nome = input("Nome do arquivo: ")
arquivo = open(nome, "r")

lista_geral = []
linhas = arquivo.readlines()

for linha in linhas:
    elementos = linha.strip().split(', ')
    lista_geral.append(elementos)

def formatar(conjunto):
    return ', '.join(conjunto)

for i in range(len(lista_geral)):
    for elemento in lista_geral[i]:
        if len(lista_geral[i]) == 1:
            if elemento == 'U':
                if i + 2 < len(lista_geral):
                    conjunto1 = set(lista_geral[i + 1])
                    conjunto2 = set(lista_geral[i + 2])
                    print(f"União: conjunto 1 {{{formatar(conjunto1)}}}, conjunto 2 {{{formatar(conjunto2)}}}. Resultado: {{{formatar(conjunto1 | conjunto2)}}}")
            elif elemento == 'I':
                if i + 2 < len(lista_geral):
                    conjunto1 = set(lista_geral[i + 1])
                    conjunto2 = set(lista_geral[i + 2])
                    print(f"Intersecção: conjunto 1 {{{formatar(conjunto1)}}}, conjunto 2 {{{formatar(conjunto2)}}}. Resultado: {{{formatar(conjunto1 & conjunto2)}}}")
            elif elemento == 'D':
                if i + 2 < len(lista_geral):
                    conjunto1 = set(lista_geral[i + 1])
                    conjunto2 = set(lista_geral[i + 2])
                    print(f"Diferença: conjunto 1 {{{formatar(conjunto1)}}}, conjunto 2 {{{formatar(conjunto2)}}}. Resultado: {{{formatar(conjunto1 - conjunto2)}}}")
            elif elemento == 'C':
                if i + 2 < len(lista_geral):
                    conjunto1 = set(lista_geral[i + 1])
                    conjunto2 = set(lista_geral[i + 2])
                    cartesiano = [(a, b) for a in conjunto1 for b in conjunto2]
                    cartesiano_str = ', '.join([f"({a}, {b})" for a, b in cartesiano])
                    print(f"Produto Cartesiano: conjunto 1 {{{formatar(conjunto1)}}}, conjunto 2 {{{formatar(conjunto2)}}}. Resultado: {cartesiano_str}")


