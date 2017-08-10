import urllib
from urllib import request
import os

def read_text():
    quotes = open(os.getcwd()+"/movie_quotes.txt", "r")
    contents_file = quotes.read()
    #print(contents_file)
    contents = contents_file.split()
    quotes.close()
    for content in contents:
        #print(content)
        check_profanity(content)

def check_profanity(text_to_check):
    #print(text_to_check)
    connection = urllib.request.urlopen("http://www.wdylike.appspot.com/?q="+text_to_check)
    output = connection.read()
    print(output)
    connection.close()


read_text()
