import pandas as pd

data = {
    "Name": ["Echezona", "Blessing", "Jennifer"],
    "Score": [80, 45, 72]
}

df = pd.DataFrame(data)
df_head = df.head()
df_shape = df.shape
df_desc = df.describe()

print(df)
print(df_head)
print(df_shape)
print(df_desc)