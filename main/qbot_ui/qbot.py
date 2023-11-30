import sys
import os
from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
from PyQt6.QtGui import *


class ChatBotUI(QMainWindow):
    def __init__(self):
        super().__init__()

        script_path = os.path.dirname(os.path.abspath(__file__))
        icon_path = os.path.join(script_path, 'gear-solid.svg')

        self.setWindowIcon(QIcon(icon_path))
        self.setWindowTitle("QUERY-BOT")
        self.setGeometry(100, 100, 800, 400)

        # Widget for Chat History
        self.chat_histories = [QTextEdit() for _ in range(3)]
        for chat_history in self.chat_histories:
            chat_history.setReadOnly(True)
            chat_history.setStyleSheet('background-color: #fff; border: 1px solid #fff;')
        # Widget for Entry Field
        self.entry_field = QLineEdit()
        self.entry_field.setPlaceholderText("Write your text here...")
        self.entry_field.setStyleSheet('background-color: #fff; border: 1px solid #fff; padding: 8px;')
        self.entry_field.textChanged.connect(self.handle_text_changed)  # Connect to textChanged signal
        # Widget for Send Button
        script_path = os.path.dirname(os.path.abspath(__file__))
        icon_path = os.path.join(script_path, 'paper-plane-solid.svg')
        self.send_button = QPushButton()
        self.send_button.setIcon(QIcon(icon_path))
        self.send_button.setStyleSheet('background-color: #fff; border: none; padding: 10px;')
        self.send_button.setEnabled(False)
        self.send_button.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.send_button.clicked.connect(self.handle_send_button)
        
        # Layout for Three (3) Chat History
        chat_history_layout = QHBoxLayout()
        for chat_history in self.chat_histories:
            chat_history_layout.addWidget(chat_history)
        # Layout for Entry Field and Send Button
        entry_layout = QHBoxLayout()
        entry_layout.setSpacing(0)
        entry_layout.addWidget(self.entry_field)
        entry_layout.addWidget(self.send_button)
        # Layout for Main Layout
        main_layout = QVBoxLayout()
        main_layout.addLayout(chat_history_layout)
        main_layout.addLayout(entry_layout)
        
        # Layout for Displaying All of the Layout
        central_widget = QWidget()
        central_widget.setStyleSheet('background-color: #ddd;')
        central_widget.setLayout(main_layout)
        self.setCentralWidget(central_widget)

        # This is where the response will be generated
        self.response1 = "Hello, how can I help you?"
        self.response2 = "How are you doing today?"
        self.response3 = "What can I assist you with?"
    
    def handle_text_changed(self, text):
        self.send_button.setEnabled(bool(text.strip()))  # Enable/disable button based on text field contents
    
    def handle_send_button(self):
        username = "User"
        self.botname1 = "NB-BOT"
        self.botname2 = "DT-BOT"
        self.botname3 = "NBT-BOT"

        message = self.entry_field.text()
        self.entry_field.clear()

        message_css = """
        <style>
            .user_box {
                border-collapse: collapse;
                margin: 0px 5px 7px 5px;
            }
            .bot_box {
                border-collapse: collapse;
                margin: 0px 5px 7px 5px;
            }

            .user_box .username{
                padding: 0px 0px 2px 5px;
                color: #999;
                font-size: 10px;
            }
            .bot_box .botname{
                padding: 0px 0px 2px 5px;
                color: #999;
                font-size: 10px;
            }

            .user_box .message{
                background-color: #222;
                color: #fff;
                padding: 10px;
                border-radius: 10px;
            }
            .bot_box .response{
                background-color: #eee;
                color: #333;
                padding: 10px;
            }
        </style>
        """
        
        
        # Add responses to chat history
        for i, chat_history in enumerate(self.chat_histories):
            botname = getattr(self, f"botname{i+1}")
            response = getattr(self, f"response{i+1}")

            chat_history.append(message_css + """
                <table class="user_box">
                    <tr><td class="username">{username}</td></tr>
                    <tr><td class="message">{message}</td></tr>
                </table>
            """.format(username=username, message=message))

            chat_history.append(message_css + """
                <table class="bot_box">
                    <tr><td class="botname">{botname}</td></tr>
                    <tr><td class="response">{response}</td></tr>
                </table>
            """.format(botname=botname, response=response))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    chatbot_ui = ChatBotUI()
    chatbot_ui.show()
    sys.exit(app.exec())
