#%% Código do Lira do Hashtag Programação
# https://www.youtube.com/watch?v=GQpQha2Mfpg

import pandas as pd
from twilio.rest import Client


# Your Account SID from twilio.com/console
account_sid = "AC64853a58b230afba7c8fc59f0bea16a1"
# Your Auth Token from twilio.com/console
auth_token  = "b31fe4fd4a83f5535cf9386ffd4631d3"
client = Client(account_sid, auth_token)

# Abrir os 6 arquivos em Excel
lista_meses = ['janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho']

for mes in lista_meses:
    tabela_vendas = pd.read_excel(f'{mes}.xlsx')
    if (tabela_vendas['Vendas'] > 55000).any():
        vendedor = tabela_vendas.loc[tabela_vendas['Vendas'] > 55000, 'Vendedor'].values[0]
        vendas = tabela_vendas.loc[tabela_vendas['Vendas'] > 55000, 'Vendas'].values[0]
        print(f'No mês {mes} alguém bateu a meta. Vendedor: {vendedor}, Vendas: {vendas}')
        message = client.messages.create(
            to="+5511971708899",
            from_="+12294904413",
            body=f'Notificação da Sandy. No mes {mes} alguem bateu a meta. Vendedor: {vendedor}, Vendas: {vendas}.')
        print(message.sid)


# Para cada arquivo:

# Verificar se algum valor na coluna Vendas daquele arquivo é maior que 55.000

# Se for maior do que 55.000 -> Envia um SMS com o Nome, o mês e as vendas do vendedor

# Caso não seja maior do que 55.000 não quero fazer nada
