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
Analyze revenue by store and grouping the store to check the billing per shop
"""

billing_by_store = df[['Stores', 'Final Value']].groupby("Stores").sum()
print(f'This is the billing by each stores: {billing_by_store}')

"""
Group the Stores and Cards columns to discover the revenue for each store and then add the revenue for each product.
"""
billing_by_card = df[['Stores', 'Cards', 'Final Value']].groupby(['Stores', 'Cards']).sum()
print(billing_by_card)


