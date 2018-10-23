import pandas as pd
from datetime import datetime
file = 'trial.xlsx'
xl = pd.ExcelFile(file)
dfs = xl.parse(xl.sheet_names[0])
dfs = list(dfs['Timeline'])
#print(dfs)
date = datetime(2016, 3, 10)
for x in range(len(dfs)):
    print(type(x))
    if type(dfs[x]) == type(date):
        dfs.remove(dfs[x])
print(dfs)
list2 = [date]
print(type(list2[0]))
