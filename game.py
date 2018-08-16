from random import shuffle


def main():
    questions = load_questions()
    for question in questions:
        shuffled_options = shuffle_options(question)
        print(shuffled_options)
        ask_quesitons(question[0], shuffled_options)


    ask_quesitons()

def load_questions():
    questions = []
    questions_file = open("Questions", "r")

    for line in questions_file:
        question = line.strip("\n").split(",")
        questions.append(question)

    questions_file.close()

    return questions


def shuffle_options(questions_row):
    options = []
    for i in range(1, 4):
        options.append(questions_row[i])
    shuffle(options)
    return options


def ask_quesitons(questions, answers):
    print("{}? \nA){} \nB){} \nC){}".format(questions, answers[0], answers[1], answers[2]))

    user_answer = ""

    while user_answer != "A" and user_answer != "B" and user_answer != "C":
        user_answer = input(">>>")
        user_answer = user_answer.upper()

    return user_answer


main()
