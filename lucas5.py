import pandas as pd

produtos=[]
print()
quantidade=int(input('Quantos produtos você quer adicionar? '))
try:
    for i in range(quantidade):
       produto=input(f'{i+1} Qual é o nome do produto: ')
       print()
       quantidade=int(input(f'{i+1} Qual é a quntidade do seu produto: '))
       print()
       preco=int(input(f'{i+1} Digite o preço do seu produto: '))
       soma=+preco
       print()
       total_rendido= preco * quantidade
       produtos.append({
           'Produtos': produto,
           'Quantidade': quantidade,
           'Preço (R$)':preco,
           'Total (R$)': total_rendido})
       
except ValueError:
    print()
    print('Digite um valor ou quantidade do itens')
    print()

df=pd.DataFrame(produtos)

print(df)