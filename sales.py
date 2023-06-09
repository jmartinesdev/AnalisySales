import pandas as pd
df = pd.read_excel('Sales.xlsx')

#df_A = df.iloc[:,2]
#print(df_A)

df['Final Value'] = df['Quantity'] * df['Single Price']
print(df)

"""
multiply the billing for the month of December 
"""
total_earning = df['Final Value'].sum()
print(f'The billing for the month of December is {total_earning}')

"""

"""