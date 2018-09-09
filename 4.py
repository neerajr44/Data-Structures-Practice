from urllib.request import urlopen

#import from URL, write to file
url = 'https://goo.gl/7oKHii'
response = urlopen(url)
html = response.read()

with open('Names.txt', 'wb') as f:
    f.write(html)

#load names in file to list
f = open('Names.txt','r')
nameslist = []
for line in f:  # loop over the lines in the file
    line = line.strip() # strip the line breaks
    nameslist.append(line) # append the word to the list




# Function to return the distance between two strings: a and b - Levenshtein distance to compute similarity measure : lower is more similar
def levenshtein(a, b):

    n, m = len(a), len(b)
    if n > m:
        # Make sure n <= m, to use O(min(n,m)) space
        a, b = b, a
        n, m = m, n

    current = range(n + 1)
    for i in range(1, m + 1):
        previous, current = current, [i] + [0] * n
        for j in range(1, n + 1):
            add, delete = previous[j] + 1, current[j - 1] + 1
            change = previous[j - 1]
            if a[j - 1] != b[i - 1]:
                change = change + 1
            current[j] = min(add, delete, change)

    return current[n]

#Take the input name
x = input("Enter the name\n")

#Create dictionary to store name and corresponding lv values
keyvaluepair = {}
for i in nameslist:
    keyvaluepair[i] = levenshtein(x,i)

s = [(k, keyvaluepair[k]) for k in sorted(keyvaluepair, key=keyvaluepair.get)]

sortednames = []
for k,v in s:
    sortednames.append(k)

print (sortednames[:5])


















