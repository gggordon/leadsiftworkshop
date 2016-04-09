# ggordon
# assignment1
# created 1.4.2016

from sklearn.feature_extraction.text import TfidfVectorizer

pathToFile='./nerualnetworkbook.txt'

fileContents = ""
with open(pathToFile,'r') as fileReader:
	fileContents = fileReader.read().decode('utf-8', 'ignore')

#fileContents = fileContents.translate(string.punctuation)

vectorizer = TfidfVectorizer(input = fileContents, \
	strip_accents='unicode',\
	stop_words='english',\
	analyzer='word',\
	ngram_range=(1,10),\
	token_pattern='[a-zA-Z]+',\
	max_features=50)

content = fileContents.split('.')
print "="*32
print """A Brief Introduction to
Neural Networks
David Kriesel
dkriesel.com
Download location:
http://www.dkriesel.com/en/science/neural_networks
NEW - for the programmers:
Scalable and efficient NN framework, written in JAVA
http://www.dkriesel.com/en/tech/snipe"""
print "="*32
print "No of sentences : %d" % len(content)
print "="*32

tf_idf= vectorizer.fit_transform(content)
feature_names = vectorizer.get_feature_names()

tokenDict = {};
print "="*32
print "==== Most Meaningful Terms =====" 
print "   Term   -   TF-IDF Weight"
print "="*32
for col in tf_idf.nonzero()[1]:
	if feature_names[col] not in tokenDict:
		tokenDict[feature_names[col]] = tf_idf[0,col]
		print feature_names[col],' - ',tf_idf[0,col]
print "="*32