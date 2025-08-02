import webbrowser
url= "https://www.google.com/"
def chatbot_response(user_input):
    user_input = user_input.lower()

    if user_input == "hello":
        return "Hi!"
    elif user_input == "how are you":
        return "I'm fine, thanks!"
    elif user_input == "bye":
        return "Goodbye!"
    elif user_input == "what are you doing":
        return "nothing chating to you"
    elif user_input == "open google":
        return webbrowser.open(url)
    else:
        return "I don't understand that."


def run_chatbot():
    print("🤖 Chatbot: Hello! Type 'bye' to exit.")
    
    while True:
        user_input = input("You: ")
        response = chatbot_response(user_input)
        print("🤖 Chatbot:", response)
        
        if user_input.lower() == "bye":
            break


# Run the chatbot
run_chatbot()
