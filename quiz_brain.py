class QuizBrain:
    def __init__(self, question_list):
        self.question_number = 0
        self.score = 0
        self.question_list = question_list
        
    def still_has_question(self):
        return self.question_number < len(self.question_list)
        
    def next_question(self):
        currentItem = self.question_list[self.question_number]
        self.question_number += 1
        answer = input(f"Q. {self.question_number}: {currentItem.text} (True/False): ")
        self.check_answer(answer, currentItem.answer)
        
    def check_answer(self, answer, correct_answer):
        if (answer.lower() == correct_answer.lower()):
            self.score += 1
            print(f"The correct answer is {correct_answer}")
            print(f"Your score is: {self.score} / {len(self.question_list)}")
        else:
            print(f"The correct answer was {correct_answer}")
            print(f"Your score is: {self.score} / {len(self.question_list)}")