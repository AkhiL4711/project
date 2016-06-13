import nltk
from nltk import word_tokenize

query = "jdkf"
tokend_query = word_tokenize(query)
pos_query = nltk.pos_tag(query, "universal")

new_query = []

no_of_words = len(tokend_query)
for i in range(no_of_words):
    if pos_query[i][1] == "NOUN":
        new_query.append(pos_query[i][0])
