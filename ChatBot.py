def chatbot_response(user_input):
    user_input = user_input.lower()
    if "hello" in user_input or "hi" in user_input:
        return "Hello! How can I assist you today?"
    elif "how are you" in user_input:
        return "I'm doing great, thank you! How about you?"
    elif "bye" in user_input or "goodbye" in user_input:
        return "Goodbye! Have a great day!"
    elif "name" in user_input:
        return "I am your friendly chatbot. You can call me Chatbot!"
    elif "help" in user_input:
        return "Sure, I can help. What do you need assistance with?"
    elif "weather" in user_input:
        return "I'm sorry, I can't check the weather right now. But you can try using a weather app!"
    else:
        return "I'm sorry, I didn't quite understand that. Can you please rephrase?"
def start_chat():
    print("Welcome to the simple chatbot! Type 'bye' to exit.")
    while True:
        user_input = input("You: ")
        if "bye" in user_input.lower() or "goodbye" in user_input.lower():
            print("Chatbot: Goodbye! Have a great day!")
            break
        response = chatbot_response(user_input)
        print(f"Chatbot: {response}")
start_chat()