#apriori algorithm

import pandas as pd
from mlxtend.preprocessing import TransactionEncoder
from mlxtend.frequent_patterns import apriori, association_rules

data = [['우유', '기저귀', '쥬스'],
        ['상추', '기저귀', '맥주'],
        ['우유', '양상추', '기저귀', '맥주'],
        ['양상추', '맥주']]

te = TransactionEncoder()
te_ary = te.fit(data).transform(data)
df = pd.DataFrame(te_ary, columns=te.columns_)
print(df)

result = apriori(df, min_support=0.5, use_colnames=True)
print(result)

result_chart = association_rules(result, metric = "confidence", min_threshold=0.5)
print(result_chart)