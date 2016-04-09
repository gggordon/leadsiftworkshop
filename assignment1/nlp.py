
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

# [(u'neuron', 918), (u'network', 686), (u'learn', 511), (u'function', 476), (u'input', 436), (u'output', 317), (u'weight', 307), (u'train', 306), (u'one', 304), (u'valu', 303), (u'p', 285), (u'use', 282), (u'activ', 236), (u'neural', 236), (u'layer', 234), (u'time', 222), (u'h', 210), (u'two', 185), (u'state', 173), (u'k', 168), (u'mean', 168), (u'error', 168), (u'pattern', 166), (u'x', 163), (u'differ', 157), (u'chang', 152), (u'process', 149), (u'definit', 147), (u'vector', 143), (u'set', 140), (u'see', 139), (u'connect', 138), (u'gfed', 134), (u'abc', 133), (u'inform', 132), (u'space', 128), (u'system', 125), (u'problem', 125), (u'perceptron', 124), (u'thus', 124), (u'exampl', 124), (u'rule', 121), (u'rbf', 116), (u'result', 114), (u'possibl', 114), (u'point', 112), (u'cluster', 111), (u'fig', 110), (u'step', 110), (u'would', 108)]









#print words

