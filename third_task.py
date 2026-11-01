
def get_reply(message):
    message = message.lower().strip()

    if message == "hello":
        return "Hi!"
    elif message == "how are you":
        return "I'm fine, thanks!"
    elif message == "bye":
        return "goodbye!"
    else:
        return "Sorry, I don't understand that."


def chatbot():
    print("= BASIC CHATBOT =")
    print("Try typing: hello, how are you, or bye\n")

    while True:
        user_input = input("You: ")
        reply = get_reply(user_input)
        print("Bot:", reply)

        if user_input.lower().strip() == "bye":
            break


chatbot()