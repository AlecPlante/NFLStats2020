########################### James Hong and Alec Plante | 3.20.21 ###########################

################################# Import the needed packages #################################
import requests
from bs4 import BeautifulSoup
import numpy


################################# use requests and bs4 to get soup #################################
URL = "https://www.pro-football-reference.com/years/2020/passing.htm" ## This is the website that we will be extracting data from
page = requests.get(URL) ## Load the page
soup = BeautifulSoup(page.content, "html.parser") ## Extract the page into the soup, which is one large list of 5 strings 




################################# Take the data from the soup and extract the needed info #################################

# rows = soup.find_all('tr') #Gives all of the rows in the data set
    ## Not used because we do not want the thead rows

rows = [] ## This list is to store the data from each row, with all of the given row data in 1 single index
for z in range(len(soup.find_all('tr'))): ## For all of the rows
    if (z != 30 and z != 92 and z != 61): ## Get rid of the rows that we do not want [normally I wouldn't hardcode this, but there is a time crunch, and this is only being used once]
        rows.append(soup.select("tr")[z])




################################# Set up the array #################################

ncol = 30 ## number of columns not including the index
data = [[0 for i in range((int(ncol)+1))] for j in range((len(rows)))]

#How to check column and row length
    # print ("number of rows " + str(len(data)))
    # print ("number of col " + str(len(data[0])))

# data = [['']*(int(ncol)+1)]*(len(rows)-4+1) 
        ## THIS FORM CAUSED A PROBLEM BECAUSE IT CREATES A POINTER TO 1 ARRAY. You cannot change the arrays without




################################# Find all of the column names #################################

rawLabels = soup.find("thead") ## to retrieve column title data, which is under thead

categories = rawLabels.find_all("th", scope = 'col') # find all of the individual elemnets that we want. They are listed as 'th' with scope = col

################################# We are starting to fill the data into the list #################################

## This loop fills our list with all of the data from the website

for i in range(len(data)): ## For all of the rows in data [112 rows]
    data[i][0] = i ## Creates the index in column 0
    colval = rows[i].find_all('td') ## Column values are being taken from each element of rows [112 rows] before being cleaned
    for j in range(len(colval)): ## For all of the elements in colval, which contain the data [30 entries] for a given row
        data[i][j+1]=colval[j].getText() ## Get the text/value for each cell and copy it to our list (data)
        print("data["+str(i)+"]["+str(j)+"] = " + str(data[i][j])) ## Print to check if the right information go into the right box, not necessary

## This loop takes the title for each categories entry and put it in row 0 of data

for i in range(len(categories)): # goes from 0 -> 30 tp create the column titles
    data[0][i] = categories[i].string

## This loop is to remove the stars and the pluses from the player names "Patrick Mahomes *" -> "Patrick Mahomes"
for i in range(1,len(data)): ## for all the elements in the name column
    star =str(data[i][1]).find("*") ## find the index of the first *
    if(star!=-1):   ## If there is a star in the element
        data[i][1] = str(data[i][1])[0:star-1]  ## take from the first part of the string to the space before the star


print(data)
print(len(data))




################################# Export into a csv file #################################

filename = "stats.csv" ## This is the CSV file that we will be saving to
numpy.savetxt(filename, data, delimiter = ",", fmt ='% s')
    #Uncomment this line if you want to save it again



################################################################## Notes ##################################################################

## To access the Player in:
# <th aria-label="Player" data-stat="player" scope="col" class="poptip sort_default_asc show_partial_when_sorting left">Player</th>
## ____.string

#How to check column and row length
    # print ("number of rows " + str(len(data)))
    # print ("number of col " + str(len(data[0])))