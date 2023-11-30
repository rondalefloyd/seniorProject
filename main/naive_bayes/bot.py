from sklearn.feature_extraction.text import CountVectorizer 
from sklearn.naive_bayes import MultinomialNB

from pathlib import Path #for traversing directories

import pandas as pd #library for reading txt file i.e., csv
import os

from sklearn.model_selection import train_test_split

from sklearn.metrics import f1_score

open_csv = os.path.join(os.path.dirname(__file__), "..\\dataset\\Python_PS_Datasets.csv")

dataset = pd.read_csv(open_csv)

que_list = dataset["Question"]
solution = dataset["Answer"]
label = dataset["QuestionID"]


vectorizer = CountVectorizer()
nb_classifier = MultinomialNB()

# Split the data into training and testing sets
que_list_train, que_list_test, label_train, label_test = train_test_split(que_list, label)

training_data = vectorizer.fit_transform(que_list_train)
nb_classifier.fit(training_data, label_train)

# Evaluate the model on the testing data
testing_data = vectorizer.transform(que_list_test)
accuracy = nb_classifier.score(testing_data, label_test)
# print("Accuracy:", accuracy)

def get_answer_nb(user_input):
  user_input = vectorizer.transform([user_input])
  prediction = nb_classifier.predict(user_input)
  return solution[prediction[0]]

# def predict_answer(user_input):
#   user_input = vectorizer.transform([user_input])
#   prediction = nb_classifier.predict(user_input)
#   probabilities = nb_classifier.predict_proba(user_input)[0]
#   max_prob = max(probabilities)
#   prediction_score = round(max_prob*100, 2)
#   print(f"The predicted class is {prediction} with a score of {prediction_score}%")
#   return prediction[0]

# user = "start bot"

# while user != "bye":
#     # Testing the chatbot       
#     print("Me: ", end = "")
#     user_input = input()

#     print("\nBot: ", ans_list[predict_answer(user_input)])


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

