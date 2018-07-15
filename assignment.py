#Convert PDF to into text readable by Python
import PyPDF2 
#To clean and convert phrases into keywords
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
#The collections module includes container data types beyond the built-in types list, dict, and tuple.
import collections
#The operator module exports a set of efficient functions corresponding to the intrinsic operators of Python.
import operator
#Pandas provides high-performance, easy-to-use data structures and data analysis tools
import pandas as pd
#name of the file
filename = 'JavaBasics-notes.pdf' 
#open allows you to read the file
pdfFileObj = open(filename,'rb')
#The pdfReader variable is a readable object that will be parsed
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
#extracting the number of pages will allow us to parse through all the pages
num_pages = pdfReader.numPages
count = 0
text = ""
#This while loop will read each page
while count < num_pages:
    pageObj = pdfReader.getPage(count)
    count +=1
    text += pageObj.extractText()
#This if statement exists to check if the above library returned words. It's done because PyPDF2 cannot read scanned files.If it contains scanned files we must use textract module
if text != "":
   text = text
#We have a text variable which contains all the text derived from our PDF file.
# Now, we will clean our text variable, and return it as a list of keywords.
#The word_tokenize() function will break our text phrases into individual words
tokens = word_tokenize(text)
#we'll create a new list which contains punctuation we wish to clean
punctuations = ['(',')',';',':','[',']',',','.','!','@','#','$','/','{','}','``','~','%','^','&','*','+','-','_','=','\\','1','2','3','4','5','6','7','8','9','0','++','--','/*','*/','<','>','*=', '/=', '+=', '-=','^=','""','//','==',"''",'...','*//*','|','||','?']
#We initialize the stopwords variable which is a list of words like "I", "and", etc. that don't hold much value as keywords
stop_words = stopwords.words('english')
#We create a list comprehension which only returns a list of words that are NOT IN stop_words and NOT IN punctuations.
keywords = [word for word in tokens if not word in stop_words and not word in punctuations]
print(keywords)
#It is a list so we will first convert it to lowercase so that any words with Camelcase will be merged with the one written in lowercase.
lowerwords=[x.lower() for x in keywords]
#This counter will count all occurences of each word and convert it to dictionary
counter=collections.Counter(lowerwords)
#This generator function will sort the values in ascending order. This will convert it to a list of tuples.
sorted_k = sorted((value, key) for (key,value) in counter.items())
#This will convert text readable to Excel Spreadsheet.
pd.DataFrame(sorted_k).to_excel('frequency.xlsx', header=False, index=False)
