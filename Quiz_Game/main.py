from data import question_data
from question_model import Question
from quiz_brain import QuizBrain


question_bank = []
for data in question_data:
     question_text = data["text"]
     question_answer = data["answer"]
     new_question = Question(question_text, question_answer)
     question_bank.append(new_question)


quiz = QuizBrain(question_bank)
quiz.next_question()

while quiz.still_has_question():
     quiz.next_question()

print("You have completed the quiz")
print(f"Your final score was: {quiz.score}/{quiz.question_number}")