# Rule-Based AI Chatbot (Project 1)

print("Chatbot: Hello! Type 'bye' to exit.")

while True:
    user_input = input("You: ").lower()

    # Greeting responses
    if user_input == "hi" or user_input == "hello" or user_input == "hey":
        print("Bot: Hello! How can I assist you?")

    # Basic conversation
    elif user_input == "how are you":
        print("Bot: I am fine. Thank you!")

    elif user_input == "what is your name":
        print("Bot: I am a Rule-Based Chatbot.")

    # Exit condition
    elif user_input == "bye" or user_input == "exit" or user_input == "quit":
        print("Bot: Goodbye! ")
        break

    # Default response
    else:
        print("Bot: Sorry, I did not understand that.")