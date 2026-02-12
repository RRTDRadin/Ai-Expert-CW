import random
from collections import Counter, defaultdict
from colorama import Fore, init

init(autoreset=True)

choices = ["rock", "paper", "scissors"]
counter_map = {"rock": "paper", "paper": "scissors", "scissors": "rock"}

def banner():
    print(Fore.CYAN + "=" * 60)
    print(Fore.YELLOW + "         SMART AI ROCK PAPER SCISSORS         ")
    print(Fore.CYAN + "=" * 60)

def display_rules():
    print(Fore.MAGENTA + "\nGame Mechanics")
    print("Rock defeats Scissors")
    print("Scissors defeats Paper")
    print("Paper defeats Rock\n")

def determine_winner(user, ai):
    if user == ai:
        return "tie"
    elif (user == "rock" and ai == "scissors") or \
         (user == "scissors" and ai == "paper") or \
         (user == "paper" and ai == "rock"):
        return "user"
    return "ai"

class SmartAI:
    def __init__(self):
        self.history = []
        self.transitions = defaultdict(Counter)

    def update(self, move):
        if self.history:
            self.transitions[self.history[-1]][move] += 1
        self.history.append(move)

    def frequency_prediction(self):
        if not self.history:
            return None, 0
        freq = Counter(self.history)
        return freq.most_common(1)[0]

    def markov_prediction(self):
        if not self.history:
            return None, 0
        last = self.history[-1]
        if last not in self.transitions:
            return None, 0
        predicted, count = self.transitions[last].most_common(1)[0]
        return predicted, count

    def ai_move(self):
        freq_pred, freq_score = self.frequency_prediction()
        markov_pred, markov_score = self.markov_prediction()

        if freq_pred and markov_pred:
            predicted = freq_pred if freq_score >= markov_score else markov_pred
            confidence = max(freq_score, markov_score)
        elif freq_pred:
            predicted = freq_pred
            confidence = freq_score
        elif markov_pred:
            predicted = markov_pred
            confidence = markov_score
        else:
            return random.choice(choices), "Random exploration mode"

        if random.random() < 0.1:
            return random.choice(choices), "Exploration mode"

        return counter_map[predicted], f"Predicted {predicted.upper()} → Optimal counter deployed"

def dashboard(round_no, user_score, ai_score, streak):
    print(Fore.CYAN + "-" * 60)
    print(Fore.YELLOW + f"Round: {round_no} | You: {user_score} | AI: {ai_score} | Streak: {streak}")
    print(Fore.CYAN + "-" * 60)

def main():
    ai_engine = SmartAI()

    while True:
        user_score = 0
        ai_score = 0
        round_no = 1
        streak = 0

        banner()
        print(Fore.GREEN + "rock / paper / scissors")
        print("rules → help | quit → exit\n")

        while True:
            dashboard(round_no, user_score, ai_score, streak)
            user = input(Fore.WHITE + "Your Move → ").lower()

            if user == "quit":
                break
            elif user == "rules":
                display_rules()
                continue
            elif user not in choices:
                print(Fore.RED + "Invalid input.")
                continue

            ai_choice, logic = ai_engine.ai_move()
            ai_engine.update(user)

            print(Fore.BLUE + f"AI Move → {ai_choice}")
            print(Fore.LIGHTBLACK_EX + f"AI Logic → {logic}")

            result = determine_winner(user, ai_choice)

            if result == "tie":
                print(Fore.YELLOW + "Result → DRAW")
                streak = 0
            elif result == "user":
                print(Fore.GREEN + "Result → YOU WIN")
                user_score += 1
                streak += 1
            else:
                print(Fore.RED + "Result → AI WINS")
                ai_score += 1
                streak = 0

            round_no += 1

        print(Fore.MAGENTA + "\nSession Analytics")
        print(Fore.GREEN + f"Your Wins: {user_score}")
        print(Fore.RED + f"AI Wins: {ai_score}")

        if input("\nRestart? (yes/no): ").lower() != "yes":
            print(Fore.CYAN + "\nSession closed.")
            break

if __name__ == "__main__":
    main()