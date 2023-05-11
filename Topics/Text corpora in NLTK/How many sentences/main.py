import nltk
from nltk.corpus import gutenberg

# nltk.download('gutenberg')

name = (input())

if name in gutenberg.fileids():
    # Получение книги  name из корпуса gutenberg
    sents = gutenberg.sents(name)

    # # Получение первых 5 предложений из книги
    # print(sents[:5])
    #
    # # Применение функции sent_tokenize() для извлечения предложений
    # for sentence in sents[:5]:
    #     print(nltk.sent_tokenize(' '.join(sentence)))

    print(len(sents))

