import pandas as pd
import numpy as np
import win32com.client as win32

# importar dadaframe
df = pd.read_excel('Relatório On-line de Atividades 2021 - UAB_IFRO (respostas).xlsx')

#tabela_bolsista.rename(columns={'Identifique o mês de referência:':'MES REFERENCIA', 'Nome do(a) bolsista:':'NOME'})

# visualizar a base de dados
pd.set_option('display.max_columns', None)
print(df)

# Relatorio por bolsista
bolsistas = df[['Nome do(a) bolsista:', 'Identifique o mês de referência:']].groupby('Nome do(a) bolsista:').sum()
print(bolsistas)

#tabela_bolsista['Identifique o mês de referência:'].value_counts()

# quantidade de produtos vendidos por loja
#quantidade = tabela_vendas[['ID Loja', 'Quantidade']].groupby('ID Loja').sum()
#print(quantidade)

#print('-' * 50)
# ticket médio por produto em cada loja
#ticket_medio = (faturamento['Valor Final'] / quantidade['Quantidade']).to_frame()
#ticket_medio = ticket_medio.rename(columns={0: 'Ticket Médio'})
#print(ticket_medio)

# enviar um email com o relatório de Vendas
outlook = win32.Dispatch('outlook.application')
mail = outlook.CreateItem(0)
mail.To = 'rogerio.dosantos@ifpr.edu.br'
mail.Subject = 'Relatório de Boslsista Geral todos os Meses'
mail.HTMLBody = f'''
<p>Prezados,</p>

<p>Segue o Relatório de bolsistas por cada Mes.</p>

<p>Bolsistas Geral:</p>
{bolsistas.to_html(formatters={'Valor Final': 'R${:,.2f}'.format})}




<p>Qualquer dúvida estou à disposição.</p>

<p>Att.,</p>
<p>Prof. Rogerio Santos</p>
'''

mail.Send()

print('Email Enviado')
