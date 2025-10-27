

#ANTES DE CONTINUAR O PROJETO DE MERGE E COMMIT


import pandas as pd

#Add expenses to table DRE DESPESAS
df_expenses=pd.read_excel(
	'CONTROLE DIÁRIO - teste.xlsx', sheet_name='RESUMO DESPESAS'
)

df_dre_expenses=pd.read_excel(
    'DRE - DEMONSTRATIVO DE RESULTADO.xlsx', sheet_name='DRE DESPESAS'
)

df_total_expenses=pd.concat([df_dre_expenses, df_expenses], axis=0)

#Add revenue to table DRE RECEITAS
df_revenue=pd.read_excel(
    'CONTROLE DIÁRIO - teste.xlsx', sheet_name='RESUMO RECEITAS'                         
)

df_dre_revenue=pd.read_excel(
    'DRE - DEMONSTRATIVO DE RESULTADO.xlsx', sheet_name='DRE RECEITAS'
)

df_total_revenue=pd.concat([df_dre_revenue, df_revenue])

#Writing changes to DRE DEMONSTRATIVO
with pd.ExcelWriter(
    'DRE - DEMONSTRATIVO DE RESULTADO.xlsx',
    engine='openpyxl',
    mode='a',
    if_sheet_exists='replace'
) as writer:
    df_total_expenses.to_excel(
        writer, sheet_name='DRE DESPESAS', index=False
    )
    df_total_revenue.to_excel(
        writer, sheet_name='DRE RECEITAS', index=False
    )

expenses_total=pd.read_excel(
    'DRE - DEMONSTRATIVO DE RESULTADO.xlsx', sheet_name='DRE DESPESAS'
)

revenue_total=pd.read_excel(
    'DRE - DEMONSTRATIVO DE RESULTADO.xlsx', sheet_name='DRE RECEITAS'
)

# Dump the resulting tabular data
print(f'''\nRESUMO DESPESAS overall shape(rows/columns): {df_expenses.shape}
DRE DESPESAS overall shape(rows/columns): {df_dre_expenses.shape}\n''')
print(f'''Resulting table overall shape(rows/columns): {expenses_total.shape}\n
------------------------------------------------------------------\n''')

print(f'''RESUMO RECEITAS overall shape(rows/columns): {df_revenue.shape}
DRE DESPESAS overall shape(rows/columns): {df_dre_revenue.shape}\n''')
print(f'Resulting table overall shape(rows/columns): {revenue_total.shape}')




