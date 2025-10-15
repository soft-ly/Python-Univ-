#apriori algorithm

import pandas as pd
from mlxtend.preprocessing import TransactionEncoder
from mlxtend.frequent_patterns import apriori, association_rules, fpgrowth

f = open("store_data.csv", "r")

temp_data = f.read().splitlines()

data = []

data = [[item.strip() for item in line.split(',')] for line in temp_data]

print(data)

te = TransactionEncoder()
te_ary = te.fit(data).transform(data)
df = pd.DataFrame(te_ary, columns=te.columns_)
print(df)

result = apriori(df, min_support=0.1, use_colnames=True)
print(result)

result = fpgrowth(df, min_support=0.1, use_colnames=True)
print(result)

result_chart = association_rules(result)
print(result_chart)