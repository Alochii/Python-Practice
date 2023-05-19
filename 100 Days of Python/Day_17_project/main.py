import question_format
import data
import quiz_brain
# user_3 = question_format.Question(question,answer)

question_bank = []
for _ in range(0, len(data.question_data)):
    text = data.question_data[_]["question"]
    answer = data.question_data[_]["correct_answer"]
    question_bank.append(question_format.Question(text, answer))
# for _ in range(1,len(data.question_data)):

# print(question_bank[11].text)
game = quiz_brain.QuizBrain(question_bank)
while game.still_has_question():
    print(game.next_question())