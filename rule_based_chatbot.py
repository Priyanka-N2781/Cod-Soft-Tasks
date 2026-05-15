import re


def normalize(text: str) -> str:
    text = text.strip().lower()
    text = re.sub(r"\s+", " ", text)
    return text


def get_response(user_text: str) -> str:
    t = normalize(user_text)

    # Greeting
    if any(word in t for word in ["hi", "hello", "hey"]):
        return "Hello! How can I help you today?"

    # Help / options
    if any(word in t for word in ["help", "what can you do", "commands", "options"]):
        return (
            "I can answer using simple rules. Try asking:\n"
            "- your name\n"
            "- hours / timing\n"
            "- price / cost\n"
            "- where you are located\n"
            "- bye / exit"
        )

    # Name
    if any(word in t for word in ["your name", "what is your name", "who are you"]):
        return "I'm a rule-based chatbot. I follow predefined responses."

    # Hours / timing
    if any(word in t for word in ["hours", "timing", "open", "close", "work time"]):
        return "We are available daily from 9:00 AM to 6:00 PM."

    # Price / cost
    if any(word in t for word in ["price", "cost", "pricing", "fee"]):
        return "Our pricing depends on the service. Tell me what you need and I’ll guide you."

    # Location
    if any(word in t for word in ["location", "where are you", "address", "branch", "where"]):
        return "We are located at: 123 Main Street, Your City."

    # Thanks
    if any(word in t for word in ["thanks", "thank you", "thx"]):
        return "You're welcome! Anything else?"

    # Exit
    if any(word in t for word in ["bye", "goodbye", "exit", "quit"]):
        return "Goodbye! Have a great day."

    # Fallback
    return (
        "I’m not sure about that. Try asking something like: "
        "'hours', 'price', 'location', or 'help'."
    )


def main() -> None:
    print("Rule-Based Chatbot (type 'exit' to quit)")
    while True:
        user_text = input("\nYou: ")
        if normalize(user_text) in ["exit", "quit", "bye"]:
            print("Bot:", get_response(user_text))
            break
        print("Bot:", get_response(user_text))


if __name__ == "__main__":
    main()

