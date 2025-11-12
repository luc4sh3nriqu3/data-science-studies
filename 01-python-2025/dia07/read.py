# %%
nome_arquvivo = 'historia.txt'

#Abre o arquivo em modo de leitura
open_file = open(nome_arquvivo)

#Lê os dados do arquivo
conteudo = open_file.read()
print(conteudo)

#Fecha o arquivo
open_file.close()
# %%

#Faz as mesmas coisas que as linhas acima
with open(nome_arquvivo) as open_file:
    conteudo = open_file.read()

print(conteudo)
# %%
