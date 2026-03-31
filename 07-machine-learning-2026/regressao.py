#%%
import pandas as pd

df = pd.read_excel('data/dados_cerveja_nota.xlsx')
df.head()
# %%
from sklearn import linear_model

X = df[['cerveja']] #Matriz (DataFrame)
y = df['nota']      #Vetor (Série)

# %%
reg = linear_model.LinearRegression()
reg.fit(X, y)
#%%
a, b = reg.coef_[0], reg.intercept_ #Coeficiente angular e linear
print(f'Coeficiente angular: {a:.2f}')
print(f'Coeficiente linear: {b:.2f}')

#%%
predict = reg.predict(X.drop_duplicates())

# %%
import matplotlib.pyplot as plt
plt.plot(X['cerveja'], y, 'o')
plt.grid(True)
plt.title('Cerveja x Nota')
plt.xlabel('Cerveja')
plt.ylabel('Nota')
plt.plot(X.drop_duplicates()['cerveja'], predict, 'r-')