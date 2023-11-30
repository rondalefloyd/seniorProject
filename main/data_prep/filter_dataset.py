from pathlib import Path #for traversing directories

import pandas as pd #library for reading txt file i.e., csv
import numpy as np

import re #library for removing html tags
import os
import time

os.chdir('../')
dataset_folder = Path("dataset/NB/")

open_questions = dataset_folder / "Questions.csv"

open_answers = dataset_folder / "Answers.csv"

data_limiter = 20000 # to limit how much data/rows we want to read

question_list = pd.read_csv(open_questions, encoding = 'latin-1')  #raw size: 607282
answer_list = pd.read_csv(open_answers, encoding = 'latin-1', nrows = data_limiter) #raw size: 987122

def filter_answer(cat_ans):
    print("\nFiltering Answer...")
    cat_ans.sort_values(by=['ParentId','Score'], ascending=[True, True], inplace=True)
    cat_ans.reset_index(drop=True, inplace=True)

    starting_point = cat_ans['ParentId'][0]


    filtered_id = []
    highest_score = []
    filtered_ans = []

    for idx, i in enumerate(cat_ans["ParentId"]):
        if idx < len(cat_ans)-1:
            if i != cat_ans["ParentId"][idx+1]:
                filtered_id.append(cat_ans["ParentId"][idx])
                highest_score.append(cat_ans["Score"][idx])
                filtered_ans.append(cat_ans["Body"][idx])
    

    dict = {'ParentId': filtered_id, 'Score': highest_score, 'Body': filtered_ans}    

    df = pd.DataFrame(dict)
    df.to_csv("dataset/NB/Filtered_Answer.csv", encoding='utf-8', errors='surrogatepass')
    print("Before: ", len(cat_ans), " || After: ", len(filtered_ans))
    print("'Filtered_Answer.csv' Saved!\n")

def fetch_all_question_with_answer(question_list, answer_list):
    que_list = []
    ans_list = []
    id_list = []
    lablel_list =[]

    for idx, i in enumerate(answer_list["ParentId"]):
        w_ans = False
        for idy, x in enumerate(question_list["Id"]):
            if i == x:
                # que_list.append(question_list["Title"][idy] + question_list["Body"][idy])
                que_list.append(question_list["Title"][idy])
                ans_list.append(answer_list["Body"][idx])
                id_list.append(x)
                w_ans = True
                break
        lablel_list.append(idx)
        print("\rFetching Question: ", idx+1, '/', len(answer_list),end="")
    print("\n", end="")

    cleaned_que_list = [noiseRemoval(w) for w in que_list]
    cleaned_ans_list = [noiseRemoval(w) for w in ans_list]

    dict = {'Label': lablel_list, 'Id': id_list, 'Problem': cleaned_que_list, 'Solution': cleaned_ans_list}    

    df = pd.DataFrame(dict)

    df.to_csv("dataset/NB/Python Dataset.csv", encoding='utf-8', errors='surrogatepass', index=False)
    
    print("'Python Dataset.csv' Saved!\n")

#removal of html tags
cleantext = re.compile('<.*?>') #detecting html tags
def noiseRemoval(raw_data):
    return re.sub(cleantext, '', raw_data) 


# Fist step is to filter all answers by selecting just one answer with the highest score
filter_answer(answer_list)


# Second step is to fetch all the questions with their corresponding answers then save it into new csv file
open_f_answers = dataset_folder / "Filtered_Answer(smol).csv"
f_answer_list = pd.read_csv(open_f_answers, encoding = 'latin-1')

fetch_all_question_with_answer(question_list, f_answer_list)
print("Done!")
