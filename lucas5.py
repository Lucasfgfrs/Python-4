import pandas as pd
import math

produtos=[]
print()
quantidades=int(input('Quantos produtos você quer adicionar? '))
try:
    for i in range(quantidades):
        print()
        produto=input(f'{i+1} Qual é o nome do produto: ')
        print()
        quantidade=int(input(f'{i+1} Qual é a quntidade do seu produto: '))
        print()
        preco=float(input(f'{i+1} Digite o preço do seu produto: '))
        print()      
        total_rendido= math.ceil(preco * quantidade)
        gasto=float(input('Quanto que você gastol com tudo: '))
        conta=math.ceil(quantidade * gasto)
        lucru= math.ceil(total_rendido - conta)
        produtos.append({
           'Produtos': produto,
           'Quantidade': quantidade,
           'Preço (R$)':preco,
           'Lucro (R$)': lucru
        })
        print('_'* 45)
except ValueError:
    print()
    print('Digite um valor ou quantidade do itens')
    print()

df=pd.DataFrame(produtos)

print(df)
print('_'* 45)
