import pandas as pd

shopA_silver = pd.read_csv('./data/silver/shopA_silver.csv').drop('Unnamed: 0', axis=1) 
# rename column
shopA_silver.rename(columns={'price': 'price_pixmania'}, inplace=True)               
shopB_silver = pd.read_csv('./data/silver/shopB_silver.csv').drop('Unnamed: 0', axis=1)
# rename column
shopB_silver.rename(columns={'price': 'price_idealo'}, inplace=True)
# merge the two dataframes on the series column
price_pulse_comparator = shopA_silver.merge(shopB_silver, on='series', how='inner').rename(columns={'link_x': 'link_ipixmania', 'link_y': 'link_idealo'})
# absolute difference between the two prices
price_pulse_comparator['price_diff'] = round(abs(price_pulse_comparator['price_pixmania'] - price_pulse_comparator['price_idealo']), 2)
# recommend the cheapest price
price_pulse_comparator['recomended_store'] = price_pulse_comparator.apply(lambda row: 'Pixmania' if row['price_pixmania'] < row['price_idealo'] else 'Idealo', axis=1)
# order the columns in this order ['series', 'price_pixmania', 'price_idealo', 'price_diff', 'recomended_store', 'link_ipixmania', 'link_idealo']]  
price_pulse_comparator = price_pulse_comparator[['series', 'price_pixmania', 'price_idealo', 'price_diff', 'recomended_store', 'link_ipixmania', 'link_idealo']] 
# save the dataframe to a csv file
price_pulse_comparator.to_csv('./data/gold/price_pulse_comparator.csv') 