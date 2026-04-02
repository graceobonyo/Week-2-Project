
import random

HIGHSCORE_FILE = "highscores.txt"

def choose_difficulty():
    print("\nChoose Difficulty Level:")
    print("1. Easy (10 tries)")
    print("2. Medium (7 tries)")
    print("3. Hard (5 tries)")

    while True:
        choice = input("Enter 1, 2, or 3: ")
        if choice == "1":
            return "Easy", 10
        elif choice == "2":
            return "Medium", 7
        elif choice == "3":
            return "Hard", 5
        else:
            print("Invalid choice. Try again.")

def save_highscore(username, attempts_left, difficulty):
    with open(HIGHSCORE_FILE, "a") as file:
        file.write(f"{username},{difficulty},{attempts_left}\n")

def show_leaderboard():
    print("\n Leaderboard ")
    try:
        with open(HIGHSCORE_FILE, "r") as file:
            scores = file.readlines()
            if not scores:
                print("No scores yet.")
                return

            for line in scores:
                name, difficulty, score = line.strip().split(",")
                print(f"{name} | {difficulty} | Attempts Left: {score}")
    except FileNotFoundError:
        print("No leaderboard found yet.")

def play_game():
    print("\n🎮 Welcome to Guess the Number Game 🎮")
    username = input("Enter your username: ")

    difficulty, max_attempts = choose_difficulty()
    secret_number = random.randint(1, 100)

    print(f"\nI'm thinking of a number between 1 and 100.")
    print(f"Difficulty: {difficulty}")
    print(f"You have {max_attempts} attempts.\n")

    attempts = 0

    while attempts < max_attempts:
        try:
            guess = int(input("Make a guess: "))
        except ValueError:
            print("Please enter a valid number.")
            continue

        attempts += 1
        remaining = max_attempts - attempts

        if guess == secret_number:
            print(f"\n Correct! You guessed the number in {attempts} tries.")
            save_highscore(username, remaining, difficulty)
            break
        elif guess > secret_number:
            print("Too High!")
        else:
            print("Too Low!")

        if attempts == 3:
            # Hint after 3 wrong attempts
            if secret_number % 2 == 0:
                print("Hint: The number is even.")
            else:
                print("Hint: The number is odd.")

        print(f"Attempts remaining: {remaining}\n")

    else:
        print(f"\n Game Over! The number was {secret_number}.")

    show_leaderboard()

if __name__ == "__main__":
    play_game()
