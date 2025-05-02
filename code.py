import random
import time

# ANSI escape codes for colored output
class Colors:
    RESET = '\033[0m'
    RED = '\033[91m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    CYAN = '\033[96m'

def colorful_print(color, text):
    print(color + text + Colors.RESET)

def get_feedback(secret, guess):
    diff = abs(secret - guess)
    if diff == 0:
        return f"{Colors.GREEN}🎉 Correct! You nailed it! 🎯{Colors.RESET}"
    elif diff <= 5:
        return f"{Colors.RED}🔥 Super hot! You're really close!{Colors.RESET}"
    elif diff <= 10:
        return f"{Colors.YELLOW}🌡️ Warm... getting closer.{Colors.RESET}"
    else:
        return f"{Colors.CYAN}❄️ Cold. Way off!{Colors.RESET}"

def guessing_game():
    secret_number = random.randint(1, 100)
    attempts = 7

    colorful_print(Colors.CYAN, "Welcome to the Number Guessing Game!")
    print("🎲 I'm thinking of a number between 1 and 100.")
    print(f"💡 You have {attempts} attempts. Let's begin!\n")

    for attempt in range(1, attempts + 1):
        try:
            guess = int(input(f"Attempt {attempt}/{attempts} - Enter your guess: "))
            if guess < 1 or guess > 100:
                colorful_print(Colors.YELLOW, "🚫 Please enter a number between 1 and 100.")
                continue
        except ValueError:
            colorful_print(Colors.YELLOW, "🚫 That's not a valid number.")
            continue

        feedback = get_feedback(secret_number, guess)
        print(feedback)

        if guess == secret_number:
            break
    else:
        colorful_print(Colors.RED, f"💀 Out of attempts! The number was {secret_number}.")

    colorful_print(Colors.CYAN, "Thanks for playing! 🎮")

if __name__ == "__main__":
    guessing_game()
