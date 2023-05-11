import json
import math
import os
import re
from gensim.models.doc2vec import Doc2Vec, TaggedDocument
import pandas as pd

import nltk
# nltk.download('punkt')

from nltk.tokenize import word_tokenize


class ChatBot:
    def __init__(self, name):
        self.name = name
        self.file_path = os.path.join(os.getcwd(), 'jeopardy.json')
        self.inp_tokens = []
        self.corpus_tokens = []
        self.df_answers = None
        self.model = None

        self.get_corpus_file(self.file_path)
        self.get_answer_file(self.file_path)

    def __repr__(self):
        return "Hello! I'm " + self.name + ", a question answering bot " \
                                           "who knows answers to all the questions from the 'Jeopardy!' game."

    def get_corpus_file(self, file_path):
        # Parse the JSON object
        with open(file_path, 'r', encoding='utf-8') as f:
            for j_id, line in enumerate(json.load(f)):
                tokens = self.tokenize(line['question'])
                self.corpus_tokens.append(TaggedDocument(words=tokens, tags=[j_id]))


    def get_answer_file(self, file_path):
        # Parse the JSON object
        with open(file_path, 'r', encoding='utf-8') as fd:
            df = pd.json_normalize(json.loads(fd.read()))
            self.df_answers = df['answer']


    def process_input(self, inq):
        # Tokenize the text by words;
        self.inp_tokens = self.tokenize(inq)

    def delete_punct(self, sentence):
        # Remove the punctuation marks from the token list.
        sentence = [x for x in sentence if re.search(r'(\w|\d)+', x)]
        return sentence

    def tokenize(self, data):
        # Convert corpus and a user request to lowercase
        tokens = self.delete_punct(word_tokenize(str(data).lower()))
        return tokens

    def convert_to_lower(self, data):
        if isinstance(data, dict):
            # print("dict: ", data)
            return {k: self.convert_to_lower(v) for k, v in data.items()}
        elif isinstance(data, list):
            # print("list: ", data)
            return [self.convert_to_lower(v) for v in data]
        elif isinstance(data, str):
            return data.lower()
        else:
            return data

    def train_model(self):
        self.model = Doc2Vec(
            documents=self.corpus_tokens,
            vector_size=200,
            window=5,
            min_count=5,
            workers=4,
            epochs=15
        )
        # сохранение модели для дальнейшего использования
        self.model.save("my_doc2vec_model")
        # self.model = Doc2Vec.load("my_doc2vec_model")

    def get_most_similar_doc(self):
        inferred_vector = self.model.infer_vector(self.inp_tokens)
        sims = self.model.dv.most_similar([inferred_vector], topn=1)
        return sims[0]

    def print_tokens(self, tokens):
        print(tokens)

    def greet(self):
        print(self)  # load _repr__ meth

        # Train the Doc2Vec model using the preprocessed corpus;
        self.train_model()
        # print(self.corpus_tokens[14460])


        while True:
            print('Ask me something!')
            self.process_input(input())
            # Print result of tokenization for the user request
            # self.print_tokens(self.inp_tokens)
            print("Let's play!")
            topic_id, similarity_score = self.get_most_similar_doc()
            answer_for_question = self.df_answers[topic_id]
            print(f"I know this question: its number is {topic_id}. "
                  f"I'm {math.floor(100 * similarity_score)}% sure of this. \n"
                  f"The answer is {answer_for_question}.")

            again = input("Do you want to ask me again? (yes/no)\n")

            if again == "no":
                print("It was nice to play with you! Goodbye!")
                break


ChatBot("Znayka").greet()
