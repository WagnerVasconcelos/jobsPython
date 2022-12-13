import pandas as pd


df = pd.read_csv('arquivo2.csv', sep=';')
   
def gerarArquivo(linha):
    valor = '10'
    dado = str(linha['nome']).ljust(30, ' ')
    dado+= valor.zfill(10)
    return dado


linhas = []

for index, row in df.iterrows():
    linhas.append(gerarArquivo(row))

with open("output.txt", "w") as txt_file:
    txt_file.write("\n".join(str(item) for item in linhas))