import pandas as pd 

# Brodie's Code!

# bring in the dataset and print out the first 10 records
df = pd.read_csv('cars.csv')

print()
print('ORGINAL DATAFRAME\t////////////////////////////')
print()
print (df.head(10))

# limit the columns to the following: mpg, hp, weightlbs, year, brand
df_thin = df[['mpg', 'hp', 'weightlbs', 'year', 'brand']]

for i in range(len(df_thin)):

    # remove the period from the end of the brand
    df_thin.loc[i,'brand'] = df_thin.loc[i,'brand'].replace('.','')


    # convert mpg, hp and weightlbs to numbers (use float()), leave the year as text
    # I encountered nulls in weightlbs that I could not figure out, so I replaced all nulls with '0'
    df_thin.loc[i,'mpg'] = float(df_thin.loc[i,'mpg'])
    df_thin.loc[i,'hp'] = float(df_thin.loc[i,'hp'])
    df_thin.loc[i,'weightlbs'] = float(df_thin.loc[i,'weightlbs'].replace(' ','0'))

# rename the columns
    # mpg to miles per gallon
    # hp to horsepower
    # weightlbs to weight (lbs)
    # brand to country
df_thin = df_thin.rename(columns={'mpg':'miles per gallon','hp':'horsepower','weightlbs':'weight (lbs)','brand':'country'})

# print out the first 10 records
print()
print('REFORMATTED DATAFRAME\t////////////////////////////')
print()
print(df_thin.head(10))

# print out the top 5 records with the lowest weight
df_light = df_thin.sort_values(by='weight (lbs)',ascending=True).head(5)

# print out the top 5 records with the highest weight
df_heavy = df_thin.sort_values(by='weight (lbs)',ascending=False).head(5)

print()
print('SORTED DATAFRAME\t////////////////////////////')
print()
print('Light')
print(df_light)
print()
print('Heavy')
print(df_heavy)

# take a subset of the following columns: country (previously brand) and horsepower (previously hp)
df_subset = df_thin[['country','horsepower']]

# group records by country
country_grouped = df_subset.groupby(['country'])

# use the mean function on the grouped records
df_country_average_hp = country_grouped.mean()

# print out the first 10 records
print()
print('AGGREGATED DATAFRAME\t////////////////////////////')
print()
print(df_country_average_hp.head(10))


# make a new dataframe with the first record in the dataset
df_single = df_heavy.head(1)

# use the line of code from the participation to make a dataframe that is "unpivoted" (meaning columns turned into rows)
df_unpivot = df_single.unstack().rename_axis(['Category','Row']).reset_index().drop(columns='Row').rename({0:'Value'}, axis=1)

print()
print('UNPIVOTED DATAFRAME\t////////////////////////////')
print()
print(df_unpivot)

# print out the entire dataframe


