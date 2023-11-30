from pathlib import Path #for traversing directories

import os
import csv

import pandas as pd #library for reading txt file i.e., csv

os.chdir('../')
dataset_folder = Path("dataset/DTree/")


open_csv = dataset_folder / "Python ProblemSolution Datasets.csv"

data = pd.read_csv(open_csv, encoding = 'utf-8')

problem_list = data["Problem"]
python_code_list = data["Python Code"]


# for i in range(len(python_code_list)):
#     print("\nrow:", i, "\n",python_code_list[i])

def genID(problem):
    problem_id = []
    for i in range(len(problem)):
        problem_id.append("problem_" + str(i))
    
    return problem_id

def to_CSV(problem_id, problem_list, python_code_list):
    df = pd.DataFrame({"Problem": problem_list, "Solution": python_code_list})
    data_test = df.assign(ProblemID = problem_id)
    data_test.to_csv("dataset/DTree/Python_PS_Datasets.csv", encoding='utf-8', index=False)



to_CSV(genID(problem_list), problem_list, python_code_list)