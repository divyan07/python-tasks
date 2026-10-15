
# BASIC CHATBOT IN PYTHON

print("ChatBot: Hello! Welcome to my chatbot.")
print("ChatBot: You can ask me simple questions.")
print("ChatBot: Type 'bye' to exit.\n")

while True:
    user = input("You: ").lower().strip()

    if user == "hello" or user == "hi" or user == "hey":
        print("ChatBot: Hello! How are you?")

    elif "how are you" in user:
        print("ChatBot: I'm doing great! Thanks for asking.")

    elif "your name" in user:
        print("ChatBot: My name is PythonBot.")

    elif "your age" in user or "how old are you" in user:
        print("ChatBot: I'm a computer program, so I don't have an age.")

    elif "who created you" in user:
        print("ChatBot: I was created using Python!")

    elif "help" in user:
        print("ChatBot: Sure! What do you need help with?")

    elif "your favourite colour" in user or "your favorite color" in user:
        print("ChatBot: I like blue!")

    elif "thank you" in user or "thanks" in user:
        print("ChatBot: You're welcome!")

    elif "what can you do" in user:
        print("ChatBot: I can answer simple questions and chat with you.")

    elif "joke" in user:
        print("ChatBot: Why do programmers prefer dark mode?")
        print("ChatBot: Because light attracts bugs!")

    elif "bye" in user or "exit" in user or "quit" in user:
        print("ChatBot: Goodbye! Have a great day!")
        break

    else:
        print("ChatBot: Sorry, I don't understand that yet.")
        print("ChatBot: Try asking me something else.")
