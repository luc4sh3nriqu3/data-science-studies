def calc_imposto(preco:float, tx_base=0.03, **kwargs): #Kwargs funcina como o args, porém o args é uma espécie de tupla de valores (somente os valores são adicionados) enquanto o args é uma espécie de dicionário de argumentos (chave: valor)
    imposto = preco * tx_base

    for i in kwargs:
        print(i, kwargs[i])
        imposto += preco * kwargs[i]
    
    return imposto

print(calc_imposto(100, 0.03, municipio=0.01, estadual=0.005))
#além de municipio e estadual, podemos adicionar infinitos impostos novos sem que a função precise reconhecelos e o código não irá quebrar.

#Outra maneira de fazer a mesma coisa

impostos_gerais = {
    'municipio': 0.01,
    'estadual': 0.005,
    'nacional': 0.001
}

print(calc_imposto(100, 0.03, **impostos_gerais))