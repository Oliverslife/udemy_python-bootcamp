# asking the questions
# checking if the answer was correct
# checking if we're the end of the quiz

# question_number, question_list
class QuizBrain:

    def __init__(self, quiz):
        self.question_number = 0
        self.question_list = quiz

    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        input(f"Q.{self.question_number}: {current_question.test} (True/Fasle): ")

    def still_has_questions(self):
        return self.question_number < len(self.question_list)

        # if self.question_number < len(self.question_list): # next_question에서 +1 되니까
        #     return True
        # else:
        #     False
