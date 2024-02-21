import pandas as pd 


# Bring csv into a variable, df
df = pd.read_csv('electric_cars.csv')

# Print top 10 records
print()
print('ORIGINAL DATAFRAME\t///////////////////////')
print()
print (df.head(10))


df_thin = df[['Name', 'Subtitle', 'Range', 'Drive', 'Price']]

# Change column formats
for i in range(len(df_thin)):

    # Subtitle reformat
    df_thin.loc[i,'Subtitle'] = float(df_thin.loc[i,'Subtitle'].replace('Battery Electric Vehicle |       ','').replace(' kWh',''))

    # Range reformat, convert km into miles
    df_thin.loc[i,'Range'] = float(df_thin.loc[i,'Range'].replace(' km','')) * 0.621371

    # Price reformat
    df_thin.loc[i,'Price'] = float(df_thin.loc[i,'Price'])

# Renaming column names
df_thin = df_thin.rename(columns={'Subtitle':'BatterySize (kWh)','Range':'Miles','Price':'Price ($)'})

print()
print('FORMATTED DATAFRAME\t///////////////////////')
print()
print(df_thin.head())

# Sort values by Price, lowest to highest
df_thin = df_thin.sort_values(by='Price ($)',ascending=True)
# Limit rows
df_cheap = df_thin.head(5)

# Sort values by Price, highest to lowest, and limit rows
df_exp = df_thin.sort_values(by='Price ($)',ascending=False).head(5)

print()
print('ROW LIMITED DATAFRAME\t///////////////////////')
print()
print('Cheap')
print(df_cheap)
print()
print('Expensive')
print(df_exp)

# Finding average values
drive_grouped = df_thin[['Drive','Price ($)']].groupby(['Drive'])
df_drive_average_sales = drive_grouped.mean()

print()
print('AGGREGATED DATAFRAME\t///////////////////////')
print()
print(df_drive_average_sales)

# Unpivot Record to change data from horizontal to vertical
df_single = df_cheap.head(1)
df_unpivot = df_single.unstack().rename_axis(['Category','Row']).reset_index().drop(columns='Row').rename({0:'Value'}, axis=1)

print()
print('UNPIVOTED DATAFRAME\t///////////////////////')
print()
print(df_unpivot)


