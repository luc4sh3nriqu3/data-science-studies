# %%
arquivo = 'data.csv'

with open(arquivo) as open_file:
    lines = open_file.readlines() #cada linha do arquivo virá um elemento na lista

for l in lines:
    print(l)

# %%
chaves = lines[0]
chaves

chaves = lines[0].strip('\n').split(';') #Retira o \n da string a ser armazenada e separa os valores a cada ';'
chaves
# %%
dados = dict()

for c in chaves:
    dados[c] = []

print(dados)
# %%
for l in lines[1:]:

    valores = l.strip('\n').split(';')
    
    for i in range(0, len(valores)):
        
        dados[chaves[i]].append(valores[i])
    
dados
# %%

idades = []

for i in dados['idade']:
    idades.append(int(i))

print(idades)

media = sum(idades) / len(idades)
print(media)
# %%
