def chatbot():
    print("Hello I am ai chatbot.")
    name = input("What is your name? ").strip()

    if name:
        print(f"Nice to meet you, {name}!")

    else:
        name = "Friend"
        print("Nice to meet you")

    while True:
        user_input = input(f"{name}: ").lower()

        if user_input in ["Hi", "Hello", "Hey"]:
            print(f"Bot: Hello {name}! How are you today?")
        elif user_input in ["How are you?", "How are you doing?"]:
            print("Bot: I'm doing great! Thanks for asking.")
        elif user_input in ["What is my name?", "Do you remember my name?"]:
            print(f"Bot: Of cource! Your name is {name}.")
        elif user_input in ["I got to go.", "Goodbye"]:
            print(f"Bot: Okay goodbye {name}! have a great day.")
            break
        else:
            print("Bot: That is interesting! Tell me more.")

chatbot()