#GoogleSearchTool

from googlesearch import search

request = input("What do you want to search in google?")

#you can change the stop number to a larger or bigger list
for i in search(request, start = 0, stop = 8):
    print (i)