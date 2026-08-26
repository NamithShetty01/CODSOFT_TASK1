from datetime import datetime
import random


def show_help():
    print("\nBot: Here are some things you can ask me:")
    print("  • Hello / Hi")
    print("  • What is your name?")
    print("  • How are you?")
    print("  • What time is it?")
    print("  • What is today's date?")
    print("  • Tell me a joke")
    print("  • Thank you")
    print("  • Help")
    print("  • Bye / Exit")


def chatbot_response(user_input):
    user_input = user_input.lower().strip()

    if user_input in ["hello", "hi", "hey", "hii", "good morning",
                      "good afternoon", "good evening"]:
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
        show_help()
        return ""

    elif user_input in ["bye", "exit", "quit"]:
        return "Goodbye! Have a great day! 👋"

    else:
        return "Sorry, I don't understand that. Type 'help' to see what I can do."


def main():
    print("=" * 55)
    print("             CODSOFT RULE-BASED CHATBOT")
    print("=" * 55)
    print("Hello! I am ChatBot 🤖")
    print("Type 'help' to see what I can do.")
    print("Type 'bye', 'exit', or 'quit' to end the conversation.")
    print("=" * 55)

    while True:
        user_input = input("\nYou: ")

        response = chatbot_response(user_input)

        if response:
            print("Bot:", response)

        if user_input.lower().strip() in ["bye", "exit", "quit"]:
            break


if __name__ == "__main__":
    main()