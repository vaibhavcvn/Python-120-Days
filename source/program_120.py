import random

questions = [
    {
        "question": "What is the correct extension for a Python file?",
        "options": ["A. .java", "B. .py", "C. .cpp", "D. .cs"],
        "answer": "B"
    },
    {
        "question": "Which keyword is used to define a function?",
        "options": ["A. function", "B. define", "C. def", "D. func"],
        "answer": "C"
    },
    {
        "question": "Which data type stores key-value pairs?",
        "options": ["A. List", "B. Tuple", "C. Set", "D. Dictionary"],
        "answer": "D"
    },
    {
        "question": "Which library is commonly used for DataFrames?",
        "options": ["A. Pandas", "B. Flask", "C. Tkinter", "D. Turtle"],
        "answer": "A"
    },
    {
        "question": "Which keyword handles exceptions?",
        "options": ["A. catch", "B. try", "C. error", "D. handle"],
        "answer": "B"
    }
]

random.shuffle(questions)

score = 0

for question in questions:
    print("\n" + question["question"])

    for option in question["options"]:
        print(option)

    answer = input("Your answer: ").upper()

    if answer == question["answer"]:
        print("Correct!")
        score += 1
    else:
        print("Wrong!")
        print("Correct answer:", question["answer"])

print("\nQuiz completed!")
print("Score:", score, "/", len(questions))
