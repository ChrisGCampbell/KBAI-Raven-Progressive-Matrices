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
        def ProductionSystemProcedural():
            
            
           # print len(FrameList['B']['b']) number of values
        
            if len(AFrame) == len(BFrame): #one-one-correspondance
                    relationshipAB = "one-to-one"
                    print relationshipAB, "procedural"
                    return relationshipAB
            
            elif len(AFrame) > len(BFrame): #deletion
                    relationshipAB = "deletion"
                    len(AFrame) < len(BFrame)
                    return relationshipAB

            elif len(AFrame) < len(BFrame): #addition
                    relationshipAB = "addition"
                    len(AFrame) < len(BFrame)
                    return relationshipAB 
            
            else:                           # undefined
                relationshipAB = "undefined"
                return relationshipAB
        
        
        def ProductionSystemTransformation(relationshipAB):
            if relationshipAB == "one-to-one":
                print relationshipAB, "transformation"

                if AFrame.values() == BFrame.values(): #there are 1 object in each FrameA(a), FrameB(b)
                    print "one-object-same"
                    return "one-object-same"
                
                
                elif len(AFrame) == 2 and len(BFrame) == 2: #if there are 2 objects in the FrameA(a,b), FrameB(c,d)
                        if AFrame.values() == BFrame.values(): #all attributes are the same
                           print "two-objects-same"
                           return "two-objects-same"
                

                        if AFrame.values() != BFrame.values(): #attributes are different
                            
                                if AFrame['a']['shape'] != BFrame['c']['shape'] or AFrame['b']['shape'] != BFrame['d']['shape']:
                                    print "shape-change"
                                    return "shape-change"
                                elif AFrame['a']['size'] != BFrame['c']['size'] or AFrame['b']['size'] != BFrame['d']['size']:
                                    print "size-change"
                                    return "size-change"
                                elif AFrame['a']['fill'] != BFrame['c']['fill'] or AFrame['b']['fill'] != BFrame['d']['fill']:
                                    print "fill-change"
                                    return "fill-change"
                                try:
                                    if AFrame['a']['angle'] != BFrame['c']['angle']:
                                        print "a-c-angel-change"
                                        return "a-c-angle-change"
                                except KeyError:
                                    pass
                                try:
                                    if AFrame['b']['angle'] != BFrame['d']['angle']:
                                        print "b-d-angel-change"
                                        return "b-d-angle-change"
                                except KeyError:
                                    pass
                                try:
                                    if AFrame['a']['inside'] != BFrame['c']['inside']:
                                        print "a-c-inside-change"
                                        return "a-c-inside-change"
                                except KeyError:
                                    pass
                                try:
                                    if AFrame['b']['inside'] != BFrame['d']['inside']:
                                        print "b-d-inside-change"
                                        return "b-d-inside-change"
                                except KeyError:
                                    pass
                           
                else:
                    print "no-rule"
                    return "no-rule"
            

        def GeneraterTester(transformationResult):
            if transformationResult == "one-object-same":
                
                if CFrame.values() == one.values():
                    return 1

                elif CFrame.values() == two.values():
                    return 2

                elif CFrame.values() == three.values():
                    return 3

                elif CFrame.values() == four.values():
                    return 4

                elif CFrame.values() == five.values():
                    return 5

                elif CFrame.values() == six.values():
                    return 6
                else:
                    return 8

            if transformationResult == "two-object-same":
                
                if CFrame.values() == one.values():
                    return 1

                elif CFrame.values() == two.values():
                    return 2

                elif CFrame.values() == three.values():
                    return 3

                elif CFrame.values() == four.values():
                    return 4

                elif CFrame.values() == five.values():
                    return 5

                elif CFrame.values() == six.values():
                    return 6
                else:
                    return 8

            
            if transformationResult == "shape-change":
                if len(AFrame) == 2 and len(BFrame) == 2:
                    try:
                        if AFrame['a']['shape'] != BFrame['c']['shape']:
                            shape = BFrame['c']['shape']
                            DFrame = CFrame.values
                            DFrame['e']['shape'] = shape
                            if DFrame.values == one.values():
                                return 1
                            elif DFrame.values == two.values():
                                return 2
                            elif DFrame.values == three.values():
                                return 3
                            elif DFrame.values == four.values():
                                return 4
                            elif DFrame.values == five.values():
                                return 5
                            elif DFrame.values == six.values():
                                return 6
                            else:-1
                    except KeyError:
                            pass
                            

                    try:
                        if AFrame['b']['shape'] != BFrame['d']['shape']:
                            shape = BFrame['c']['shape']
                            DFrame = CFrame.values
                            DFrame['f']['shape'] = shape
                            if DFrame.values == one.values():
                                return 1
                            elif DFrame.values == two.values():
                                return 2
                            elif DFrame.values == three.values():
                                return 3
                            elif DFrame.values == four.values():
                                return 4
                            elif DFrame.values == five.values():
                                return 5
                            elif DFrame.values == six.values():
                                return 6
                            else:
                                -1
                    except KeyError:
                            pass
            if transformationResult == "KeyError":
                return 8
            if transformationResult == "undefined":
                return 8
            else:
                return 8

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
            transformationResult = ProductionSystemTransformation(relationshipAB)
            answer = GeneraterTester(transformationResult)
            print "final ", answer
            
            ## to print items in a dictionary - print FrameList[0]
            ##print type(FrameList[0])
            #print FrameList[0][1]
            print " "
            return answer
        
        if problem.problemType == "3x3": 
            return -1
