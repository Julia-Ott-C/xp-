#!/usr/bin/env python
# coding: utf-8

# 

# In[9]:


#Chamando a bibilioteca pandas com apelido pd
import pandas as pd


# In[10]:


#Lendo o aquivo
dados_VENDAS = pd.read_excel(r'C:\Users\julia.colognese\Documents\Teste\XPinvestimento\XPinvestimento\Base-Dados-Desafio-D&A-01.xlsx',sheet_name='VENDAS')
dados_PRODUTOS = pd.read_excel(r'C:\Users\julia.colognese\Documents\Teste\XPinvestimento\XPinvestimento\Base-Dados-Desafio-D&A-01.xlsx',sheet_name='PRODUTOS')


# In[11]:


#Apresentando os dados das VENDAS
dados_VENDAS


# In[12]:


#Apresentando os dados das PRODUTOS
dados_PRODUTOS


# In[14]:


#1. Qual é o perfil demográfico dos clientes da empresa XYZ?

#Temos as colunas Clientes e Estado, agrupa os clientes por estado (bahia tem o cliente número 3)
UF_CLIENTES = dados_VENDAS.groupby('ESTADO')['CLIENTE'].unique()


# In[35]:


print(UF_CLIENTES)


# In[36]:


#armazenar nesse dicionário onde estado é a vhave e cliente o conteudo
clientes_por_estado = {}
#percorre cada estado pela sua lista de clientes, o metodo items faz a interação  
for estado, clientes in UF_CLIENTES.items():
    #usa-se a função len para pegar o tamanho da lista de clientes de cada estado e guarda no dicionário
    clientes_por_estado[estado] = len(clientes)


# In[38]:


#Separando por estado e por quantidade de clientes
estado_q = clientes_por_estado.keys()
QUANTIDADE = clientes_por_estado.values()


# In[39]:


#Importando para fazer os graficos
import matplotlib.pyplot as plt


# In[40]:


total_clientes = len(dados_VENDAS['CLIENTE'].unique())

percentual =[(quantidade * 100 )/ total_clientes for quantidade in QUANTIDADE]
fig = plt.figure(figsize =(10, 7)) 
plt.title('Perfil demográfico dos clientes da empresa')
plt.pie(percentual, labels = estado_q, autopct= '%1.f%%',startangle=90) 
plt.show() 


# A empresa tem uma concentração maior de clientes em Santa catarina e na Paraíba 

# In[33]:


#2. Qual a categoria de produto mais vendidas e a menos vendidas?
PRODUTO_QUANTIDADE_VENDIDA = dados_VENDAS.groupby('PRODUTO')['QUANTIDADE_VENDIDA'].sum()
PRODUTO_QUANTIDADE_VENDIDA


# In[20]:


junta = pd.merge(PRODUTO_QUANTIDADE_VENDIDA,dados_PRODUTOS,left_on='PRODUTO', right_on='PRODUTO')
junta


# In[21]:


y= junta['QUANTIDADE_VENDIDA']
x = junta['CATEGORIA']

fig = plt.figure(figsize =(10, 7)) 
plt.title('Categoria de produto mais vendidas e a menos vendidas')
plt.xlabel('Categoria')
plt.ylabel('Quantidade vendida')
plt.bar(x,y)
plt.xticks(x, rotation=45)
plt.show()


# A categoria de produto mais vendida é a UTILIDADES DOMÉSTICAS e a menos vendida JARDINAGEM

# In[22]:


#3. Há alguma relação entre as vendas e a época do ano?
##Agrupar vendas por mes(Qual mes eu vendi mais)
import matplotlib.pyplot as plt
QUANTIDADE_DATA = dados_VENDAS.groupby(dados_VENDAS['DATA'].dt.month)['QUANTIDADE_VENDIDA'].sum().reset_index(name='QUANTIDADE')
QUANTIDADE_DATA

y= QUANTIDADE_DATA['QUANTIDADE']
x = QUANTIDADE_DATA['DATA']

fig = plt.figure(figsize =(10, 7)) 
plt.title('Vendas por mês')
plt.bar(x,y)
plt.xlabel('Mês')
plt.ylabel('Quantidade vendida')
plt.xticks(x, rotation=45)

plt.show()


# No mês 8 existiu  aumento nas vendas, no mês 6 uma diminuição das vendas.

# In[168]:


#4. Qual é a tendência de vendas por região geográfica?
PRODUTO_QUANTIDADE_VENDIDA_regiao = dados_VENDAS.groupby('ESTADO')['QUANTIDADE_VENDIDA'].sum()
PRODUTO_QUANTIDADE_VENDIDA_regiao


# In[23]:



produtos_estado = dados_VENDAS.groupby(['ESTADO','PRODUTO'])['QUANTIDADE_VENDIDA'].unique()
produtos_estado


# Na BAHIA a categoria mais venida foi a B, NO PARANÁ C....    

# In[25]:


#5. Há alguma correlação entre a idade dos clientes e as categorias de produtos que eles compram?
#Idade de x anos compram tais produtos 


# In[29]:


CLIENTE_IDADE = dados_VENDAS.groupby(['IDADE','PRODUTO'])['CLIENTE'].unique()
CLIENTE_IDADE


# Os clientes com 47 e 43 anos realizaram compras dos itens das categorias A, B e C porém que tem 47 anos comprou também itens da categora E...         
#        
