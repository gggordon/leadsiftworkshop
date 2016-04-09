import nltk
from nltk.corpus import stopwords
from nltk.tokenize import RegexpTokenizer
from nltk.stem.snowball import SnowballStemmer
import random
from re import split

pathToFile='./nerualnetworkbook.txt'
pathToTempFile='./temp.txt'

print "Processsing"

fileContents = ""
with open(pathToFile,'r') as fileReader:
	fileContents = fileReader.read().decode('utf-8', 'ignore')

print "We read the file contents. Size %d bytes" % (len(fileContents))

tokenizer = RegexpTokenizer(r'[a-zA-Z]+')
words = tokenizer.tokenize(fileContents)
# print words

print "No. of words before prep : %d " % (  len(words) )



good_words  = []
#remove stopwords and numbers
for w in words:
	if w.lower() not in stopwords.words():
		if not w.isdigit():
		    good_words.append(w.lower())

print "No. of words without puctuation: %d" % ( len(good_words) )



stemmer = SnowballStemmer("english")

stemmed_words = [ stemmer.stem(w) for w in good_words  ]

print "No. of stemmed words : %d" % ( len(stemmed_words ) )

fdist = nltk.FreqDist(stemmed_words)

print "Top 50 Words"
print fdist.most_common(50)









#print words

