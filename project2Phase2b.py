# "age" , "gender", "occupation", "zip"

def getID(line):
    pieces = line.split("|")
    return int(pieces[0])

def getAge(line):
    pieces = line.split("|")
    return int(pieces[1])

def getGender(line):
    pieces = line.split("|")
    return (str(pieces[2]))

def getOccupation(line):
    pieces = line.split("|")
    return (str(pieces[3]))

def getZip(line):
    pieces = (line.split("|"))
    zipString = pieces[4].strip()
    return zipString

def createUserList():
    f = open("u.user.txt")
    userList = []
    
    for line in f:
        tempDictionary = {"age":0,"gender":0,"occupation":0,"zip":0}
        
        tempDictionary["age"] = getAge(line)
        tempDictionary["gender"] = getGender(line)
        tempDictionary["occupation"] = getOccupation(line)
        tempDictionary["zip"] = getZip(line)
        
        
        userList.append(tempDictionary)
        
    return userList


def getTitle(line):
    pieces = line.split("|")
    return pieces[1]

def getReleaseDate(line):
    pieces = line.split("|")
    return (str(pieces[2]))

def getVideoReleaseDate(line):
    pieces = line.split("|")
    return (str(pieces[3]))

def getIMDBurl(line):
    pieces = (line.split("|"))
    zipString = pieces[4].strip()
    return zipString

def getGenre(line):
    pieces = line.split("|")
    genreList = pieces[5:]
    newGenreList = []
    for piece in genreList:
        part = int(piece)
        
        newGenreList.append(part)
    return newGenreList

def createMovieList():
    f = open("u.item.txt", encoding="windows-1252")
    movieList = []
    
    for line in f:
        tempDictionary = {"title":0,"release date":0,"video release date": "","IMDB url":0, "genre":0}
        
        tempDictionary["title"] = getTitle(line) 
        tempDictionary["release date"] = getReleaseDate(line)
        tempDictionary["video release date"] = getVideoReleaseDate(line)
        tempDictionary["IMDB url"] = getIMDBurl(line)
        tempDictionary["genre"] = getGenre(line)
        
        
        movieList.append(tempDictionary)
        
    return movieList

def getUser(line):
    pieces = line.split("\t")
    return int(pieces[0])

def getMovie(line):
    pieces = line.split("\t")
    return int(pieces[1])

def getRating(line):
    pieces = line.split("\t")
    return int(pieces[2])

def readRatings():
    f = open("u.data.txt")
    
    tuplesList = []
    
    for line in f:
        
        tempList = getUser(line),getMovie(line),getRating(line)
        
        tuplesList.append(tempList)
        
    return tuplesList


def createRatingsDataStructure(numUsers, numItems, ratingTuples):
    
    rLu=[]
    rLm=[]
    
    for user in range(numUsers):
        
        tempDict = {}
        
        for i in ratingTuples:
            if (i[0] == user + 1):
                tempDict[i[1]] = i[2] 
                
        rLu.append(tempDict)

    for movie in range(numItems):
        
        tempDict={}
        
        for i in ratingTuples:
            if (i[1] == movie + 1):
                tempDict[i[0]] = i[2]
                         
        rLm.append(tempDict)
        
    return rLu, rLm

    
def createGenreList():
    f = open("u.genre.txt")
    genreList = []
    for line in f:
        line.strip()
        pieces = line.split("|")
        piecesStr = pieces[0].strip()
        genreList.append(piecesStr)
        
    return genreList



def demGenreRatingFractions(userList, movieList, rLu, gender, ageRange, ratingRange):

    genreList= createGenreList()
    
    fractions = [0] * len(createGenreList())
    
    subPopulation = []
    
    denominator = 0
    
    for user in range(len(userList)):
        if (gender == "A") or (userList[user]["gender"] == gender):
            if (userList[user]["age"] >= ageRange[0]) and (userList[user]["age"] < ageRange[1]):
                subPopulation.append(user)
           
    for user in subPopulation:
        userDict = rLu[user]
        
        denominator = denominator + len(userDict) 
    
        for movie in userDict.items():
            if (movie[1] >= ratingRange[0]) and (movie[1] <= ratingRange[1]):
                for i in range(len(genreList)):
                    if movieList[movie[0]-1]["genre"][i] == 1:
                        fractions[i] += 1
    
    for i in range(len(fractions)):   
        if denominator == 0:
            fractions[i] =  None
        else:
            fractions[i] = fractions[i] / denominator
    
    return fractions 
###############################################################################
#project2Phase2a - Start

def randomPrediction(u, m):
    import random
    return random.randint(1,5)

def meanUserRatingPrediction(u, m, rLu):
    userMovies = rLu[u - 1] 
    numRatings = 0
    totalRatingsValue = 0
    for movie in userMovies.items():
        totalRatingsValue += movie[1]
        numRatings += 1 
        
    if len(userMovies) == 0:
        return None
    
    return totalRatingsValue / numRatings

def meanMovieRatingPrediction(u, m, rLm):
    movieRatings = rLm[m -1]
    numRatings = 0
    totalRatingsValue = 0
    for rating in movieRatings.items():
        totalRatingsValue += rating[1]
        numRatings += 1 
        
    if len(movieRatings) == 0:
        return None
    
    return totalRatingsValue / numRatings

