# Don't download treebank. Just import it
import nltk
from nltk.corpus import treebank

# nltk.download("treebank")

number = int(input()) # a row number of a sentence in Treebank corpus
print(treebank.parsed_sents()[number])

# or
# print(__import__('nltk').corpus.treebank.parsed_sents()[int(input())])