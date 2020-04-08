df = pandas.DataFrame({"City": ["chicagoo", "Chicago", "Chiccago"]})
print(df.head())

import pandas

from RookiePackage.my_mod import preprocess_city

df = preprocess_city(df)
print(df.head)
