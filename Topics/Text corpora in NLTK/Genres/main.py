import nltk
from nltk.corpus import brown

# nltk.download('brown')

# ask the user to input a category
category = input()

# load the corpus and select the specified category
corpus = brown

if category not in corpus.categories():
    print(f"Category '{category}' not found in the Brown corpus.")
    exit()

documents = corpus.fileids(categories=category)

# print the names of the first three documents
if len(documents) < 3:
    print(f"The '{category}' category has less than 3 documents.")
else:
    print(documents[:3])
