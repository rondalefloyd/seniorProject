import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split


from pathlib import Path #for traversing directories
import os

from sklearn.feature_extraction.text import CountVectorizer 

from sklearn.metrics import f1_score

open_csv = os.path.join(os.path.dirname(__file__), "..\\dataset\\Python_PS_Datasets.csv")

# Load the dataset containing Python problems and their solutions
data = pd.read_csv(open_csv)


# Initialize the CountVectorizer
vectorizer = CountVectorizer()

# Split the data into features and target
features = vectorizer.fit_transform(data['Question'])
target = data["QuestionID"]
solution = data["Answer"]

# Split the data into training and testing sets
features_train, features_test, target_train, target_test = train_test_split(features, target)


# Train the decision tree classifier
clf = DecisionTreeClassifier()
clf.fit(features_train, target_train)

# Evaluate the model on the test data
accuracy = clf.score(features_test, target_test)

# Implement the query bot
def get_answer_dtree(input):
    user_input = vectorizer.transform([input])
    prediction = clf.predict([user_input.toarray()[0]])
    return solution[prediction[0]]

def predict_label(input):
    user_input = vectorizer.transform([input])
    prediction = clf.predict([user_input.toarray()[0]])
    return prediction[0]

# user = "start bot"

# while user != "bye":
#     # Testing the chatbot       
#     print("Me: ", end = "")
#     user = input()

#     print("\nBot: ", get_answer_dtree(user))
    
# test_data = ["Write a NumPy program to repeat elements of an array.", "Write a NumPy program to create a vector with values from 0 to 20 and change the sign of the numbers in the range from 9 to 15.",
#             "Write a Python program to All pair combinations of 2 tuples,", "Getting Unique values from a column in Pandas dataframe in Python",
#             "Convert the column type from string to datetime format in Pandas dataframe in Python"]
# true_labels = [0, 1544, 1746, 1843,2031]

# predicted_labels = []
# for input in test_data:
#   prediction = predict_label(input)
#   predicted_labels.append(prediction)

# # compute F1 score
# f1 = f1_score(true_labels, predicted_labels, average='weighted')
# print("F1 score: ", f1)