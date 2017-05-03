import cgi
import cgitb
import random
#cgitb.enable()

'''d = {}
orig = cgi.FieldStorage()
for k in orig.keys():
    d[k] = orig[k].value
    
x = d["book"]

inSight = open(str(x)+".htm", "r")
book = inSight.read()
inSight.close()
'''

#book = open("book.txt","r")

book = open("book_example.txt","r")
book_text = book.read()

book_words = book_text.split();

'''print book_words
print
print "---------------------------------------------------"
print
'''

def f_single(word):
   list_single_word = filter(lambda x: x == word, book_words)
   #return list_single_word
   return len(list_single_word)

def f_phrase(words):
	list_words = filter(lambda x: x in words, book_words)
	return len(list_words)


print f_single("a")

print f_phrase(["we", "do", "not"])
