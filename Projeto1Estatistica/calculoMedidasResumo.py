import pandas as pd

nomesColunas = ["Data", "Brasil", "Ceará", "Minas Gerais", "Paraná", "Rio de Janeiro"]
linhasPular = []
for i in range(172):

    linhasPular.append(i)

gripe_df = pd.read_csv('data.csv', header=None, skiprows=linhasPular, usecols=[0, 1, 2, 4, 5, 6], names=nomesColunas)

print("                 MEDIDAS DE POSIÇÃO                  \n")
#Cálculo da MÉDIA de buscas no google relacionadas a gripe no Brasil, por estado.
print("1. Média de buscas no google relacionadas a gripe no Brasil de '22/01/2006' à '09/08/2015'.\n")
print("     1.1 Média para o estado do CEARÁ: %.2f" %gripe_df["Ceará"].mean())
print("     ------------------------------------------------\n")
print("     1.2 Média para o estado de MINAS GERAIS: %.2f" %gripe_df["Minas Gerais"].mean())
print("     ------------------------------------------------\n")
print("     1.3 Média para o estado do PARANÁ: %.2f" %gripe_df["Paraná"].mean())
print("     ------------------------------------------------\n")
print("     1.4 Média para o estado do RIO DE JANEIRO: %.2f" %gripe_df["Rio de Janeiro"].mean())
print("     ------------------------------------------------\n")
print("     1.5 Média para o Brasil: %.2f" %gripe_df["Brasil"].mean())
print("     ------------------------------------------------\n\n")

#Cálculo da MODA de buscas no google relacionadas a gripe no Brasil, por estado.
print("2. Moda de buscas no google relacionadas a gripe no Brasil de '22/01/2006' à '09/08/2015'.\n")
print("2.1 Moda para o estado do CEARÁ:\n", gripe_df["Ceará"].mode())
print("------------------------------------------------\n")
print("2.2 Moda para o estado de MINAS GERAIS: \n", gripe_df["Minas Gerais"].mode())
print("------------------------------------------------\n")
print("2.3 Moda para o estado do PARANÁ: \n", gripe_df["Paraná"].mode())
print("------------------------------------------------\n")
print("2.4 Moda para o estado do RIO DE JANEIRO: \n", gripe_df["Rio de Janeiro"].mode())
print("------------------------------------------------\n")
print("2.5 Moda para o Brasil: \n", gripe_df["Brasil"].mode())
print("------------------------------------------------\n\n")

#Cálculo da MEDIANA de buscas no google relacionadas a gripe no Brasil, por estado.
print("3. Mediana de buscas no google relacionadas a gripe no Brasil de '22/01/2006' à '09/08/2015'.\n")
print("     3.1 Mediana para o estado do CEARÁ: %.2f" %gripe_df["Ceará"].median())
print("     ------------------------------------------------\n")
print("     3.2 Mediana para o estado de MINAS GERAIS: %.2f" %gripe_df["Minas Gerais"].median())
print("     ------------------------------------------------\n")
print("     3.3 Mediana para o estado do PARANÁ: %.2f" %gripe_df["Paraná"].median())
print("     ------------------------------------------------\n")
print("     3.4 Mediana para o estado do RIO DE JANEIRO: %.2f" %gripe_df["Rio de Janeiro"].median())
print("     ------------------------------------------------\n")
print("     3.5 Mediana para o Brasil: %.2f" %gripe_df["Brasil"].median())
print("     ------------------------------------------------\n\n")

print("                 MEDIDAS DE DISPERSÃO                  \n")
#Cálculo da AMPLITUDE de buscas no google relacionadas a gripe no Brasil, por estado.
print("1. Amplitude de buscas no google relacionadas a gripe no Brasil de '22/01/2006' à '09/08/2015'.\n")
print("     1.1 Amplitude para o estado do CEARÁ: %.2f" %(gripe_df["Ceará"].max() - gripe_df["Ceará"].min()))
print("     ----------------------------------------------------\n")
print("     1.2 Amplitude para o estado de MINAS GERAIS: %.2f" %(gripe_df["Minas Gerais"].max() - gripe_df["Minas Gerais"].min()))
print("     ----------------------------------------------------\n")
print("     1.3 Amplitude para o estado do PARANÁ: %.2f" %(gripe_df["Paraná"].max() - gripe_df["Paraná"].min()))
print("     ----------------------------------------------------\n")
print("     1.4 Amplitude para o estado do RIO DE JANEIRO: %.2f" %(gripe_df["Rio de Janeiro"].max() - gripe_df["Rio de Janeiro"].min()))
print("     ----------------------------------------------------\n")
print("     1.5 Amplitude para o Brasil: %.2f" %(gripe_df["Brasil"].max() - gripe_df["Brasil"].min()))
print("     ----------------------------------------------------\n\n")

