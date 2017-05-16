import urllib

def profanity():
    texts =  open("/Users/ashokjain/Desktop/Python/movie_quotes.txt","r")
    file_contents = texts.read()
    check_profanity(file_contents)
    texts.close()

def check_profanity(text_to_check):
    connection = urllib.urlopen("http://www.wdylike.appspot.com/?q=" +text_to_check)
    output = connection.read()
    connection.close()
    if(output) == True:
        print "Profanity Alert"
    else:
        print "Document has no profanity"

print profanity()