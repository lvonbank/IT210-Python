# Levi VonBank

## Creates a student to calculate average and total quiz scores
class Student:
    ## Constructs students name and quiz variables
    # @studentName obtains the students name
    def __init__(self, studentName="NA"):
        self._name = studentName
        self._quizs = []
        self._total = 0
        self._count = 0

    ## Returns students name
    def getName(self):
        return self._name

    ## Adds the quiz score and updates the running total
    # @score obtains a score to append to the student list
    def addQuiz(self, score):
        try:
            quizScore = float(score)
            if quizScore >= 0:
                self._quizs.append(quizScore)
                self._count += 1
                self._total += quizScore
        except: pass

    ## Returns the total of the quiz scores
    def getTotalScore(self):
        return round(self._total,2)

    ## Calculates the quiz average
    # @return provides a average of the scores
    def getAverageScore(self):
        average = 0
        if self._count > 0:
            average = self._total/self._count
        return round(average,2)


if __name__ == "__main__":
    
    id_1 = Student("Jim Dean")
    id_1.addQuiz(95)
    id_1.addQuiz(53)
    id_1.addQuiz(20.4)
    print('Name:', id_1.getName())
    print('Total Score:', id_1.getTotalScore())
    print('Average Score:', id_1.getAverageScore(), '\n')
    
    id_2 = Student("Kenny Jen")
    id_2.addQuiz(86)
    id_2.addQuiz(74.3)
    id_2.addQuiz(51)
    id_2.addQuiz(64.8)
    print('Name:', id_2.getName())
    print('Total Score:', id_2.getTotalScore())
    print('Average Score:', id_2.getAverageScore(), '\n')
    
    id_3 = Student("Larry Rice")
    id_3.addQuiz(65)
    id_3.addQuiz(92.5)
    print('Name:', id_3.getName())
    print('Total Score:', id_3.getTotalScore())
    print('Average Score:', id_3.getAverageScore())