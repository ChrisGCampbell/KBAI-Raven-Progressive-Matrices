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
import copy
import random
import numbers

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
        def ProductionSystemProcedural():
            
            
           # print len(FrameList['B']['b']) number of values
        
            if len(AFrame) == 1 and len(BFrame) ==1:
                return "one-to-one"
                
        
        #Transformation function. Returns a possible answer in the form of a Frame#
        def ProductionSystemTransformation(relationshipAB, DFrame):
            values={}
            tempA={}
            tempB={}
            temp2={}
            changeValue=-1
            
            if len(AFrame)==1 and len(BFrame)==1: #if we are working on 1 object in each Frame
                if AFrame.values() == BFrame.values() and relationshipAB == "one-to-one":
                    for obj in list(C.objects): #generate a possible answer
                        values[C.objects[obj].name] = C.objects[obj].attributes
                    return values

                if AFrame.values() != BFrame.values(): #there is a change between AFrame and BFrame
                    for obj in list(A.objects):
                        tempA[A.objects[obj].name] = A.objects[obj].attributes
                    for obj in list(B.objects):
                        tempB[B.objects[obj].name] = B.objects[obj].attributes
                    
                    count = sum(len(v) for v in tempA.itervalues())#if FrameA and FrameB have the same length
                    count = sum(len(v) for v in tempA.itervalues())#if FrameA and FrameB have the same length
                    if count == count:#if FrameA and FrameB have the same length find the difference in values
                        Avalue = tempA.values() #change to list data structure
                        for item in Avalue:
                            AitemValues = item.values()

                        #print AitemValues

                        #print AitemValues[0]

                        Bvalue = tempB.values() #change to list data structure
                        for item in Bvalue:
                            BitemValues = item.values()

                        #print BitemValues, "checkpoint"

                        #print AitemValues[0], "checkpoint"
                        
                        for x in range(0,count-1):
                          if AitemValues[x] != BitemValues[x]:
                              changeValue = BitemValues[x]

                        try:
                            changeValue = int(changeValue)
                        except ValueError:
                            pass

                        if isinstance(changeValue, int):#suggest rotation
                            for obj in list(C.objects): #generate a possible answer
                                values[C.objects[obj].name] = C.objects[obj].attributes

                            values['c']['angle']=changeValue
                            return values
                    
                        if isinstance(changeValue, str):
                            for obj in list(C.objects): #generate a possible answer
                                values[C.objects[obj].name] = C.objects[obj].attributes

                            if changeValue == "very large" or changeValue == "small" or changeValue == "huge":
                                values['c']['size'] = changeValue
                                return values
                            elif changeValue == "square" or changeValue == "pac-man" or changeValue == "right triangle" or changeValue == "circle":
                                return values
                                values['c']['shape'] = changeValue
                            elif changeValue == "yes" or changeValue == "no" or changeValue == "right-half" or changeValue == "left-half":
                                return values
                                values['c']['fill'] = changeValue
                            else:
                                return values
                        #print changeValue, "change value"
                        #print nameValue, "name value"
                        #for item1 in value:
                        #    time =+ item1
                        #print item1.values()
                        #print item1.keys()
                        #or key, val in tempA.items():
                          #  temp2 = tempA[key][val]
                           # print temp2
                            #for key, val in temp2.values():
                             #   print temp2[key].values()
                            #print temp
                            #print temp.keys()
                            #print temp.values()
                        
                    
                            return values


            elif len(AFrame)==2 and len(BFrame)==2: #if we are working on 1 object in each Frame
                return values

            else:
                return values

        def GeneraterTester(possibleAnswer):
                #test answers
                iteration=0
                if possibleAnswer.values() == one.values():
                    return 1

                elif possibleAnswer.values() == two.values():
                    return 2

                elif possibleAnswer.values() == three.values():
                    return 3

                elif possibleAnswer.values() == four.values():
                    return 4

                elif possibleAnswer.values() == five.values():
                    return 5

                elif possibleAnswer.values() == six.values():
                    return 6
                else:
                    #ProductionSystemProcedural()
                    #if iteration >= 3:
                        return random.randint(1,6)

            

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
                three[solutionThree.objects[obj].name] = solutionThree.objects[obj].attributes

            for obj in list(solutionFour.objects):
                four[solutionFour.objects[obj].name] = solutionFour.objects[obj].attributes

            for obj in list(solutionFive.objects):
                five[solutionFive.objects[obj].name] = solutionFive.objects[obj].attributes

            for obj in list(solutionSix.objects):
                six[solutionSix.objects[obj].name] = solutionSix.objects[obj].attributes

            for obj in list(C.objects):
                DFrame[C.objects[obj].name] = C.objects[obj].attributes


            
        ## Begin Program ##
        ## Set empty dictionaries for each frame
        AFrame = {}
        BFrame = {}
        CFrame = {}
        DFrame = {}
        one = {}
        two = {}
        three = {}
        four = {}
        five = {}
        six = {}
        
        ## Retrieve values from file ##   
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

            ## build dictionary of each Frame
            buildFrame()
            
        
        if problem.hasVerbal: #Verify that we are working on a verbal problem
            relationshipAB = ProductionSystemProcedural()
            possibleAnswer = ProductionSystemTransformation(relationshipAB, DFrame)
            print possibleAnswer
            answer = GeneraterTester(possibleAnswer)
            print "answer", answer
            
            ## to print items in a dictionary - print FrameList[0]
            ##print type(FrameList[0])
            #print FrameList[0][1]
            print " "
            return answer
        
        if problem.problemType == "3x3": 
            return -1
