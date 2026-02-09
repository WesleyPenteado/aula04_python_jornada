import csv


caminho_do_arquivo = str = "exemplo.csv"

arquivo_csv: list = []

# With é um gerenciador de contexto, ele é utilizado para abrir arquivos, e ele garante que o arquivo 
# seja fechado corretamente após o uso, mesmo que ocorra um erro durante a manipulação do arquivo.

with open(file=caminho_do_arquivo, mode="r", encoding="utf-8") as arquivo:
    leitor_csv = csv.DictReader(arquivo)
    for linha in leitor_csv:
        arquivo_csv.append(linha)

print(arquivo_csv)

