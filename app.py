from Question import Question

question_prompts = [
    "Where is Nigeria located?\n(a) Asia\n(b) Oceania\n(c) Africa\n(d) Europe\n",
    "What color is water?\n(a) colorless\n(b) white\n(c) transparent\n(d) none of the above\n",
    "In what year did Nigeria gain her independence?\n(a) 1979\n(b) 1960\n(c) 1900\n(d) 1950\n",
    "How many players play in a soccer team ?\n(a) 9\n(b) 22\n(c) 11\n(d) I don't know\n",
]

answers = ['c', 'a', 'b', 'c']
questions = []

for index in range(len(question_prompts)):
    questions.append(Question(question_prompts[index], answers[index]))


def run_test(quests):
    score = 0
    for question in quests:
        answer = input(question.prompt)
        if answer == question.answer:
            score += 1
    return "You scored " + str(score) + '/' + str(len(quests))


print(run_test(questions))
