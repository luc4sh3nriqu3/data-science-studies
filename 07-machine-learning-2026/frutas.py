#%%
import pandas as pd
from sklearn import tree
#%%

df = pd.read_excel('data/dados_frutas.xlsx')

y = df['Fruta']

caracteristicas = ['Arredondada', 'Suculenta', 'Vermelha', 'Doce']
x = df[caracteristicas]
x

# Declarando um modelo de árvore de decisão (random_state permite a árvore partir de um ponto de aleatoriedade específico)
# random_state permite criar o mesmo modelo a partir de máquinas e códigos diferentes
arvore = tree.DecisionTreeClassifier(random_state=42)
# %%
arvore.fit(x, y)
# %%
arvore.predict([[0, 0, 0, 0]])
#%%

# Plotando a árvore de decisão
import matplotlib.pyplot as plt

plt.figure(dpi=400)
tree.plot_tree(arvore,
               feature_names=caracteristicas,
               class_names=arvore.classes_,
               filled=True)
#%%
proba = arvore.predict_proba([[0, 0, 0, 0]])[0] #Mostra a probabilidade de ser cada uma das classes possíveis
pd.Series(proba, index=arvore.classes_)