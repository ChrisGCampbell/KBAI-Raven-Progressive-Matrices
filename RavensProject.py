# DO NOT MODIFY THIS FILE.


import os
import sys
from Agent import Agent
from ProblemSet import ProblemSet


def main():
    sets=[] # The variable 'sets' stores multiple problem sets.
            # Each problem set comes from a different folder in /Problems/
            # Additional sets of problems will be used when grading projects.


    r = open("Problems" + os.sep + "ProblemSetList.txt")    # ProblemSetList.txt lists the sets to solve.
    line = getNextLine(r)                                   # Sets will be solved in the order they appear in the file.
    while not line=="":
        sets.append(ProblemSet(line))
        line=getNextLine(r)

    # Initializing problem-solving agent from Agent.java
    agent=Agent()

    # Running agent against each problem set
    results=open("ProblemResults.csv","w")
    setResults=open("SetResults.csv","w")       # Set-level summaries will be written to SetResults.csv.
    results.write("Problem,Agent's Answer,Correct?,Correct Answer\n")
    setResults.write("Set,Correct,Incorrect,Skipped\n")
    for set in sets:
        for problem in set.problems:   # Your agent will solve one problem at a time.
            #try:
            problem.setAnswerReceived(agent.Solve(problem))

            result=problem.name + "," + str(problem.givenAnswer) + "," + problem.getCorrect() + "," + str(problem.correctAnswer)

            results.write("%s\n" % result)
            #except:
            #    print("Error encountered in " + problem.name + ":")
            #    print(sys.exc_info()[0])
            #    result=problem.name + "," + str(problem.givenAnswer) + ",Error," + str(problem.correctAnswer)
            #    results.write("%s\n" % result)
        setResult=set.name + "," + str(set.getTotal("Correct")) + "," + str(set.getTotal("Incorrect")) + "," + str(set.getTotal("Skipped"))
        setResults.write("%s\n" % setResult)
    results.close()
    setResults.close()

def getNextLine(r):
    return r.readline().rstrip()

if __name__ == "__main__":
    main()
