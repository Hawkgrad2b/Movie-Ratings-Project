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




#producing visualizations
def main():
    userList = createUserList()
    movieList = createMovieList()
    rawRatings = readRatings()
    numUsers = len(userList)
    numMovies = len(movieList)
    [rLu, rLm] = createRatingsDataStructure(numUsers, numMovies, rawRatings)
    genreList = createGenreList()
    
    import matplotlib.pyplot as plt
    
    def add_to_all_elements_in_list(list1, val):
        return [elem+val for elem in list1]
    
    def plot_grouped_bar_chart(data, label_tuple, title, ylabel):
        x = [val for val in range(len(label_tuple))]  # the label locations
        width = 1/(len(data)+1)  # the width of the bars
        multiplier = 0
    
        fig, ax = plt.subplots()
    
        for attribute, measurement in data.items():
            offset = width * multiplier
            rects = ax.bar(add_to_all_elements_in_list(x, offset), measurement, width, label=attribute)
            multiplier += 1
    
        # Add some text for labels, title and custom x-axis tick labels, etc.
        ax.set_ylabel(ylabel)
        ax.set_title(title)
        ax.set_xticks(add_to_all_elements_in_list(x, width), label_tuple)
        # ax.legend(loc='upper left', ncols=3)
        ax.legend(loc='best')
        # ax.set_ylim(0, 250)
        y_max = max([max(v) for k,v in data.items()])
        ax.set_ylim(0, y_max*1.2)
    
        plt.show()
    # -------------------------------------------------
    # Sample Data1
    
    maleHigh = demGenreRatingFractions(userList, movieList, rLu, "M", [1,100], [4,5])
    
    femaleHigh = demGenreRatingFractions(userList, movieList, rLu, "F", [1,100], [4,5])
    
    label_tuple = ("Action", "Comedy", "Drama", "Horror", "Romance")
    data = {
        'Male Ratings': (maleHigh[1], maleHigh[2], maleHigh[3], maleHigh[4], maleHigh[5]),
        'Female Ratings': (femaleHigh[1], femaleHigh[2], femaleHigh[3], femaleHigh[4], femaleHigh[5]),
    }
    
    title='High Ratings From All Ages'
    ylabel=' Fractions'
    plot_grouped_bar_chart(data, label_tuple, title, ylabel)
    # -------------------------------------------------
    # Sample Data2
    
    maleLow = demGenreRatingFractions(userList, movieList, rLu, "M", [1,100], [1,2])
    
    femaleLow = demGenreRatingFractions(userList, movieList, rLu, "F", [1,100], [1,2])
    
    label_tuple = ("Action", "Comedy", "Drama", "Horror", "Romance")
    data = {
        'Male Ratings': (maleLow[1], maleLow[2], maleLow[3], maleLow[4], maleLow[5]),
        'Female Ratings': (femaleLow[1], femaleLow[2], femaleLow[3], femaleLow[4], femaleLow[5]),
    }
    
    title='Low Ratings From All Ages'
    ylabel=' Fractions'
    plot_grouped_bar_chart(data, label_tuple, title, ylabel)
    # -------------------------------------------------
    # Sample Data3
    
    maleYoung = demGenreRatingFractions(userList, movieList, rLu, "M", [20,30], [4,5])
    
    femaleYoung = demGenreRatingFractions(userList, movieList, rLu, "F", [20,30], [4,5])
    
    label_tuple = ("Action", "Comedy", "Drama", "Horror", "Romance")
    data = {
        'Male Ratings': (maleYoung[1], maleYoung[2], maleYoung[3], maleYoung[4], maleYoung[5]),
        'Female Ratings': (femaleYoung[1], femaleYoung[2], femaleYoung[3], femaleYoung[4], femaleYoung[5]),
    }
    
    title='High Ratings by Young Adults'
    ylabel=' Fractions'
    plot_grouped_bar_chart(data, label_tuple, title, ylabel)
    # -------------------------------------------------
    # Sample Data4
    
    maleOld = demGenreRatingFractions(userList, movieList, rLu, "M", [50,60], [1,2])
    
    femaleOld = demGenreRatingFractions(userList, movieList, rLu, "F", [50, 60], [1,2])
    
    label_tuple = ("Action", "Comedy", "Drama", "Horror", "Romance")
    data = {
        'Male Ratings': (maleOld[1], maleOld[2], maleOld[3], maleOld[4], maleOld[5]),
        'Female Ratings': (femaleOld[1], femaleOld[2], femaleOld[3], femaleOld[4], femaleOld[5]),
    }
    
    title='Low Ratings by Older Adults'
    ylabel=' Fractions'
    plot_grouped_bar_chart(data, label_tuple, title, ylabel)