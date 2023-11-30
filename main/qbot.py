import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QTextEdit, QVBoxLayout, QHBoxLayout, QPushButton, QTabWidget

from naive_bayes.bot import get_answer_nb
from decision_tree.bot import get_answer_dtree
from NB_Tree.bot import get_answer_nbtree

import textwrap
import html


class ChatbotWindow(QWidget):
    def __init__(self, algorithm):
        super().__init__()

        # Store the algorithm type as an instance variable
        self.algorithm = algorithm

        # Create a QTextEdit for displaying chat history
        self.chat_history = QTextEdit()
        self.chat_history.setReadOnly(True)
        
        # Create a QTextEdit for entering new messages
        self.message_input = QTextEdit()
        self.message_input.setMaximumHeight(25)
        
        # Create a send button
        self.send_button = QPushButton('Send')
        self.send_button.clicked.connect(self.send_message)
        self.send_button.setFixedSize(50, 25)
        
        
        # Create a layout for the chat window
        main_layout = QVBoxLayout()
        main_layout.addWidget(self.chat_history)
        
        # Add the message input field and send button to a horizontal layout
        input_layout = QHBoxLayout()
        input_layout.addWidget(self.message_input)
        input_layout.addWidget(self.send_button)
        
        # Add the input layout to the main layout
        main_layout.addLayout(input_layout)
        
        # Set the main layout for the window
        self.setLayout(main_layout)

    def send_message(self):
        # Get the message text and clear the message input
        message = self.message_input.toPlainText()
        
        self.message_input.clear()
        
        # Apply CSS attributes to HTML tags/classes
        message_style = """
        <style>
        .user {
        
        }
        .chatbot {
        
        }
        .user td {
            padding: 5px;
            background-color: lightgreen;
        }
        .chatbot td {
            padding: 5px;
            background-color: lightblue;
        }
        .user th {
            text-align: left;
            color: #999999;
            font-weight: 100;
            font-size: 10px;
        }
        .chatbot th {
            text-align: left;
            color: #999999;
            font-weight: 100;
            font-size: 10px;
        }
        </style>
        """

       # Append the message to the chat history
        self.chat_history.append(message_style + "<table class='user'><tr><th>User</th></tr><tr><td>" + message + "</td></tr></table>")
        
        # Send the message to the chatbot and get the response
        response = self.get_response(message)

        algorithm = self.get_name(message)

        res_html = response.replace('\n', '<br>').replace('\t', '&nbsp;&nbsp;&nbsp;&nbsp;')

        self.chat_history.append(message_style + "<table class='chatbot'><tr><th>" + algorithm + "</th></tr><tr><td>" + res_html + "</td></tr></table>")
        
    def get_name(self, name):
        # Apply the name of the chatbot based on the specified algorithm
        if self.algorithm == 'algorithm1':
            return "Algorithm 1"
        elif self.algorithm == 'algorithm2':
            return "Algorithm 2"
        elif self.algorithm == 'algorithm3':
            return "Algorithm 3"

    def get_response(self, message):
    # Implement the logic for your chatbot based on the specified algorithm
        if self.algorithm == 'algorithm1':
        # Implement algorithm 1 here
            response = get_answer_nb(message)
        elif self.algorithm == 'algorithm2':
        Implement algorithm 2 here
            response = get_answer_dtree(message)
        elif self.algorithm == 'algorithm3':
        Implement algorithm 3 here
            response = get_answer_nbtree(message)
        Check if the response is None, and if so, return an empty string
        if response is None:
            response = ''
        return response


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        # Create three instances of ChatbotWindow with different algorithms
        chatbot_1 = ChatbotWindow('algorithm1')
        chatbot_2 = ChatbotWindow('algorithm2')
        chatbot_3 = ChatbotWindow('algorithm3')

        # Create a horizontal layout to hold the three chatbot widgets
        chatbots_layout = QHBoxLayout()
        chatbots_layout.addWidget(chatbot_1)
        chatbots_layout.addWidget(chatbot_2)
        chatbots_layout.addWidget(chatbot_3)

        # Set the layout for the main window
        self.setLayout(chatbots_layout)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
