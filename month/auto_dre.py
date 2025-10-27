import pandas as pd

#Ask for month and add it in the column month of RESUMO DESPESAS and RESUMO RECEITAS
month=input('Enter the month: ')

df_expenses=pd.read_excel(
	'CONTROLE DIÁRIO - teste.xlsx', sheet_name='RESUMO DESPESAS'
)

df_revenue=pd.read_excel(
    'CONTROLE DIÁRIO - teste.xlsx', sheet_name='RESUMO RECEITAS'                         
)

df_expenses['MES'], df_revenue['MES']=month, month

with pd.ExcelWriter(						# File Handle to write on the file.
	'CONTROLE DIÁRIO - teste.xlsx',         
	engine='openpyxl',
	mode='a',                              	# 'a' append: add things to the file.
	if_sheet_exists='replace'              	# Substitutes the sheet if already exists.
) as writer:
    df_expenses.to_excel(writer, sheet_name='RESUMO DESPESAS', index=False)
    df_revenue.to_excel(writer, sheet_name='RESUMO RECEITAS', index=False)

month_valE=pd.read_excel(
	'CONTROLE DIÁRIO - teste.xlsx', sheet_name='RESUMO DESPESAS'
)

month_valR=pd.read_excel(
    'CONTROLE DIÁRIO - teste.xlsx', sheet_name='RESUMO RECEITAS'                         
)

month_in_exp=month_valE['MES']
month_in_rev=month_valR['MES']

# Dump

print(f'Content of column month in RESUMO DESPESAS: {month_in_exp}\n')
print(f'Content of column month in RESUMO RECEITAS: {month_in_exp}\n')
   


