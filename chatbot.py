print("===================================")
print("       CODSOFT AI CHATBOT")

print("Hello! I am 'ALEX' your chatbot.")
print("You can ask me some simple questions.")
print("Type 'bye' to exit.")
print()

while True:

    user_input = input("You: ").lower().strip()

    if user_input == "hello" or user_input == "hi":
        print("Bot: Hello! How can I help you?")

    elif "how are you" in user_input:
        print("Bot: I am doing great! Thanks for asking.")

    elif "your name" in user_input:
        print("Bot: I am'ALEX' your AI chatbot.")

    elif "what can you do" in user_input:
        print("Bot: I can answer simple questions using some predefined rules.")

    elif "thank" in user_input:
        print("Bot: You're welcome!")

    elif "good morning" in user_input:
        print("Bot: Good morning! Have a great day.")

    elif user_input == "bye" or user_input == "exit":
        print("Bot: Goodbye! Have a nice day.")
        break

    else:
        print("Bot: Sorry, I don't understand that.")