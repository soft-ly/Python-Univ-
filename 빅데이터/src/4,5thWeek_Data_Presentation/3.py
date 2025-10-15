import pandas as pd

col = ['col1', 'col2', 'col3']
row = ['row1', 'row2', 'row3', 'row4', 'row5']
data = [[1,2,3],[4,5,6],[7,8,9],[10,11,12],[13,14,15]]
df = pd.DataFrame(data, row, col)

s = pd.Series(data=[10,10,3,3,1], index=row)
print(df.sample(n=3, weights=s))
