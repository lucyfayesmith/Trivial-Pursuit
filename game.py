def main():


    questions_file = open("Questions","r")

    questions = []

    for line in questions_file:
        question = line.strip("\n").split(",")
        questions.append(question)

    print(questions)

    ask_questions()

def ask_questions():

    questions_file = open("Questions", "r")

    user_answer = []

    for line in questions_file:
        user_answer = input("What is your answer?"
                            "\nA"
                            "\nB"
                            "\nC")

main()