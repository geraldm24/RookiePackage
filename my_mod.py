# replace nulls with missing 
# make all strings lower case
def preprocess_city(X):
  X = X.copy()
  X = X.fillna('Missing')
  X["City"] = X["City"].str.lower()
  return X



