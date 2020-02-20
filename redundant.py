import pandas as pd
file_name = "Ground_Truth.csv"
file_name_output = "New_ground_truth.csv"

df = pd.read_csv(file_name, sep="\t or ,")
df.drop_duplicates(subset=None, inplace=True)

df.to_csv(file_name_output)