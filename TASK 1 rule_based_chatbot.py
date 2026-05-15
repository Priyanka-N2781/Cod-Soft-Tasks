# Enhanced Rule-Based Chatbot in Python
# Version with main() function

from datetime import datetime


def get_response(user):
    user = user.lower().strip()

    # Greetings
    if user in ["hi", "hello", "hey"]:
        return "Hello! How can I help you?"

    # Basic conversation
    elif "how are you" in user:
        return "I am doing great. Thanks for asking!"

    elif "your name" in user:
        return "My name is RuleBot."

    elif "who created you" in user or "who made you" in user:
        return "I was created using Python."

    elif "what can you do" in user:
        return "I can answer simple predefined questions."

    # Date and time
    elif "time" in user:
        return "Current time is " + datetime.now().strftime("%H:%M:%S")

    elif "date" in user:
        return "Today's date is " + datetime.now().strftime("%d-%m-%Y")

    # Educational questions
    elif "what is ai" in user:
        return "AI stands for Artificial Intelligence."

    elif "what is python" in user:
        return "Python is a popular programming language."

    elif "what is java" in user:
        return "Java is an object-oriented programming language."

    elif "what is nlp" in user:
        return "NLP stands for Natural Language Processing."

    elif "what is machine learning" in user:
        return "Machine Learning is a branch of AI that enables systems to learn from data."

    elif "what is deep learning" in user:
        return "Deep Learning uses neural networks with many layers."

    elif "what is chatbot" in user:
        return "A chatbot is a program that simulates human conversation."

    # Programming questions
    elif "what is list" in user:
        return "A list is a collection of items in Python."

    elif "what is tuple" in user:
        return "A tuple is an immutable collection of items."

    elif "what is dictionary" in user:
        return "A dictionary stores data in key-value pairs."

    elif "what is loop" in user:
        return "A loop is used to repeat a block of code."

    elif "what is function" in user:
        return "A function is a reusable block of code."

    elif "what is class" in user:
        return "A class is a blueprint for creating objects."

    elif "what is object" in user:
        return "An object is an instance of a class."

    # Math questions
    elif "2 + 2" in user:
        return "2 + 2 = 4"

    elif "5 * 6" in user:
        return "5 * 6 = 30"

    elif "10 / 2" in user:
        return "10 / 2 = 5"

    elif "square of 5" in user:
        return "The square of 5 is 25"

    # General knowledge
    elif "capital of india" in user:
        return "The capital of India is New Delhi."

    elif "capital of france" in user:
        return "The capital of France is Paris."

    elif "largest planet" in user:
        return "Jupiter is the largest planet in our solar system."

    elif "fastest animal" in user:
        return "The cheetah is the fastest land animal."

    elif "who is the president of india" in user:
        return "The President of India is Droupadi Murmu."

    # Fun questions
    elif "tell me a joke" in user:
        return "Why do programmers prefer dark mode? Because light attracts bugs!"

    elif "favorite color" in user:
        return "My favorite color is blue."

    elif "favorite food" in user:
        return "I like binary cookies!"

    elif "sing a song" in user:
        return "La la la... I hope you enjoyed my song!"

    # Weather
    elif "weather" in user:
        return "I cannot check live weather, but I hope it is pleasant outside!"

    # Polite responses
    elif "thank you" in user or "thanks" in user:
        return "You're welcome!"

    elif "good morning" in user:
        return "Good morning! Have a wonderful day!"

    elif "good night" in user:
        return "Good night! Sweet dreams!"

    # Help
    elif "help" in user:
        return ("You can ask me about AI, Python, Java, NLP, date, time, "
                "capitals, jokes, and more.")

    # Exit
    elif user in ["bye", "exit", "quit"]:
        return "Goodbye! Have a great day!"

    # Default response
    else:
        return "Sorry, I don't understand that. Type 'help' to see what I can do."


def main():
    print("Chatbot: Hello! I am RuleBot.")
    print("Chatbot: Type 'bye' to exit.\n")

    while True:
        user_input = input("You: ")
        response = get_response(user_input)
        print("Chatbot:", response)

        if user_input.lower().strip() in ["bye", "exit", "quit"]:
            break


# Program starts here
if __name__ == "__main__":
    main()
