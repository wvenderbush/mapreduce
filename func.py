
book = open("book.txt","r")

#book = open("book_example.txt","r") ....for testing


book_text = book.read()

book_words = book_text.split();

'''print book_words
print
print "---------------------------------------------------"
print
'''

def f_single(word):
   list_single_word = filter(lambda x: x == word, book_words)
  
   return len(list_single_word)

def f_phrase(words):
   list_words = filter(lambda x: x in words, book_words)
   return len(list_words)


def most_frequent():
   word = reduce( lambda x, y: x if f_single(x) >= f_single(y) else y, book_words )
   return word




print f_single("a")
print f_single("the")
print f_phrase(["a","the"])

print f_single("we")
print f_single("do")
print f_single("not")
print f_phrase(["we", "do", "not"])

print most_frequent()
