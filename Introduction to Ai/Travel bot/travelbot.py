import json
import random
import re
from colorama import Fore, Style, init

init(autoreset=True)

with open("training_data.jason", "r", encoding="utf-8") as f:
    intents = json.load(f)["intents"]

STOP_WORDS = {
    "i", "me", "you", "can", "please", "help", "on", "about",
    "the", "a", "an", "is", "am", "are", "to", "for", "with",
    "my", "your", "of", "before", "after", "some", "any"
}

def normalize(text):
    text = text.lower()
    text = re.sub(r"[^a-z\s]", "", text)
    tokens = text.split()
    tokens = [t for t in tokens if t not in STOP_WORDS]

def stem(word):
    for suffix in ["ing", "ed", "s"]:
        if word.endswith(suffix) and len(word) > 4:
            return word[:-len(suffix)]
        
def detect_intent (user_input):
    tokens = normalize(user_input)
    stemmed = {stem(t) for t in tokens}

    best_intent = None
    highest_score = 0

    for intent in intents:
        score = 0
        keyword = {stem(k) for k in intent["keyword"]}
        for token in stemmed:
            if token in keyword:
                score += 1

        if score > highest_score:
            highest_score = score
            best_intent = intent

    return best_intent if highest_score > 0 else None

def destination_help():
    return (
        "Destination Suggestions:\n"
        "- Budget: Cox’s Bazar, Nepal, Darjeeling\n"
        "- Nature: Bhutan, Switzerland, Kashmir\n"
        "- City: Dubai, Singapore, Bangkok"
    )


def packing_help():
    return (
        "Packing Checklist:\n"
        "- Documents\n"
        "- Clothes (weather-based)\n"
        "- Toiletries\n"
        "- Medicines\n"
        "- Charger & power bank\n"
        "- Emergency cash"
    )

def budget_help():
    return (
        "Budget Travel Tips:\n"
        "- Travel off-season\n"
        "- Use public transport\n"
        "- Book budget hotels\n"
        "- Avoid tourist traps"
    )

def guideline_help():
    return (
        "Travel Guidelines:\n"
        "- Keep documents secure\n"
        "- Respect local laws\n"
        "- Carry insurance\n"
        "- Stay aware of surroundings"
    )

def travelbot():
    print(Fore.CYAN + Style.BRIGHT + "\nTravelBot | Smart Travel Assistant\n")
    while True:
        user_input = input(Fore.YELLOW + "You: ")
        intent = detect_intent(user_input)

        if not intent:
            print(Fore.RED + "TravelBot: I’m not fully sure I understood. Please ask about planning, packing, destinations, or travel advice.")
            continue

        tag = intent["tag"]
        response = random.choice(intent["responses"])
        print(Fore.GREEN + "TravelBot: " + response)

        if tag == "destination":
            print(Fore.BLUE + destination_help())

        elif tag == "packing":
            print(Fore.BLUE + packing_help())

        elif tag == "budget":
            print(Fore.BLUE + budget_help())

        elif tag == "guidelines":
            print(Fore.BLUE + guideline_help())

        elif tag == "exit":
            break