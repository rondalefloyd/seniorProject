from pathlib import Path #for traversing directories

import pandas as pd #library for reading txt file i.e., csv
import numpy as np
import os

import nltk
import string
os.chdir('../')
dataset_folder = Path("dataset/NB/")

open_csv = dataset_folder / "Python Datasets.csv"

question_list = pd.read_csv(open_csv, encoding = 'latin-1')

sample = []
sample.append(question_list["Problem"][0])
sample.append(question_list["Problem"][1])
def tokenize(sentence):
    return nltk.word_tokenize(sentence)

def normalize_case(sentence):
    return sentence.lower()

def remove_punctation(sentence):
    removed_punctuation = []
    for word in sentence:
        if word not in string.punctuation:
            removed_punctuation.append(word)
    return removed_punctuation
    # return sentence.translate(str.maketrans('', '', string.punctuation))

# tok_sen = tokenize(sample)
# norm_sen = [normalize_case(word) for word in tok_sen]
# rem_sen = remove_punctation(norm_sen)

# print(rem_sen)
