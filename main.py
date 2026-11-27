
import random
import re


# NUMBER GUESSING GAME
def guessing_game():
    print("\n===== NUMBER GUESSING GAME =====")
    print("Guess a number between 1 and 100!")

    secret_number = random.randint(1, 100)
    attempts = 0
    score = 100

    while True:
        try:
            guess = int(input("Enter your guess: "))

            if guess < 1 or guess > 100:
                print("Please enter a number between 1 and 100.")
                continue

            attempts += 1

            if guess < secret_number:
                score = max(0, 100 - (attempts - 1) * 10)
                print("Too low! Try again.")

            elif guess > secret_number:
                score = max(0, 100 - (attempts - 1) * 10)
                print("Too high! Try again.")

            else:
                print("\nCongratulations! You guessed correctly!")
                print("Secret number:", secret_number)
                print("Total attempts:", attempts)
                print("Your score:", score, "/100")
                break

        except ValueError:
            print("Invalid input! Enter a whole number.")


# WORD FREQUENCY ANALYZER
def word_analyzer():
    print("\n===== WORD FREQUENCY ANALYZER =====")

    filename = input("Enter the text file name: ").strip()

    try:
        with open(filename, "r", encoding="utf-8") as file:
            text = file.read().lower()

        words = re.findall(r"\b[\w']+\b", text)

        if not words:
            print("The file is empty or contains no words.")
            return

        word_count = {}

        for word in words:
            word_count[word] = word_count.get(word, 0) + 1

        sorted_words = sorted(
            word_count.items(),
            key=lambda item: item[1],
            reverse=True
        )

        print("\n===== WORD FREQUENCY RESULTS =====")
        print("Total words:", len(words))
        print("Unique words:", len(word_count))

        print("\nMost common words:")

        for word, count in sorted_words[:10]:
            print(f"{word}: {count}")

    except FileNotFoundError:
        print("Error: File not found!")

    except PermissionError:
        print("Error: Permission denied!")

    except OSError as error:
        print("File error:", error)


# MAIN MENU
def main():
    while True:
        print("\n==============================")
        print("       PYTHON MINI TOOLS")
        print("==============================")
        print("1. Number Guessing Game")
        print("2. Word Frequency Analyzer")
        print("3. Exit")
        print("==============================")

        choice = input("Enter your choice (1-3): ").strip()

        if choice == "1":
            guessing_game()

        elif choice == "2":
            word_analyzer()

        elif choice == "3":
            print("Thank you for using Python Mini Tools!")
            break

        else:
            print("Invalid choice! Please select 1, 2, or 3.")


if __name__ == "__main__":
    main()
