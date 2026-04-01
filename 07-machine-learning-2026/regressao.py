#%%
import pandas as pd

df = pd.read_excel('data/dados_cerveja_nota.xlsx')
df.head()
# %%
from sklearn import linear_model
from sklearn import tree

X = df[['cerveja']] #Matriz (DataFrame)
y = df['nota']      #Vetor (Série)

# %%
reg = linear_model.LinearRegression()
reg.fit(X, y)

arvore_full = tree.DecisionTreeRegressor(random_state=42)
arvore_full.fit(X, y)
arvore_predict = arvore_full.predict(X.drop_duplicates())

#%%
a, b = reg.coef_[0], reg.intercept_ #Coeficiente angular e linear
print(f'Coeficiente angular: {a:.2f}')
print(f'Coeficiente linear: {b:.2f}')

#%%
predict_reg = reg.predict(X.drop_duplicates())

# %%
import matplotlib.pyplot as plt
plt.plot(X['cerveja'], y, 'o')
plt.grid(True)
plt.title('Cerveja x Nota')
plt.xlabel('Cerveja')
plt.ylabel('Nota')
plt.plot(X.drop_duplicates()['cerveja'], predict_reg, 'r-')
plt.plot(X.drop_duplicates()['cerveja'], arvore_predict, 'g-')

plt.legend(['Observado', f'Predito: y = {a:.3f}x + {b:.3f}', 'Predito (Árvore)'])