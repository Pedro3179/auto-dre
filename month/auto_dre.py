import pandas as pd

# Ask for the file name.
file_name=input('Enter the Daily Financial Report file (file.extension): ')

if __name__=='__main__':
# Ask for the month and add it to the "MES" column of RESUMO DESPESAS and RESUMO RECEITAS.
	month=input('Enter the month: ')

	df_expenses=pd.read_excel(
		file_name, sheet_name='RESUMO DESPESAS'
	)

	df_revenue=pd.read_excel(
		file_name, sheet_name='RESUMO RECEITAS'                         
	)

	df_expenses['MES'], df_revenue['MES']=month, month

	with pd.ExcelWriter(						# File Handle used to write to the file.
		file_name,         
		engine='openpyxl',
		mode='a',                              	# 'a' append: add data to the file.
		if_sheet_exists='replace'              	# Replace the sheet if it already exists.
	) as writer:
		df_expenses.to_excel(writer, sheet_name='RESUMO DESPESAS', index=False)
		df_revenue.to_excel(writer, sheet_name='RESUMO RECEITAS', index=False)

	month_valE=pd.read_excel(
		file_name, sheet_name='RESUMO DESPESAS'
	)

	month_valR=pd.read_excel(
		file_name, sheet_name='RESUMO RECEITAS'                         
	)

	month_in_exp=month_valE['MES']
	month_in_rev=month_valR['MES']

	# Display some data.

	print(f'Content of column month in RESUMO DESPESAS: {month_in_exp}\n')
	print(f'Content of column month in RESUMO RECEITAS: {month_in_rev}\n')
	


