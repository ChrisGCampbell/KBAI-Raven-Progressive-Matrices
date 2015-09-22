# Your Agent for solving Raven's Progressive Matrices. You MUST modify this file.
#
# You may also create and submit new files in addition to modifying this file.
#
# Make sure your file retains methods with the signatures:
# def __init__(self)
# def Solve(self,problem)
#
# These methods will be necessary for the project's main method to run.

# Install Pillow and uncomment this line to access image processing.
#from PIL import Image
import os
import itertools
import inspect

class Agent:
    # The default constructor for your Agent. Make sure to execute any
    # processing necessary before your Agent starts solving problems here.
    #
    # Do not add any variables to this signature; they will not be used by
    # main().
    def __init__(self):
        pass

    # The primary method for solving incoming Raven's Progressive Matrices.
    # For each problem, your Agent's Solve() method will be called. At the
    # conclusion of Solve(), your Agent should return an integer representing its
    # answer to the question: "1", "2", "3", "4", "5", or "6". These integers
    # are also the Names of the individual RavensFigures, obtained through
    # RavensFigure.getName() (as Strings).
    #
    # In addition to returning your answer at the end of the method, your Agent
    # may also call problem.checkAnswer(int givenAnswer). The parameter
    # passed to checkAnswer should be your Agent's current guess for the
    # problem; checkAnswer will return the correct answer to the problem. This
    # allows your Agent to check its answer. Note, however, that after your
    # agent has called checkAnswer, it will *not* be able to change its answer.
    # checkAnswer is used to allow your Agent to learn from its incorrect
    # answers; however, your Agent cannot change the answer to a question it
    # has already answered.
    #
    # If your Agent calls checkAnswer during execution of Solve, the answer it
    # returns will be ignored; otherwise, the answer returned at the end of
    # Solve will be taken as your Agent's answer to this problem.
    #
    # Make sure to return your answer *as an integer* at the end of Solve().
    # Returning your answer as a string may cause your program to crash.
    def Solve(self,problem):
        # problem.name - string containing the name of the problem
	# problem.problemType - string containing the type of problem
	# problem.hasVisual - boolean on if pictures included
	# problem.hasVerbal - boolean on if text included
	# problem.figures - dictionary for figures & solutions
	
        #Begin Solving
        print "Working on problem: " + problem.problemType + " " + problem.name
        

        ##compares attributes between objects
        ##Rules governing how to handle matches
        def ProductionSystemProcedural( FrameList ):

            
           # print len(FrameList['B']['b']) number of values

            #print FrameList
            
            if len(FrameList['A']['a']) == len(FrameList['B']['b']): #one-one-correspondance
                    relationshipAB = "one-to-one"
                    return relationshipAB

            if cmp(FrameList[0][1], FrameList[0][2]) == 0:
                    relationshipAB = "two-to-one"
                    return relationshipAB

            if cmp(FrameList[0][1], FrameList[0][2]) == 0:
                    relationshipAB = "Three-to-one"
                    return relationshipAB
        

        def ProductionSystemTransformation(relationship,FrameList):
            if relationship == "one-to-one":
                return "same"
                

        def GeneraterTester(transformationResult):
            if transformationResult == "same":
                
                if cmp(FrameList['C']['c'], FrameList[1]['d']) == 0:
                    return 1

                if cmp(FrameList['C']['c'], FrameList[2]['e']) == 0:
                    return 2

                if cmp(FrameList['C']['c'], FrameList[3]['f']) == 0:
                    return 3

                if cmp(FrameList['C']['c'], FrameList[4]['g']) == 0:
                    return 4

                if cmp(FrameList['C']['c'], FrameList[5]['h']) == 0:
                    return 5

                if cmp(FrameList['C']['c'], FrameList[6]['i']) == 0:
                    return 6
            else:
                return 0

        def buildFrame():
            
            for obj in list(A.objects):
                AFrame[A.objects[obj].name] = A.objects[obj].attributes

            for obj in list(B.objects):
                BFrame[B.objects[obj].name] = B.objects[obj].attributes

            for obj in list(C.objects):
                CFrame[C.objects[obj].name] = C.objects[obj].attributes

            for obj in list(solutionOne.objects):
                one[solutionOne.objects[obj].name] = solutionOne.objects[obj].attributes

            for obj in list(solutionTwo.objects):
                two[solutionTwo.objects[obj].name] = solutionTwo.objects[obj].attributes

            for obj in list(solutionThree.objects):
                two[solutionThree.objects[obj].name] = solutionThree.objects[obj].attributes

            for obj in list(solutionFour.objects):
                four[solutionFour.objects[obj].name] = solutionFour.objects[obj].attributes

            for obj in list(solutionFive.objects):
                five[solutionFive.objects[obj].name] = solutionFive.objects[obj].attributes

            for obj in list(solutionSix.objects):
                six[solutionSix.objects[obj].name] = solutionSix.objects[obj].attributes


            
        ## Begin Program ##
        ## Set empty dictionaries for each frame
        AFrame = {}
        BFrame = {}
        CFrame = {}
        one = {}
        two = {}
        three = {}
        four = {}
        five = {}
        six = {}
            
        if problem.problemType == "2x2":
            A = problem.figures['A']
            B = problem.figures['B']
            C = problem.figures['C']
            solutionOne = problem.figures['1']
            solutionTwo = problem.figures['2']
            solutionThree = problem.figures['3']
            solutionFour = problem.figures['4']
	    solutionFive = problem.figures['5']
            solutionSix = problem.figures['6']

            buildFrame()
            
              
            print one
               
        
        
        if problem.hasVerbal: #Verify that we are working on a verbal problem
            relationship = ProductionSystemProcedural()
            transformationResult = ProductionSystemTransformation(relationship,FrameList)
            answer = GeneraterTester(transformationResult)
            
            ## to print items in a dictionary - print FrameList[0]
            ##print type(FrameList[0])
            #print FrameList[0][1]
            print " "
            return answer
        
        if problem.problemType == "3x3": 
            return -1
