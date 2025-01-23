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
    
##############################################################################
# Reads information about users from the file u.user. This information is stored as a list dictionaries and returned.
# Each dictionary has keys "age", "gender", "occupation", and "zip". The dictionary for user i is stored in slot i-1.
##############################################################################
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
    
##############################################################################
# Reads information about users from the file u.item. This information is stored as a list dictionaries and returned.
# Each dictionary has keys "title", "release date", "video release date", "IMDB url", and "genre". The dictionary for movie i
# is stored in slot i-1.
##############################################################################
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
    
##############################################################################
# Read ratings from a file u.data. Each rating line consisting of a user, movie, and rating are turned into a length-3 int tuple.
# A list of 100,000 such ratings is returned. The timestamps that appear in each rating are ignored. 
##############################################################################
def readRatings():
    f = open("u.data.txt")
    
    tuplesList = []
    
    for line in f:
        
        tempList = getUser(line),getMovie(line),getRating(line)
        
        tuplesList.append(tempList)
        
    return tuplesList

##############################################################################
# This function is given a bunch of ratings in the form of a list of (user, movie, rating)-tuple.
# It then creates two data structures, one from the point of view of users and one from the point of view of movies. 
# In addition, the function takes the number of users and movies as parameters and uses these to appopriately initialize
# the rating lists.
##############################################################################
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
    
##############################################################################
# This function is given a bunch of ratings in the form of a list of (user, movie, rating)-tuple.
# It then creates two data structures, one from the point of view of users and one from the point of view of movies. 
# In addition, the function takes the number of users and movies as parameters and uses these to appopriately initialize
# the rating lists.
##############################################################################   
def createGenreList():
    f = open("u.genre.txt")
    genreList = []
    for line in f:
        line.strip()
        pieces = line.split("|")
        piecesStr = pieces[0].strip()
        genreList.append(piecesStr)
        
    return genreList

##############################################################################
#
# This function takes demographic information given by gender and ageRange. It
# identifies the subpopulation of users that have the given gender and fall within
# the given ageRange. For each movie genre, the function computes the number N of ratings
# in the range ratingsRange provided by this subpopulation for movies in that genre. 
# It then returns the fraction, which is N dividied by the total number
# of ratings provided by all the users in this subpopulation. It returns this 
# fraction for the 19 genres as a length-19 list of floating points.
#
##############################################################################
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
