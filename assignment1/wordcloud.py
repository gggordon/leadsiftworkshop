from sklearn.feature_extraction.text import TfidfVectorizer
import numpy as np

fileContents = ""
with open('./temp.txt','r') as fileReader:
	fileContents = fileReader.read().decode('utf-8', 'ignore')


fileContents= np.array(fileContents.split(' '))

vectorizer = TfidfVectorizer(min_df=1)
print vectorizer.fit_transform(fileContents)