import tkinter as tk
from tkinter import scrolledtext
from datetime import datetime
import random


# ---------------- CHATBOT LOGIC ----------------

def chatbot_response(user_input):
    user_input = user_input.lower().strip()

    if user_input in [
        "hello", "hi", "hey", "hii",
        "good morning", "good afternoon", "good evening"
    ]:
        return "Hello! Nice to meet you. How can I help you?"

    elif "how are you" in user_input:
        return "I'm doing great! Thanks for asking."

    elif "your name" in user_input or "who are you" in user_input:
        return "I am a rule-based chatbot created using Python."

    elif "time" in user_input:
        current_time = datetime.now().strftime("%I:%M %p")
        return f"The current time is {current_time}."

    elif "date" in user_input or "today" in user_input:
        current_date = datetime.now().strftime("%d-%m-%Y")
        return f"Today's date is {current_date}."

    elif "joke" in user_input:
        jokes = [
            "Why do programmers prefer dark mode? Because light attracts bugs! 😄",
            "Why was the computer cold? It left its Windows open! 😂",
            "Why do programmers wear glasses? Because they can't C#! 🤓"
        ]
        return random.choice(jokes)

    elif "thank" in user_input:
        return "You're welcome! 😊"

    elif "help" in user_input:
        return (
            "Here are some things you can ask me:\n\n"
            "• Hello / Hi\n"
            "• What is your name?\n"
            "• How are you?\n"
            "• What time is it?\n"
            "• What is today's date?\n"
            "• Tell me a joke\n"
            "• Thank you\n"
            "• Help\n"
            "• Bye / Exit"
        )

    elif user_input in ["bye", "exit", "quit"]:
        return "Goodbye! Have a great day! 👋"

    else:
        return "Sorry, I don't understand that. Type 'help' to see what I can do."


# ---------------- GUI FUNCTIONS ----------------

def send_message(event=None):
    user_input = entry.get().strip()

    if not user_input:
        return

    chat_area.config(state=tk.NORMAL)

    # Display user message
    chat_area.insert(tk.END, f"You: {user_input}\n", "user")

    # Get chatbot response
    response = chatbot_response(user_input)

    # Display bot response
    chat_area.insert(tk.END, f"Bot: {response}\n\n", "bot")

    chat_area.config(state=tk.DISABLED)
    chat_area.see(tk.END)

    entry.delete(0, tk.END)

    # Close after goodbye
    if user_input.lower() in ["bye", "exit", "quit"]:
        root.after(1500, root.destroy)


def show_help():
    entry.delete(0, tk.END)
    entry.insert(0, "help")
    send_message()


def clear_chat():
    chat_area.config(state=tk.NORMAL)
    chat_area.delete("1.0", tk.END)

    chat_area.insert(
        tk.END,
        "Bot: Hello! I am your Rule-Based Chatbot 🤖\n"
        "Bot: Type 'help' to see what I can do.\n\n",
        "bot"
    )

    chat_area.config(state=tk.DISABLED)


# ---------------- MAIN WINDOW ----------------

root = tk.Tk()
root.title("CODSOFT - Rule-Based Chatbot")
root.geometry("700x650")
root.minsize(600, 550)

# Header
header = tk.Frame(root, bg="#1f2937", height=80)
header.pack(fill=tk.X)

title = tk.Label(
    header,
    text="🤖 CODSOFT RULE-BASED CHATBOT",
    font=("Arial", 20, "bold"),
    bg="#1f2937",
    fg="white"
)
title.pack(pady=20)

# Chat area
chat_area = scrolledtext.ScrolledText(
    root,
    wrap=tk.WORD,
    font=("Arial", 12),
    padx=15,
    pady=15,
    state=tk.DISABLED
)

chat_area.pack(
    fill=tk.BOTH,
    expand=True,
    padx=15,
    pady=(15, 10)
)

# Message formatting
chat_area.tag_config("user", font=("Arial", 12, "bold"))
chat_area.tag_config("bot", font=("Arial", 12))

# Initial message
chat_area.config(state=tk.NORMAL)
chat_area.insert(
    tk.END,
    "Bot: Hello! I am your Rule-Based Chatbot 🤖\n"
    "Bot: Type 'help' to see what I can do.\n\n",
    "bot"
)
chat_area.config(state=tk.DISABLED)

# Input frame
input_frame = tk.Frame(root)
input_frame.pack(fill=tk.X, padx=15, pady=5)

entry = tk.Entry(
    input_frame,
    font=("Arial", 13)
)
entry.pack(
    side=tk.LEFT,
    fill=tk.X,
    expand=True,
    ipady=10
)

entry.bind("<Return>", send_message)

send_button = tk.Button(
    input_frame,
    text="Send",
    font=("Arial", 11, "bold"),
    command=send_message,
    padx=20,
    pady=8
)
send_button.pack(side=tk.RIGHT, padx=(8, 0))

# Bottom buttons
button_frame = tk.Frame(root)
button_frame.pack(fill=tk.X, padx=15, pady=(5, 15))

help_button = tk.Button(
    button_frame,
    text="Help",
    command=show_help,
    width=12
)
help_button.pack(side=tk.LEFT)

clear_button = tk.Button(
    button_frame,
    text="Clear Chat",
    command=clear_chat,
    width=12
)
clear_button.pack(side=tk.RIGHT)

# Focus input
entry.focus()

# Start GUI
root.mainloop()