#%%
import pandas as pd
from sklearn import tree
#%%

dados = pd.read_parquet('data/dados_clones.parquet')


replaces = {
    'Tipo 1': 1,
    'Tipo 2': 2,
    'Tipo 3': 3,
    'Tipo 4': 4,
    'Tipo 5': 5,

    'Aayla Secura' : 1,
    'Obi-Wan Kenobi' : 2,
    'Mace Windu' : 3,
    'Yoda' : 4,
    'Shaak Ti' : 5

}

dados
#%%
target = 'Status '
features = [
    'Massa(em kilos)',
    'Estatura(cm)', 'Distância Ombro a ombro', 'Tamanho do crânio',
    'Tamanho dos pés', 'Tempo de existência(em meses)'
]

x = dados[features]
y = dados[target]

x = x.replace(replaces)
#%%
model = tree.DecisionTreeClassifier()

model.fit(X=x, y=y)
#%%
tree.plot_tree(model, feature_names=features,
               class_names=model.classes_,
               filled=True, max_depth=3)