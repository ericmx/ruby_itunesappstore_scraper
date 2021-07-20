import sklearn
import pandas as pd
import numpy as np

dfRating = pd.read_csv('rating.txt', header = 0, delimiter = "\n")
dfReview = pd.read_csv('reviews.txt', header = None ,delimiter = ",")

del dfReview[1]
dfReview.columns = ['review']
dfReview.head()
dfRating.head()

dfReview = dfReview.apply(lambda x: x.astype(str).str.lower())
dfReview = dfReview.replace('\d+', '', regex = True)
dfReview = dfReview.replace('[^\w\s\+]', '', regex = True)

dfReview.head()

allData = pd.concat([dfRating, dfReview], axis=1, ignore_index=True)
allData.columns = ['rating', 'review']
train.dropna(axis = 0, how = 'any', inplace = True)
train.reset_index(inplace=True)

allData.to_csv('all_data.txt', index = False)
