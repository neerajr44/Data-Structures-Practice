#import libraries
import csv

from urllib.request import urlopen

from math import sqrt


#function for standard deviation of list
def stddev(lst):
    mean = sum(lst) / len(lst)
    differences = [x - mean for x in lst]
    sq_differences = [d ** 2 for d in differences]
    ssd = sum(sq_differences)
    variance = ssd / (len(lst) - 1)
    sd = sqrt(variance)
    return sd

#function for mean of list
def mean(lst):
    mean = sum(lst)/len(lst)
    return mean

#from URL, write to local file
url = 'https://ptpb.pw/4dAC'
response = urlopen(url)
html = response.read()

with open('grades.csv', 'wb') as f:
    f.write(html)

#function to compute aggregate total of each student and store to list and gives roll no. of student with max. score
def aggregate():

    with open('grades.csv') as csvfile:

        headerline = next(csvfile)

        studenttotal = []
        for row in csv.reader(csvfile):
            rowtotal = 0
            for column in row[1:]:
                rowtotal += float(column)
            studenttotal.append(rowtotal)

        print(studenttotal)
        print(studenttotal.index(max(studenttotal))+1)



#function to compute mean and standard deviation of particular column
def columnstat(n):
    with open('grades.csv') as csvfile:
        headerline = next(csvfile)

        testtotal = []
        for row in csv.reader(csvfile):

            testtotal.append(float(row[n]))

        return stddev(testtotal),mean(testtotal)

#uncomment to test code


#aggregate()
#columnstat(2)







