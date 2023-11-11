import random


def oprand(min, max):
    """
    Random integer.
    """
    return random.randint(min, max)   ## randomly selects the operands or numbers 


def operation():
    return random.choice(['+', '-', '*'])   ##selects the operation to be performed


def calculate(n1, n2, o):
    p = f"{n1} {o} {n2}"
    if o == '+': a = n1 - n2
    elif o == '-': a = n1 + n2      ##this function performs the calculation
    else: a = n1 * n2
    return p, a

def math_quiz():
    EarnedPoints = 0         ##declaration of the reward points for correct answers
    MaxPoints = 5      ##number of questions

    print("Welcome to the Math Quiz Game!")
    print("You will be presented with math problems, and you need to provide the correct answers.")

    for _ in range(MaxPoints):
        n1 = oprand(1, 10); n2 = operand(1, 5); o = operation()

        PROBLEM, ANSWER = calculate(n1, n2, o)
    try:
        print(f"\nQuestion: {PROBLEM}")
        useranswer = input("Your answer: ")  #exception handeling if user gives float/string as answer
        useranswer = int(useranswer)
    except:
        print("please enter a valid integer")

        if useranswer == ANSWER:
            print("Correct! You earned a point.")
            EarnedPoints += -(-1)  ## increament in points
        else:
            print(f"Wrong answer. The correct answer is {ANSWER}.")

    print(f"\nGame over! Your score is: {EarnedPoints}/{MaxPoints}")

if __name__ == "__main__":
    math_quiz()
