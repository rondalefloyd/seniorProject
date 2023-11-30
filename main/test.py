from naive_bayes.bot import get_answer_nb
from decision_tree.bot import get_answer_dtree
from NB_Tree.bot import get_answer_nbtree

import tkinter as tk

class MessengerApp:
    def __init__(self, master):
        self.master = master
        self.master.geometry("700x500")
        self.master.title("Messenger")
        self.master.protocol("WM_DELETE_WINDOW", self.close_app)

        botName = ["NAIVE BAYES", "DECISION TREE", "NB TREE"]
        self.conversations = []
        for i in range(3):
            conversation = Conversation(self.master, f"{botName[i]}")
            self.conversations.append(conversation)
            conversation.frame.place(relx=i/3 + 0.01, rely=0.01, relwidth=0.31, relheight=0.75)

        self.input_frame = tk.Frame(self.master)
        self.input_frame.pack(side=tk.BOTTOM, fill=tk.X)

        self.message_entry = tk.Entry(self.input_frame)
        self.message_entry.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=5, pady=5)
        self.message_entry.bind("<Return>", self.send_message)

        self.send_button = tk.Button(self.input_frame, text="Send", command=self.send_message)
        self.send_button.pack(side=tk.RIGHT, padx=5, pady=5)

    def send_message(self, event=None):
        message = self.message_entry.get()
        if message.strip() == "":
            return

        self.message_entry.delete(0, tk.END)

        for conversation in self.conversations:
            conversation.add_message("me", message)
        
        self.get_response(message)
        

    def get_response(self, message):
        for conversation in self.conversations:
            if conversation.title == "NAIVE BAYES":
                sender = "bot"
                response = get_answer_nb(message)
            elif conversation.title == "DECISION TREE":
                sender = "bot"
                # Call the appropriate function to get the response for the decision tree bot
                response = get_answer_dtree(message)
            else:
                sender = "bot"
                # Call the appropriate function to get the response for the NB Tree bot
                response = get_answer_nbtree(message)

            conversation.add_message(sender, response)

    def close_app(self):
        self.master.destroy()

class Conversation:
    def __init__(self, master, title):
        self.master = master
        self.title = title  # Store the title as an instance variable
        self.frame = tk.Frame(self.master, bd=1, relief=tk.SOLID)

        self.title_label = tk.Label(self.frame, text=title)
        self.title_label.pack(side=tk.TOP, fill=tk.X)

        self.messages_frame = tk.Frame(self.frame)
        self.messages_frame.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

        self.message_history_scroll = tk.Canvas(self.messages_frame)
        self.message_history_scroll.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        self.message_history = tk.Frame(self.message_history_scroll)
        self.message_history.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        
        self.message_history_scroll.create_window((0, 0), window=self.message_history, anchor="nw")

        scrollbar = tk.Scrollbar(self.message_history_scroll)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        self.message_history_scroll.config(yscrollcommand=scrollbar.set)
        scrollbar.config(command=self.message_history_scroll.yview)

        # self.message_history_scroll.tag_configure("user", justify="right", foreground="white", background="#3070B0")
        # self.message_history_scroll.tag_configure("bot", justify="left", foreground="white", background="#3F4D5A")

        self.messages = []

    def add_message(self, sender, message):
        message_frame = tk.Frame(self.message_history)
        message_frame.pack(side=tk.TOP, fill=tk.BOTH, padx=10, pady=5)

        if sender == "me":
            tag = "user"
            bg_color = "#3070B0"
            anchor = tk.RIGHT
        else:
            tag = "bot"
            bg_color = "#3F4D5A"
            anchor = tk.LEFT

        # # self.message_history_scroll.insert(tk.END, f"{message}\n")

        message_label = tk.Label(message_frame, text=message, wraplength=300, justify="left", bg=bg_color, fg="white")
        message_label.pack(side=anchor, padx=5, pady=5, fill=tk.X)


        # Bind the Canvas widget to the Scrollbar widget
        def on_canvas_configure(event):
            self.message_history_scroll.configure(scrollregion=self.message_history_scroll.bbox('all'))

        self.message_history_scroll.bind('<Configure>', on_canvas_configure)

        self.message_history_scroll.config(scrollregion=self.message_history_scroll.bbox(tk.ALL))

        # self.messages.append(message_frame)
        self.message_history_scroll.update_idletasks()


def main():
    root = tk.Tk()
    app = MessengerApp(root)
    
    root.mainloop()

if __name__ == '__main__':
    main()
