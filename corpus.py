import nltk
import os
from pyuca import Collator
import codecs 

c = Collator("allkeys.txt")

corpusdir = './data/' # Directory of corpus.
files = [ fname for fname in os.listdir(corpusdir)]

# separa em linhas
stok = nltk.data.load('tokenizers/punkt/portuguese.pickle')

for f in files:
    fileObj = codecs.open("%s%s" % (corpusdir, f), "r", "utf-8" )
    mikrofesto = fileObj.read() 
    print mikrofesto
    catalinhas=stok.tokenize(mikrofesto)
    print catalinhas
