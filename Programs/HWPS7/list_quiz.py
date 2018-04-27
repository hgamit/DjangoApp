#
# list_quiz.py:
#
#   Starting code H7-5
#

# Give short one-question quiz on HTT10 (Lists) to user

import random

question = "How many minutes is a rugby match?(Enter your answer on prompt)\n"
answer = "80"


print("---------------------------------")
print("You are running quick quiz")
print("---------------------------------\n")

user_answer_1 = input(question)
if user_answer_1.lower() == answer:
    print("Correct\n")
else:
    print("Incorrect, Correct answer is 80 Minutes\n")