def demRatingPrediction(u, m, userList, rLu):
    userGender = userList[u-1]["gender"]
    userAgeLow = userList[u-1]["age"] - 5
    userAgeHigh = userList[u-1]["age"] + 5
    subPop = []
    numRatings = 0
    totalRatings = 0
    
    for user in range(len(userList)):
        if (userList[user]["gender"] == userGender):
            if (userList[user]["age"] >= userAgeLow) and (userList[user]["age"] <= userAgeHigh):
                subPop.append(user)

    subPop.remove(u-1)
    
    for u1 in subPop:
        
        if m not in rLu[u1]:
            continue
        else:
            totalRatings += rLu[u1][m]
            numRatings += 1
    
    if len(subPop) == 0:
        return None
    
    if numRatings == 0:
        return 0
    
    return totalRatings / numRatings

def genreRatingPrediction(u, m, movieList, rLu):
    subMovies = []
    numRatings = 0
    totalRatings = 0 
    
    refGenre = movieList[m-1]["genre"]
    
    for movie in range(len(movieList)):
        for i in range(len(refGenre)):
            if movieList[movie]["genre"][i] == 1 and movieList[m-1]["genre"][i] == 1:
                subMovies.append(movie)
                break

    subMovies.remove(m-1)
    
    for m1 in subMovies:
        
        if m1+1 not in rLu[u-1]:
            continue
        else:
            totalRatings += rLu[u-1][m1+1]
            numRatings += 1
            
    if len(subMovies) == 0:
        return None 
    
    if numRatings == 0:
        return 0
    
    return totalRatings / numRatings
     

def partitionRatings(rawRatings, testPercent):
    import random
    newRawRatings = []
    
    for i in rawRatings:
        newRawRatings.append(i)
        
    random.shuffle(newRawRatings)
    
    numTests = int(len(rawRatings) * testPercent / 100)
    
    trainingSet = newRawRatings[numTests:]
    
    testingSet = newRawRatings[:numTests]      
    
    return [trainingSet, testingSet]


def rmse(actualRatings, predictedRatings):
    import math
    
    denom = 0
    totalRMSE = 0
    for i in range(len(actualRatings)):
        if predictedRatings[i] != None:
            totalRMSE += (actualRatings[i] - predictedRatings[i])**2
            denom += 1
        
    answer = math.sqrt(totalRMSE / denom)
    return answer
        
def createActualRatings(rawRatings):
    actualRatings = []
    for i in rawRatings:
        list(i)
        actualRatings.append(i[2])
    return actualRatings



def main1():
    import time

    start_time = time.time()  # get the current time
    
    randomPredictionListRMSE = []
    meanUserRatingPredictionListRMSE = []
    meanMovieRatingPredictionListRMSE = []
    demRatingPredictionListRMSE = []
    genreRatingPredictionListRMSE = []
    
    rawRatings = readRatings() 
    userList = createUserList()
    movieList = createMovieList()
    numUsers = len(userList)
    numItems = len(movieList)

    for repeat in range(10):
        
        [trainingSet, testingSet] = partitionRatings(rawRatings, 20)
        
        [TrRLu, TrRLm] = createRatingsDataStructure(numUsers, numItems, trainingSet)
        

        randomPredictionList = []
        meanUserRatingPredictionList = []
        meanMovieRatingPredictionList = []
        demRatingPredictionList = []
        genreRatingPredictionList = []
        
        for (u, m, r) in testingSet:
            randomPredictionList.append(randomPrediction(u, m))
            
            meanUserRatingPredictionList.append(meanUserRatingPrediction(u, m, TrRLu))
            
            meanMovieRatingPredictionList.append(meanMovieRatingPrediction(u, m, TrRLm))
            
            demRatingPredictionList.append(demRatingPrediction(u, m, userList, TrRLu))
            
            genreRatingPredictionList.append(genreRatingPrediction(u, m, movieList, TrRLu))
            
        
        actualRatings = createActualRatings(testingSet)
        
        randomPredictionListRMSE.append(rmse(actualRatings, randomPredictionList))
        
        meanUserRatingPredictionListRMSE.append(rmse(actualRatings, meanUserRatingPredictionList))
        
        meanMovieRatingPredictionListRMSE.append(rmse(actualRatings, meanMovieRatingPredictionList))
        
        demRatingPredictionListRMSE.append(rmse(actualRatings, demRatingPredictionList))
        
        genreRatingPredictionListRMSE.append(rmse(actualRatings, genreRatingPredictionList))
        
        
    import matplotlib.pyplot as plt


    def draw_boxplot(data, labels):
        plt.boxplot(x=data, labels=labels)
        plt.title("Algorithm performance comparison")
        plt.ylabel("RMSE values")
        plt.show()
        plt.close()

    # ---------------
    # Data
    algo1 = randomPredictionListRMSE
    algo2 = meanUserRatingPredictionListRMSE
    algo3 = meanMovieRatingPredictionListRMSE
    algo4 = demRatingPredictionListRMSE
    algo5 = genreRatingPredictionListRMSE

    data = [algo1, algo2, algo3, algo4, algo5]
    labels = ['rp',  'murp', 'mmrp', 'drp', 'grp']

    draw_boxplot(data, labels)
    
    end_time = time.time()  # get the current time again

    elapsed_time = end_time - start_time  # compute the elapsed time

    print("Elapsed time:", elapsed_time, "seconds")  # print the elapsed time
    