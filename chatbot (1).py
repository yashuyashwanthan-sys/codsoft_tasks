# ============================================================
# TASK 1: RULE-BASED CHATBOT
# CodSoft AI Internship - Batch C19
# ============================================================
# WHAT THIS DOES:
# A chatbot that reads what you type and replies based on
# rules we define. No AI needed — just smart if/else logic!
# ============================================================

import re  # 're' helps us do pattern matching (find words in sentences)

# ---------------------------------------------------------------
# STEP 1: Define our rules
# Each rule has:
#   "patterns" → words/phrases the user might type
#   "responses" → what the bot will reply
# ---------------------------------------------------------------

rules = [
    {
        "patterns": ["hello", "hi", "hey", "good morning", "good evening", "howdy"],
        "responses": [
            "Hello! How can I help you today?",
            "Hi there! What can I do for you?",
            "Hey! Nice to meet you. How can I assist?"
        ]
    },
    {
        "patterns": ["how are you", "how r you", "how are u", "are you okay"],
        "responses": [
            "I'm doing great, thanks for asking! How about you?",
            "I'm just a bot, but I'm functioning perfectly! 😊"
        ]
    },
    {
        "patterns": ["your name", "who are you", "what are you", "introduce yourself"],
        "responses": [
            "I'm RuleBot — a simple chatbot built for the CodSoft AI Internship!",
            "My name is RuleBot. I respond based on rules written by my creator!"
        ]
    },
    {
        "patterns": ["what can you do", "help", "features", "capabilities"],
        "responses": [
            "I can answer questions about: greetings, jokes, the weather (fake!), time, and general chat. Try asking me something!",
        ]
    },
    {
        "patterns": ["joke", "tell me a joke", "make me laugh", "funny"],
        "responses": [
            "Why do programmers prefer dark mode? Because light attracts bugs! 🐛",
            "Why did the computer go to the doctor? Because it had a virus! 💻",
            "How do you comfort a JavaScript bug? You console it! 😄"
        ]
    },
    {
        "patterns": ["weather", "temperature", "hot", "cold", "rain"],
        "responses": [
            "I don't have real weather data, but it's always sunny in the world of code! ☀️",
            "Check Google for weather — I only know that Python is always warm! 🐍"
        ]
    },
    {
        "patterns": ["time", "what time", "current time"],
        "responses": [
            "I don't have a clock, but Python's datetime module can help! Try: import datetime; print(datetime.datetime.now())"
        ]
    },
    {
        "patterns": ["bye", "goodbye", "see you", "exit", "quit", "stop"],
        "responses": [
            "Goodbye! Have a great day! 👋",
            "See you later! Keep coding! 💻",
            "Bye bye! Come back anytime!"
        ]
    },
    {
        "patterns": ["thank", "thanks", "thank you", "thx"],
        "responses": [
            "You're welcome! 😊",
            "Happy to help!",
            "Anytime! That's what I'm here for."
        ]
    },
    {
        "patterns": ["codsoft", "internship", "task"],
        "responses": [
            "CodSoft is a great platform to learn by doing! This chatbot is Task 1 of the AI Internship.",
            "You're doing the CodSoft AI internship? Awesome! Keep going — you've got this! 💪"
        ]
    }
]

# ---------------------------------------------------------------
# STEP 2: The matching function
# This checks if any pattern word appears in what the user typed
# ---------------------------------------------------------------

import random  # used to pick a random response so it doesn't feel robotic

def get_response(user_input):
    """
    Takes what the user typed, looks for matching patterns,
    and returns an appropriate response.
    """
    # Convert to lowercase so "Hello" and "hello" both match
    user_input_lower = user_input.lower()

    # Loop through each rule
    for rule in rules:
        for pattern in rule["patterns"]:
            # Check if the pattern appears anywhere in user's message
            if pattern in user_input_lower:
                # Pick a random response from the list
                return random.choice(rule["responses"])

    # If nothing matched, return a default message
    return "Hmm, I'm not sure about that. Try asking something else, or type 'help'!"

# ---------------------------------------------------------------
# STEP 3: Run the chatbot
# This is the main loop — it keeps asking for input until you say bye
# ---------------------------------------------------------------

def run_chatbot():
    print("=" * 50)
    print("       Welcome to RuleBot! 🤖")
    print("  Type 'bye' to exit the chatbot")
    print("=" * 50)

    while True:
        # Get input from the user
        user_input = input("\nYou: ").strip()

        # Skip if user just pressed Enter with nothing
        if not user_input:
            print("RuleBot: Please type something!")
            continue

        # Get and print the bot's response
        response = get_response(user_input)
        print(f"RuleBot: {response}")

        # If user wants to exit, break the loop
        if any(word in user_input.lower() for word in ["bye", "goodbye", "exit", "quit", "stop"]):
            break

# ---------------------------------------------------------------
# Run the chatbot when this file is executed
# ---------------------------------------------------------------
if __name__ == "__main__":
    run_chatbot()
