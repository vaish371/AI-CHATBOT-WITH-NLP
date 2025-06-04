import nltk
from nltk.chat.util import Chat, reflections

# --- NLTK Data Download (Automated Check) ---
try:
    nltk.data.find('corpora/wordnet')
except Exception:
    print("Downloading 'wordnet' NLTK corpus...")
    nltk.download('wordnet')
except Exception as e:
    print(f"Error checking/downloading 'wordnet': {e}")

try:
    nltk.data.find('tokenizers/punkt')
except Exception:
    print("Downloading 'punkt' NLTK tokenizer...")
    nltk.download('punkt')
except Exception as e:
    print(f"Error checking/downloading 'punkt': {e}")

# --- Chatbot Patterns and Responses ---
pairs = [
    [
        r"hi|hello|hey",
        ["Hello!", "Hi there!", "Hey! How can I help you?"]
    ],
    [
        r"my name is (.*)",
        ["Hello %1, how can I assist you today?", "Nice to meet you, %1!"]
    ],
    [
        r"what is your name?",
        ["I am a chatbot created to help you.", "You can call me ChatBot.", "I don't have a name, I'm just a program."]
    ],
    [
        r"how are you?",
        ["I'm doing great, thank you for asking!", "I'm just a program, but I'm ready to help.", "All good! How about you?"]
    ],
    [
        r"what can you do|how can you help",
        ["I can answer your questions based on my programming.", "I can provide information on various topics. What are you looking for?", "I can help with general inquiries and simple conversations."]
    ],
    [
        r"i need (.*)",
        ["Why do you need %1?", "Are you sure you need %1?", "Perhaps I can help you find %1."]
    ],
    [
        r"i am (.*) (good|well|fine)",
        ["That's great to hear!", "Wonderful!"]
    ],
    [
        r"quit|bye|exit|goodbye",
        ["Goodbye! Have a great day!", "See you later!", "Bye for now!", "It was nice chatting with you!"]
    ],
    [
        r"(.*) (thank you|thanks)",
        ["You're welcome!", "Glad I could help!", "No problem!", "Anytime!"]
    ],
    [
        r"(.*)", # This is a default, catch-all pattern for anything not matched above.
        ["I'm sorry, I don't understand that.", "Can you please rephrase your question?", "Could you provide more details?", "I'm still learning. Can you try asking in a different way?"]
    ]
]

# --- Chatbot Initialization ---
chatbot = Chat(pairs, reflections)

# --- Main Chatbot Function ---
def start_chatbot():
    """
    Starts the interactive chatbot conversation.
    """
    print("--- Welcome to the NLTK Chatbot! ---")
    print("Type your message and press Enter. Type 'quit' to exit.")
    print("-" * 35)

    while True:
        user_input = input("You: ")
        if user_input.lower() in ['quit', 'exit', 'goodbye', 'bye']:
            print("ChatBot: Goodbye! Have a great day!")
            break

        response = chatbot.respond(user_input)

        if response:
            print(f"ChatBot: {response}")
        else:
            print("ChatBot: I'm not sure how to respond to that.")

if __name__ == "__main__":
    start_chatbot()
