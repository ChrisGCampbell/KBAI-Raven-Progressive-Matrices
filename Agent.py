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
        

        def calculateIndex(i, j):
                
                if i == 1:
                    j='b'#indexes relating to object attributes
                    i=i+1
                    return (i,j)
                if i == 2:
                    j='c'
                    i=i+1
                    return (i,j)

                if i == 3:
                    j = 'd'
                    i=i+1
                    return (i,j)
                    
                if i == 4:
                    j = 'e'
                    i=i+1
                    return (i,j)
                    
                if i == 5:
                    j = 'f'
                    i=i+1
                    return (i,j)
                    
                if i == 6:
                    j = 'g'
                    i=i+1
                    return (i,j)
                    
                if i == 7:
                    j = 'h'
                    i=i+1
                    return (i,j)
                    
                if i == 8:
                    j = 'i'
                    i=i+1
                    return (i,j)
                    
                if i == 9:
                    j = 'j'
                    i=i+1
                    return (i,j)

                if i == 10:
                    j = 'k'
                    i=i+1
                    return (i,j)

                if i == 11:
                    j = 'l'
                    i=i+1
                    return (i,j)

                if i == 12:
                    j = 'm'
                    i=i+1
                    return (i,j)

                if i == 13:
                    j = 'n'
                    i=i+1
                    return (i,j)

                if i == 14:
                    j = 'o'
                    i=i+1
                    return (i,j)

                if i == 15:
                    j = 'p'
                    i=i+1
                    return (i,j)

                if i == 16:
                    j = 'q'
                    i=i+1
                    return (i,j)

                if i == 17:
                    j = 'r'
                    i=i+1
                    return (i,j)

                if i == 18:
                    j = 's'
                    i=i+1
                    return (i,j)

                if i == 19:
                    j = 't'
                    i=i+1
                    return (i,j)
            
        #Gather all frames within a 2x2 problems
        def buildFrame(A, B, C, sol1, sol2, sol3, sol4, sol5, sol6):
            #build a Frames
            frameObjectsA={} #dictionary to hold objects
            frameObjectsB={}
            frameObjectsC={}
            solutionObjects1={}
            solutionObjects2={}
            solutionObjects3={}
            solutionObjects4={}
            solutionObjects5={}
            solutionObjects6={}
            
            
            i=1
            j='a'
            
            for obj in list(A.objects):
                frameObjectsA[j] = A.objects[obj].attributes
                answer = calculateIndex(i, j)
                i = answer[0]
                j = answer[1]


                print i
                print j
                
            
                #print A.objects[obj].attributes #print attributes in dictionary
                #print " "
                #for keys, values in FrameA.items():
                 #   print(keys)
                  #  print(values)

                #print FrameA #to get all values from dictionary
               # print FrameA.keys()
            #print frameObjects[1]
           # print frameObjects[2]
           
            for obj in list(B.objects):
                frameObjectsB[j] = B.objects[obj].attributes
                answer = calculateIndex(i, j)
                i = answer[0]
                j = answer[1]
                    
            for obj in list(C.objects):
                frameObjectsC[j] = C.objects[obj].attributes
                answer = calculateIndex(i, j)
                i = answer[0]
                j = answer[1]
                    
            for obj in list(sol1.objects):
                solutionObjects1[j] = sol1.objects[obj].attributes
                answer = calculateIndex(i, j)
                i = answer[0]
                j = answer[1]

            for obj in list(sol2.objects):
                solutionObjects2[j] = sol2.objects[obj].attributes
                answer = calculateIndex(i, j)
                i = answer[0]
                j = answer[1]

  
            for obj in list(sol3.objects):
                solutionObjects3[j] = sol3.objects[obj].attributes
                answer = calculateIndex(i, j)
                i = answer[0]
                j = answer[1]


            for obj in list(sol4.objects):
                solutionObjects4[j] = sol4.objects[obj].attributes
                answer = calculateIndex(i, j)
                i = answer[0]
                j = answer[1]


            for obj in list(sol5.objects):
                solutionObjects5[j] = sol5.objects[obj].attributes
                answer = calculateIndex(i, j)
                i = answer[0]
                j = answer[1]


            for obj in list(sol6.objects):
                solutionObjects6[j] = sol6.objects[obj].attributes
                answer = calculateIndex(i, j)
                i = answer[0]
                j = answer[1]


            frameObjectList = frameObjectsA, frameObjectsB, frameObjectsC, solutionObjects1,solutionObjects2, solutionObjects3,solutionObjects4, solutionObjects5, solutionObjects6

            return frameObjectList

        ##compares attributes between objects
        ##Rules governing how to handle matches
        def ProductionSystemProcedural( FrameList ):

            print FrameList
           
            if cmp(FrameList[0][1],FrameList[0][2]) == 0: #one-one-correspondance
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
                
                if cmp(FrameList[2], FrameList[3]) == 0:
                    return 1

                if cmp(FrameList[2], FrameList[4]) == 0:
                    return 2

                if cmp(FrameList[2], FrameList[5]) == 0:
                    return 3

                if cmp(FrameList[2], FrameList[6]) == 0:
                    return 4

                if cmp(FrameList[2], FrameList[7]) == 0:
                    return 5

                if cmp(FrameList[2], FrameList[8]) == 0:
                    return 6
            else:
                return 0

        ## Begin Program ##
        
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

        
        
        if problem.hasVerbal: #Verify that we are working on a verbal problem
            FrameList = buildFrame(A, B, C, solutionOne, solutionTwo, solutionThree, solutionFour, solutionFive, solutionSix)
            relationship = ProductionSystemProcedural(FrameList)
            transformationResult = ProductionSystemTransformation(relationship,FrameList)
            answer = GeneraterTester(transformationResult)
            
            ## to print items in a dictionary - print FrameList[0]
            ##print type(FrameList[0])
            #print FrameList[0][1]
            print " "
            return answer
        
        if problem.problemType == "3x3": 
            return -1
