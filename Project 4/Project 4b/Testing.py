from NeuralNetUtil import buildExamplesFromCarData,buildExamplesFromPenData
from NeuralNet import buildNeuralNet
import cPickle 
from math import pow, sqrt

def average(argList):
    return sum(argList)/float(len(argList))

def stDeviation(argList):
    mean = average(argList)
    diffSq = [pow((val-mean),2) for val in argList]
    return sqrt(sum(diffSq)/len(argList))

penData = buildExamplesFromPenData() 
def testPenData(hiddenLayers = [24]):
    return buildNeuralNet(penData,maxItr = 200, hiddenLayerList =  hiddenLayers)

carData = buildExamplesFromCarData()
def testCarData(hiddenLayers = [16]):
    return buildNeuralNet(carData, maxItr = 200, hiddenLayerList =  hiddenLayers)

def LearningWithRestarts():
    carResults = []
    penResults = []
    for _ in range(5):
        carResults.append(testCarData()[1])
        penResults.append(testPenData()[1])

    print "Car Results"
    print "Max: %f, Average: %f, StdDev: %f" % (max(carResults), average(carResults), stDeviation(carResults))
    print "Pen Results"
    print "Max: %f, Average: %f, StdDev: %f" % (max(penResults), average(penResults), stDeviation(penResults))

def VaryingHiddenLayers():
    carResults = []
    penResults = []
    for numLayers in range(0, 41, 5):
        tempCarResults = []
        tempPenResults = []
        for _ in range(5):
            tempCarResults.append(testCarData([numLayers])[1])
            tempPenResults.append(testPenData([numLayers])[1])
        carResults.append((max(tempCarResults), average(tempCarResults), stDeviation(tempCarResults)))
        penResults.append((max(tempPenResults), average(tempPenResults), stDeviation(tempPenResults)))
    print carResults
    print penResults

