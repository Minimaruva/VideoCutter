import pandas as pd
import random

quotes_df = pd.read_csv("./assets/filtered_data.csv", sep=";")

random_row = random.randint(1, len(quotes_df))

quote = quotes_df.loc[random_row]["QUOTE"]
# print(quotes_df.head())
# print(quotes_df.iloc[[random_row]])
# print(quote)
