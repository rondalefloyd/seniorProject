import numpy as np
import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.naive_bayes import MultinomialNB
from sklearn.ensemble import VotingClassifier


from pathlib import Path #for traversing directories
import os

from sklearn.feature_extraction.text import CountVectorizer

from sklearn.metrics import f1_score

# os.chdir('../')
# dataset_folder = Path("dataset/")

# open_dtree_csv = dataset_folder / "Python_PS_Datasets.csv"

open_csv = os.path.join(os.path.dirname(__file__), "..\\dataset\\Python_PS_Datasets.csv")


# Load the data into a Pandas dataframe
df = pd.read_csv(open_csv, encoding="utf-8")

# Initialize the CountVectorizer
vectorizer = CountVectorizer()

solution = df["Answer"]

# Split the data into features (X) and target variable (y)
X = vectorizer.fit_transform(df['Question'])
y = df["QuestionID"]

np.random.seed(42)

# Train Decision Tree Classifier
dt = DecisionTreeClassifier()
dt.fit(X, y)

# Train Naive Bayes Classifier
nb = MultinomialNB()
nb.fit(X, y)

# Combine the models using VotingClassifier
voting = VotingClassifier(estimators=[('dt', dt), ('nb', nb)], voting='hard')
voting.fit(X, y)

# Function to predict the label of the given question
def predict_answer(input):
  input = vectorizer.transform([input])
  # print(query)
  prediction = voting.predict(input)[0]
  return prediction

def get_answer_nbtree(input):
  input = vectorizer.transform([input])
  prediction = voting.predict(input)[0]
  return solution[prediction]

# user = "start bot"

# while user != "bye":
#   # Testing the chatbot
#   print("Me: ", end = "")
#   user = input()
#   prediction = get_answer(user)
  # print("\nBot: ", prediction, "\n")


# test_data = ["Write a NumPy program to repeat elements of an array.", "Write a NumPy program to create a vector with values from 0 to 20 and change the sign of the numbers in the range from 9 to 15.",
#             "Write a Python program to All pair combinations of 2 tuples,", "Getting Unique values from a column in Pandas dataframe in Python",
#             "Convert the column type from string to datetime format in Pandas dataframe in Python"]
# true_labels = [0, 1544, 1746, 1843,2031]

# predicted_labels = []
# for input in test_data:
#   prediction = predict_answer(input)
#   predicted_labels.append(prediction)

# # compute F1 score
# f1 = f1_score(true_labels, predicted_labels, average='weighted')
# print("F1 score: ", f1)