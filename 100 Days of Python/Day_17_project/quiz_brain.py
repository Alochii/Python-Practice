class QuizBrain:
    def __init__(self, q_list):
        self.question_number = 0
        self.question_list = q_list
        self.score = 0

    def next_question(self):
        self.question_number += 1
        my_answer = input(f"Question {self.question_number}. {self.question_list[self.question_number - 1].text},"
              f" is that 'True' or 'False'?")
        self.check_answer(my_answer,self.question_list[self.question_number -1].answer)
        print(f"your current score is : {self.score}/{self.question_number}\n")
    def still_has_question(self):
        if self.question_number < len(self.question_list):
            return True
        else :
            print(f"you've completed the quiz and managed to score {self.score} points out of {self.question_number}")
            return False

    def check_answer(self,my_answer,correct_answer):
        if my_answer.lower() == correct_answer.lower():
            print("you were right!")
            self.score += 1
        else :
            print("you were wrong.")
