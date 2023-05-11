# Don't download movie_reviews. Just import it
import nltk
from nltk.corpus import movie_reviews

# nltk.download("movie_reviews")
#
# print(movie_reviews.categories())
# print(movie_reviews.words(categories='pos')[:10])

# номер строки предложения в корпусе обзоров фильмов
number = int(input())

# Загрузить корпус негативных отзывов о фильмах
neg_corpus = movie_reviews.fileids('neg')

# Получить предложение по указанному номеру строки из subcorpus
neg_sentence = movie_reviews.sents(fileids=neg_corpus)[number]

# Print out the negative sentence as a list of tokens
print(neg_sentence)
