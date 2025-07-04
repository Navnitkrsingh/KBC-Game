# Print welcome message for the game
print("Welcome to the KBC Quiz Show! Let's win big!")

# Define questions, options, and answers
questions = [
    {"question": "What is the capital of India?", "options": ["1. Mumbai", "2. Delhi", "3. Kolkata", "4. Chennai"], "answer": 2},
    {"question": "Which planet is known as the Red Planet?", "options": ["1. Jupiter", "2. Mars", "3. Venus", "4. Mercury"], "answer": 2}
]

# Function to run one quiz question
def ask_question(q, prize):
    # Print prize amount for current question
    print("Question for $" + str(prize) + ":")
    # Print the question
    print(q["question"])
    # Print all options
    for option in q["options"]:
        print(option)
    try:
        # Get user's answer
        user_answer = int(input("Enter your answer (1-4): "))
        # Check if answer is correct
        if user_answer == q["answer"]:
            print("Correct! You won $" + str(prize) + "!")
            return True
        else:
            print("Wrong answer! Game over!")
            return False
    except:
        # Handle invalid input
        print("Invalid input! Game over!")
        return False

# Main game loop
while True:
    # Initialize prize money
    prize = 1000
    # Track if player can continue
    game_on = True
    # Loop through each question
    for q in questions:
        # Ask question and update game status
        if not ask_question(q, prize):
            game_on = False
            break
        # Double prize for next question
        prize *= 2
    # Print final result
    if game_on:
        print("Congrats! You answered all questions!")
    # Ask to play again
    play_again = input("Play again? (yes/no): ")
    # Exit if player says no
    if play_again.lower() != "yes":
        print("Thanks for playing KBC! Come back soon!")
        break