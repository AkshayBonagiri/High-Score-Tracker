import random

def game():
    # Generate a random score between 1 and 100
    score = random.randint(1, 100)

    # Read the current high score from the file
    with open("Hi_score.txt") as f:
        Hi_score = f.read()
        if Hi_score != "":
            Hi_score = int(Hi_score)
        else:
            Hi_score = 0

    print(f"Your score: {score}")

    # If the current score is greater than the high score, update the file
    with open("Hi_score.txt", "w") as f:
        if score > Hi_score:
            f.write(str(score))
        else:
            f.write(str(Hi_score))  # Ensure the file always has the highest score

    return score

game()
