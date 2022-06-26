####################################################
# CS 31, Prof. Muldrow
# Name: Victoria Clemente
# Assignment: Project 3
# Due Date: May 31st, 2022
####################################################
## open,file loop though contents, strip \n, put in a list, save in dictionary
def main():
#open and read the file, and strip \n
    tvShows = open('tv_shows.txt','r')
    title = tvShows.readline().upper()#.rstrip('\n')
    showsDic = {}
    while title != '':
        title = title.rstrip('\n')
        code = tvShows.readline().rstrip('\n')
        #call grab code func,organize data
        yearAired = startYear(code)
        networkID = getnetworkID(code)
        endYear = getEndYear(code,yearAired)
        actor1 = tvShows.readline().rstrip('\n')
        actor2 = tvShows.readline().rstrip('\n')
        actor3 = tvShows.readline().rstrip('\n')
        actor4 = tvShows.readline().rstrip('\n')
        #store all processed data in this array of 7 elements
        showsDic[title] = [yearAired,endYear,networkID, actor1, actor2, actor3, actor4]
        title = tvShows.readline().upper()
    tvShows.close()
    #print(showsDic) def another loop to display data
    for title,values in showsDic.items():
        print(title,' aired from ',values[0],' to ',values[1],' on ',values[2],'.',sep='')
        print('It starred ',values[3],', ',values[4],', ',values[5],', and ',values[6],'.',sep='')
        print()

#grab the code function
#5 digits, first two = year it aired, next two =number of seasons, last num = network id
#variable_name[start:stop:step]
# 1=ABC, 2=CBS, 3=NBC, 4=FOX
def getnetworkID(code):
    networkNum = code[-1:]
    if networkNum == '1':
        return 'ABC'
    elif networkNum == '2':
        return 'CBS'
    elif networkNum == '3':
        return 'NBC'
    elif networkNum == '4':
        return 'FOX'
    else:
        return 'Network ID Error'

#get the year it aired
def startYear(code):
    year = int(code[0:2])
    if  year >= 0 and year <= 18:
        year += 2000
        return year
    elif year > 18:
        year += 1900
        return year

#get the year it stopped airing
def getEndYear(code,yearAired):
    endYear = int(code[2:4])
    endYear += yearAired
    return endYear

main()