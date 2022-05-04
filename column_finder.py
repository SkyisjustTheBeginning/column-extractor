import pandas as pd
ids = []
filename = str(input("FILE NAME "))
column = str(input("COLUMN "))
handler = pd.read_csv(filename)
for content in handler[column]:
    print(content)
