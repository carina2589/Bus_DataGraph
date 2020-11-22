import pandas as pd

df = pd.read_csv("/Users/amitcharran/Desktop/weekend.csv")

# print(df)

df.set_index("0-1")

print(df.loc[0:6,"0-1":"5-6"])

# gets an entire column
print(df.loc[:, "5-6"])

# also get entire column
print(df["5-6"])


# get row
print(df.loc[1,:])

# get row
print(df.iloc[0, 4])
