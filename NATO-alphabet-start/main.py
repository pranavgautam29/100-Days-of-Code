import pandas as pd

data = pd.read_csv("nato.csv")
data_dict = {row.letter:row.code for (index,row) in data.iterrows()}
user_input = input("Enter a word:").upper()
new_l = [data_dict[letter] for letter in user_input]
print(new_l)

