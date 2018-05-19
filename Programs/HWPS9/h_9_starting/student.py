#
# H9-1:
#
#   student.py
#

class Student():
   #list_quizScore = []
   '''
   Represents a single student, with attribes:
      name, list of quiz scores, # to drop,
      average score for all quizzes after
      dropping specified # of lowest cores
   '''

   def __init__(self, name):
	   self.name = name
	   self.list_quizScore = []
	   '''
      Initialize new Student with given name
         and empty list _scores
      '''

   def addScore(self,score):
	   self.list_quizScore.append(score)
	   '''
      Add score to internal attribute (field) _scores
      '''

   def getNumberQuizzes(self):
	   return str(len(self.list_quizScore))
	   '''
      Return number of scores in attribute (field) _scores
      '''

   def calcQuizStats(self,dropNumber):
      self.dropNumber = dropNumber
      if(self.dropNumber>=len(self.list_quizScore)):
      	return 0.0
      else:
      	_average = Student.getAverage(self)
      	return str(_average)
      '''
      Set _dropNumber, then set _average to mean (avg) 
	  calculated after dropping dropNumber lowest scores'''
   def getAverage(self):
	   #print("avg")
	   n = len(self.list_quizScore) - self.dropNumber
	   sum = 0.0
	   for x in range(0, n):
		   sum += self.list_quizScore[x]
		
	   return sum/n
	   '''
      Return value of _average
      '''
   def __str__(self):
	   
	   length = len(self.list_quizScore)
	   print("Name: "+self.name)
	   print("")
	   print("Quiz Average: "+str(self.calcQuizStats(self.dropNumber)))
	   print("Number of Quizzes: "+str(length))
	   print("Dropped Quizzes: "+str(self.dropNumber))
	   print("Quiz Scores (* => dropped):")

	   n = length - self.dropNumber
	   for x in range(0, length):
		   if(x>n-1):
			   print(x,end="")
			   print(" - ", end="")
			   print(self.list_quizScore[x], end="")
			   print(" * ")
		   else:
			   print(x,end="")
			   print(" - ", end="")
			   print(self.list_quizScore[x])
	   print(" --------------------------------------------------- ")
	   '''
      Return string, formatted as shown in handout
      '''

def main():
	"This would create first object of Student class"
	student1 = Student("Zara")
	student1.addScore(64.0)
	student1.addScore(30.0)
	student1.addScore(10.0)
	student1.addScore(20.0)
	student1.calcQuizStats(2)
	student1.__str__()
	student2 = Student("Hu")
	student2.addScore(60.0)
	student2.addScore(35.0)
	student2.addScore(10.0)
	student2.addScore(2.0)
	student2.calcQuizStats(4)
	student2.__str__()
	'''
   Create two Students, add quiz scores to each, then
      calculated quiz stats (choose # of lowest to drop)
      and print the stringified Student.
   One of your Students should have same output as in handout;
      you can choose your own data for the second
   '''

main()




