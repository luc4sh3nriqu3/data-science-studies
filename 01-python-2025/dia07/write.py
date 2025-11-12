#%%
nome_arquivo = 'historia02.txt'

txt = 'Chupa meu pintaçio'

#Modo w sobrescreve o arquivo existente
#Modo a adiciona conteúdo ao já existente
with open(nome_arquivo, mode='a') as open_file:
    open_file.write(txt)
# %%
