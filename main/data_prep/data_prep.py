from pathlib import Path #for traversing directories

import os
import csv

import spacy
import pytextrank

from collections import Counter
from string import punctuation

import pandas as pd #library for reading txt file i.e., csv
import en_core_web_sm

nlp = en_core_web_sm.load()
nlp.add_pipe("textrank")

os.chdir('../')
dataset_folder = Path("dataset/DTree/")

open_csv = dataset_folder / "Python_PS_Datasets.csv"

data = pd.read_csv(open_csv, encoding = 'utf-8', nrows = 100)

problem_id = data["ProblemID"]
question = data["Problem"]
python_code = data["Solution"]

def extractKeywords(nlp, text):
    doc = nlp(text)

    keywords = []

    for phrase in doc._.phrases[:10]:
        keywords.append(phrase.text)
    return keywords

def shuf(array):
    len_arr = len(array)
    shuffled_arr = []
    temp_arr = array

    for i in reversed(range(len_arr)):
        shuffled_arr.append(temp_arr) 
        if i > 0:
            temp = array[i-1]
            array[i-1] = array[len_arr-1]
            array[len_arr-1] = temp
        
        temp_arr = [x for i, x in enumerate(array) if i != len_arr -  1]

    return shuffled_arr

def toCSV_raw(value, question):
    df = pd.DataFrame(value)
    data_test = df.assign(problem = question)
    data_test.to_csv("dataset/DTree/Grouped(raw).csv", encoding='utf-8', index=False, header = False)

l_keywords = []

for x in question:
    keywords = extractKeywords(nlp, x)
    l_keywords.append(keywords)

nkey = [shuf(x) for x in l_keywords]

main_prob = []
main_que = []
list_que = []
list_prob = []

smallest_group = 5
index = 0
removed_count = 0
rm = 0

for i in range(len(nkey)):
    for x in range(len(nkey[i])):
        if len(nkey[i]) >= 4:
            list_que.append(problem_id[i])   
            list_prob.append(nkey[i][x])
        if len(nkey[i]) < smallest_group:
            smallest_group = len(nkey[i])
            index = i
            prob = nkey[i][0]
        # if x == :
        #     break
    if len(nkey[i]) <= 2:
            removed_count += 1
    else:
        rm += 1 
        main_prob.append(nkey[i]) 
        main_que.append(question[i])

# print("Size: ", smallest_group, " row: ", index)
# print("Problem: ", question[index] , "\nKeywords: " , prob)

# print("Total of removed question: ",  removed_count)
# print("Remaing questions: ", rm)


# Saving extracted keywords to a csv file
toCSV_raw(list_prob, list_que)

def dataTrans(word, value, question):
    df = pd.DataFrame(value, columns = word)
    data_test = df.assign(problem = question)
    data_test.to_csv("dataset/DTree/DTree.csv", encoding='utf-8', index=False)

def getFirstIndex(question_array):
    keywords = []
    for x in range(len(question_array)):
        keywords.append(question_array[x][0])

    return keywords_array

def getMainKeywords(keywords_array):
    keywords = []
    for x in range(len(keywords_array)):
        for i in range(len(keywords_array[x])):
            keywords.append(keywords_array[x][i])
    return keywords


def  getValuePerRow(problem_array, header):
    valRow = []

    for sen in problem_array:
        valForRow = [0] * len(header)
        for w in sen:
            for i, x in enumerate(header):
                if w == x:
                    valForRow[i] = 1
        valRow.append(valForRow)
    return valRow

header = sorted(set(getMainKeywords(l_keywords)))
valRow = getValuePerRow(list_prob, header)
mainkey = getValuePerRow(main_prob, header)

nvalRow = []
nlist_que = []
nmainkey = []
nmain_que = []

for i in range(6):
    nmainkey.extend(valRow)
    nmain_que.extend(list_que)

# Saving the transformed data into csv file
dataTrans(header,nmainkey, nmain_que)

