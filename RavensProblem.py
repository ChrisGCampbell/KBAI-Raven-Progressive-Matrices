# DO NOT MODIFY THIS FILE.

# A single Raven's Progressive Matrix problem, represented by a type (2x2
# or 3x3), a String name, and a dictionary of figures.
class RavensProblem:
    # Initializes a new Raven's Progressive Matrix problem given a name, a
    # type, and a correct answer to the problem. Also initializes a blank
    # dictionary representing the figures in the problem.
    #

    def __init__(self, name, problemType, correctAnswer, hasVisual, hasVerbal):
        # The name of the problem, typically the set followed by an identifier,
        # such as "Basic Problem B-02".
        self.name=name

        # The type of problem, either 2x2 or 3x3.
        self.problemType=problemType


        self.correctAnswer=correctAnswer

        # Whether or not the problem has visual representations available.
        self.hasVisual=hasVisual

        # Whether or not the problem has verbal representations available.
        self.hasVerbal=hasVerbal


        self.figures={}

        # Whether or not an answer has been received. As soon as your agent has
        # given an answer to this problem, answerReceived will be set to true.

        self.answerReceived=False


        self.givenAnswer=-1

    # Returns the correct answer to the problem.

    # This method is provided to enable your Agent to participate in learning
    # and meta-reasoning by reflecting on its past incorrect answers. Using
    # this method is completely optional.
    def checkAnswer(self, givenAnswer):
        self.setAnswerReceived(givenAnswer)
        return self.correctAnswer



    def setAnswerReceived(self, givenAnswer):
        if not self.answerReceived:
            self.answerReceived=True
            self.givenAnswer=int(givenAnswer)


    def getCorrect(self):
        if self.givenAnswer==self.correctAnswer:
            return "Correct"
        elif self.givenAnswer<0:
            return "Skipped";
        else:
            return "Incorrect"

