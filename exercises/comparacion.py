import pandas as pd
d1 = pd.read_csv("t1.csv", delimiter="|")
d2 = pd.read_csv("t2.csv", delimiter="|")

for col in d1.columns:
    if d1[col].dtype == "object":
        d1[col] = d1[col].replace("\s+", " ", regex=True).str.rstrip(" .").str.lstrip(" ")

for col in d2.columns:
    if d2[col].dtype == "object":
        d2[col] = d2[col].replace("\s+", " ", regex=True).str.rstrip(" .").str.lstrip(" ")


d1 = d1.loc[d1.Type == "table"]
d2 = d2.loc[d2.Type == "table"]

list(set(d1.Name.values) - set(d2.Name.values))