import pandas as pd 
s = pd.Series([3, -5, 7, 4], index=['a', 'b', 'c', 'd'])
data = {'Country': ['Belgium', 'India', 'Brazil'],
'Capital': ['Brussels', 'New Delhi', 'Brasília'],
'Population': [11190846, 1303171035, 207847528]}
df = pd.DataFrame(data,
columns=['Country', 'Capital', 'Population'])

s=s.drop(['a', 'c'])
print(s)
df=df.drop('Country', axis=1)
print(df)
'''Output
b   -5
d    4
dtype: int64
     Capital  Population
0   Brussels    11190846
1  New Delhi  1303171035
2   Brasília   207847528
'''