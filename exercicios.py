# 1. Crie uma lista com os números de 1 a 10 
# e use um loop para imprimir cada número elevado ao quadrado.

# numeros = list(range(1, 11))

# for numero in numeros:
#     print(numero ** 2)


# 2. Dada a lista ["Python", "Java", "C++", "JavaScript"], 
# remova o item "C++" e adicione "Ruby".


# lista = ["Python", "Java", "C++", "JavaScript"]

# lista.remove("C++")
# lista.append("Ruby")

# print(lista)


# 3. Crie um dicionário para armazenar informações de um livro, incluindo título, 
# autor e ano de publicação. Imprima cada informação.

# from typing import Dict, Any


# livro: Dict[str, Any] = {
#     "Título": "Jurassic Park",
#     "Autor": "Michael Crichton",
#     "Ano de publicação": "1990"
#     }

# lista_de_livros = livro.items()
# for c, v in lista_de_livros:
#     print(f"{c}: {v}")

# 4. Escreva um programa que conta o número de ocorrências 
# de cada caractere em uma string usando um dicionário.


# def contar_caracteres(s):
#     s_limpo = s.lower()

#     contagem = {}
#     for caractere in s_limpo:
#        contagem[caractere] = contagem.get(caractere, 0) + 1
#     return contagem

# print(contar_caracteres("pneumouloultramicroscopicosilicovolcanoconiose"))


# 5. Dada a lista ["maçã", "banana", "cereja"] e o dicionário {"maçã": 0.45, "banana": 0.30, "cereja": 0.65}, 
# calcule o preço total da lista de compras.

# lista = ["maçã", "banana", "cereja"]
# dicionario = {"maçã": 0.45, "banana": 0.30, "cereja": 0.65}
# preço_total = sum(dicionario[fruta] for fruta in lista)
# print(f"O preço total da lista de compras é: R${preço_total:.2f}")


#6. Eliminação de Duplicatas
# Objetivo: Dada uma lista de emails, remover todos os duplicados.

# emails = ["user@example.com", "admin@example.com", "user@example.com", "manager@example.com"]
# emails_unicos = list(set(emails))
# print(emails_unicos)

# 7. Filtragem de Dados
# Objetivo: Dada uma lista de idades, filtrar apenas aquelas que são maiores ou iguais a 18.

# idades = [15, 22, 17, 30, 12, 18]
# maiores_iguais_18 = [idade for idade in idades if idade >= 18]
# print(maiores_iguais_18)

# 8. Ordenação Personalizada
# Objetivo: Dada uma lista de dicionários representando pessoas, ordená-las pelo nome.

# pessoas = [
#     {"nome": "Bob", "idade": 30},
#     {"nome": "Alice", "idade": 25},
#     {"nome": "Carol", "idade": 20}
# ]

# pessoas.sort(key = lambda pessoa: pessoa["nome"])

# print(pessoas)

# 9. Agregação de Dados
# Objetivo: Dado um conjunto de números, calcular a média

# numeros = [10, 20, 30, 40, 50]
# media = sum(numeros) / len(numeros)
# print(f"A média dos números é: {media}")

# 10. Divisão de Dados em Grupos
# Objetivo: Dada uma lista de valores, dividir em duas listas: uma para valores pares e outra para ímpares.

# valores = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# pares = [valor for valor in valores if valor % 2 == 0]
# impares = [valor for valor in valores if valor % 2 != 0]
# print(f"Valores pares: {pares}")
# print(f"Valores ímpares: {impares}")

# 11. Atualização de Dados
# Objetivo: Dada uma lista de dicionários representando produtos, atualizar o preço de um produto específico.

# produtos = [
#     {"id": 1, "nome": "Teclado", "preço": 100},
#     {"id": 2, "nome": "Mouse", "preço": 80},
#     {"id": 3, "nome": "Monitor", "preço": 300}
# ]

# id_pdto_atualizar = 1
# novo_preço = 120
# for produto in produtos:
#     if produto["id"] == id_pdto_atualizar:
#         produto["preço"] = novo_preço
#         break

# print(produtos)

# 12. Fusão de Dicionários
# Objetivo: Dados dois dicionários, fundi-los em um único dicionário.

# dicionario1 = {"a": 1, "b": 2}
# dicionario2 = {"c": 3, "d": 4}

# dicionario_fundido = {**dicionario1, **dicionario2}
                      
# print(dicionario_fundido)

# 13. Filtragem de Dados em Dicionário
# Objetivo: Dado um dicionário de estoque de produtos, filtrar aqueles com quantidade maior que 0.

# estoque = {"Produto A": 10, "Produto B": 0, "Produto C": 5, "Produto D": 0}
# produtos_disponiveis = {produto: quantidade for produto, quantidade in estoque.items() if quantidade > 0}
# print(produtos_disponiveis)

# 14. Extração de Chaves e Valores
# Objetivo: Dado um dicionário, criar listas separadas para suas chaves e valores

# dicionario = {"chave1": "valor1", "chave2": "valor2", "chave3": "valor3"}
# chaves = list(dicionario.keys())
# valores = list(dicionario.values())
# print(f"Chaves: {chaves}")
# print(f"Valores: {valores}")

# 15. Contagem de Frequência de Itens
# Objetivo: Dada uma string, contar a frequência de cada caractere usando um dicionário.

# string = "banana"
# contagem = {}
# for caractere in string:
#     contagem[caractere] = contagem.get(caractere, 0) + 1
# print(contagem)


# 16. Escreva uma função que receba uma lista de números e retorne a soma de todos os números.

# def soma_lista(numeros : list):
#     return sum(numeros)

# lista = [1,2,3,5]

# print(soma_lista(lista))


# 17. Crie uma função que receba um número como argumento e retorne True se o número for primo e False caso contrário.

# def numeros_primos(n):
#     if n <= 1:
#         return False
#     for i in range(2, int(n**0.5) + 1):
#         if n % i == 0:
#             return False
#     return True

# print(numeros_primos(20))  


# 18. Desenvolva uma função que receba uma string como argumento e retorne essa string revertida.

# def string_invertida(s : str):
#     return s[::-1]

# string = "Será que funciona?"

# print(string_invertida(string))


# 19. Implemente uma função que receba dois argumentos: uma lista de números e um número. A função deve retornar 
# todas as combinações de pares na lista que somem ao número dado.

# def encontrar_pares(lista, numero):
#     pares = []
#     for i in range(len(lista)):
#         for j in range(i + 1, len(lista)):
#             if lista[i] + lista[j] == numero:
#                 pares.append((lista[i], lista[j]))
#     return pares

# lista = [1, 2, 3, 4, 5, 6]
# numero = 7
# print(encontrar_pares(lista, numero))


# 20. Escreva uma função que receba um dicionário e retorne uma lista de chaves ordenadas

# def chaves_ordenadas(dicionario):
#     return sorted(dicionario.keys())

# dicionario = {"c": 3, "a": 1, "b": 2}
# print(chaves_ordenadas(dicionario))