import pandas as pd
import matplotlib.pyplot as plt

nomesColunas = ["Data", "Brasil", "Ceará", "Minas Gerais", "Paraná", "Rio de Janeiro"]
linhasPular = []
for i in range(172):

    linhasPular.append(i)

gripe_df = pd.read_csv('data.csv', header=None, skiprows=linhasPular, usecols=[0, 1, 2, 4, 5, 6], names=nomesColunas)

gripe_df.boxplot(grid = False)

plt.show()