#Cálculo do DESVIO ABSOLUTO de buscas no google relacionadas a gripe no Brasil, por estado.
print("2. Desvio Absoluto de buscas no google relacionadas a gripe no Brasil de '22/01/2006' à '09/08/2015'.\n")
print("     2.1 Desvio Absoluto para o estado do CEARÁ: %.2f" %gripe_df["Ceará"].mad())
print("     ----------------------------------------------------------\n")
print("     2.2 Desvio Absoluto para o estado de MINAS GERAIS: %.2f" %gripe_df["Minas Gerais"].mad())
print("     ----------------------------------------------------------\n")
print("     2.3 Desvio Absoluto para o estado do PARANÁ: %.2f" %gripe_df["Paraná"].mad())
print("     ----------------------------------------------------------\n")
print("     2.4 Desvio Absoluto para o estado do RIO DE JANEIRO: %.2f" %gripe_df["Rio de Janeiro"].mad())
print("     ----------------------------------------------------------\n")
print("     2.5 Desvio Absoluto para o Brasil: %.2f" %gripe_df["Brasil"].mad())
print("     ----------------------------------------------------------\n\n")

#Cálculo da VARIÂNCIA de buscas no google relacionadas a gripe no Brasil, por estado.
print("3. Variância de buscas no google relacionadas a gripe no Brasil de '22/01/2006' à '09/08/2015'.\n")
print("     3.1 Variância para o estado do CEARÁ: %.2f" %gripe_df["Ceará"].var())
print("     ----------------------------------------------------------\n")
print("     3.2 Variância para o estado de MINAS GERAIS: %.2f" %gripe_df["Minas Gerais"].var())
print("     ----------------------------------------------------------\n")
print("     3.3 Variância para o estado do PARANÁ: %.2f" %gripe_df["Paraná"].var())
print("     ----------------------------------------------------------\n")
print("     3.4 Variância para o estado do RIO DE JANEIRO: %.2f" %gripe_df["Rio de Janeiro"].var())
print("     ----------------------------------------------------------\n")
print("     3.5 Variância para o Brasil: %.2f" %gripe_df["Brasil"].var())
print("     ----------------------------------------------------------\n\n")

#Cálculo do DESVIO PADRÃO de buscas no google relacionadas a gripe no Brasil, por estado.
print("4. Desvio Padrão de buscas no google relacionadas a gripe no Brasil de '22/01/2006' à '09/08/2015'.\n")
print("     4.1 Desvio Padrão para o estado do CEARÁ: %.2f" %gripe_df["Ceará"].std())
print("     ----------------------------------------------------------\n")
print("     4.2 Desvio Padrão para o estado de MINAS GERAIS: %.2f" %gripe_df["Minas Gerais"].std())
print("     ----------------------------------------------------------\n")
print("     4.3 Desvio Padrão para o estado do PARANÁ: %.2f" %gripe_df["Paraná"].std())
print("     ----------------------------------------------------------\n")
print("     4.4 Desvio Padrão para o estado do RIO DE JANEIRO: %.2f" %gripe_df["Rio de Janeiro"].std())
print("     ----------------------------------------------------------\n")
print("     4.5 Desvio Padrão para o Brasil: %.2f" %gripe_df["Brasil"].std())
print("     ----------------------------------------------------------\n\n")

print("                      SEPARATRIZES                       \n")
#Cálculo das SEPARATRIZES(1º, 2º e 3º QUARTIS) de buscas no google relacionadas a gripe no Brasil, por estado.
print("1. Separatrizes das buscas no google relacionadas a gripe no Brasil de '22/01/2006' à '09/08/2015'.\n")
print("     1.1 Separatrizes para o estado do CEARÁ:\n      Q1 = %.2f\n      Q2 = %.2f\n      Q3 = %.2f" %(gripe_df["Ceará"].quantile(q=0.25), gripe_df["Ceará"].quantile(), gripe_df["Ceará"].quantile(q=0.75)))
print("     ----------------------------------------------------------\n")
print("     1.2 Separatrizes para o estado de MINAS GERAIS:\n      Q1 = %.2f\n      Q2 = %.2f\n      Q3 = %.2f" %(gripe_df["Minas Gerais"].quantile(q=0.25), gripe_df["Minas Gerais"].quantile(), gripe_df["Minas Gerais"].quantile(q=0.75)))
print("     ----------------------------------------------------------\n")
print("     1.3 Separatrizes para o estado do PARANÁ:\n      Q1 = %.2f\n      Q2 = %.2f\n      Q3 = %.2f" %(gripe_df["Paraná"].quantile(q=0.25), gripe_df["Paraná"].quantile(), gripe_df["Paraná"].quantile(q=0.75)))
print("     ----------------------------------------------------------\n")
print("     1.4 Separatrizes para o estado do RIO DE JANEIRO:\n      Q1 = %.2f\n      Q2 = %.2f\n      Q3 = %.2f" %(gripe_df["Rio de Janeiro"].quantile(q=0.25), gripe_df["Rio de Janeiro"].quantile(), gripe_df["Rio de Janeiro"].quantile(q=0.75)))
print("     ----------------------------------------------------------\n")
print("     1.5 Separatrizes para o Brasil:\n      Q1 = %.2f\n      Q2 = %.2f\n      Q3 = %.2f" %(gripe_df["Brasil"].quantile(q=0.25), gripe_df["Brasil"].quantile(), gripe_df["Brasil"].quantile(q=0.75)))
print("     ----------------------------------------------------------\n\n")