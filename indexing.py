from xml.dom.minidom import Document
import pandas as pd
import numpy as np
import time
import string
from nltk.corpus import stopwords
# from build_index import searchable_encryption
import csv
import sys
import PyPDF2

# data = pd.read_csv("Advanced_Meter.csv")
# data.info()

# print(data.head())
n_doc=4
inverted_index = {}
# importing required modules

# creating a pdf file object
# document = sys.argv[1]
pdfFileObj = open('India.pdf', 'rb')

# creating a pdf reader object
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)

# printing number of pages in pdf file
# print(pdfReader.numPages)

# creating a page object
document = (pdfReader.getPage(0).extractText())

# extracting text from page
# print(document.extractText())
# print(document)

# closing the pdf file object
pdfFileObj.close()

# document ="India, officially the Republic of India, is a country in South Asia. It is the seventh largest country by area, the second most populous country, and the most populous democracy in the world. Bounded by the Indian Ocean on the south, the Arabian Sea on the southwest, and the Bay of Bengal on the southeast, it shares land borders with Pakistan to the west; China, Nepal, and Bhutan to the north; and Bangladesh and Myanmar to the east. In the Indian Ocean, India is in the vicinity of Sri Lanka and the Maldives; its Andaman and Nicobar Islands share a maritime border with Thailand, Myanmar, and Indonesia. The nation's capital city is New Delhi."
def text_preprocess(text):
    nltk_english_stopwords = stopwords.words('english')
    # remove punctuations
    trans = str.maketrans('', '', string.punctuation)
    text = text.translate(trans)
    # lowercase the text
    text = text.lower()
    # remove stopwords
    cleaned_text = ""
    for word in text.split():
        if word not in nltk_english_stopwords:
            cleaned_text += word + " " 
    return cleaned_text

# def createIndex(doc, i):
#     # print(inverted_index)
#     for term in doc.split():
#         if term in inverted_index:
#             inverted_index[term][i] +=1
#             # print(inverted_index)
            
#         else:
#             inverted_index[term] = ([0 for i in range(4)])
#             inverted_index[term][i]+=1
#             # print(inverted_index) 
#     return inverted_index

def createIndex(doc, i):
    # print(inverted_index)
    for term in doc.split():
        inverted_index[term]= inverted_index.get(term, [0]*1)
        inverted_index[term][i] +=1
    return inverted_index


# document = input("Please enter the document text:  ")
# document = sys.argv[1]
cleaned_doc = text_preprocess(document)
# print("\nThe cleaned text is: \n", cleaned_doc)
indexTable = createIndex(cleaned_doc, 0)
# print("\nThe inverted index table: \n", indexTable)
# for k, v in indexTable.items():
#     print(k, " : ", v)

# print(indexTable.keys())
index_header = ["keyword"]
for i in range(1, (n_doc) + 1):
    index_header.append("doc_" + str(i))

# res = indexTable.items()
# print(res)
# data = list(res)
# print("data is: \n", data)
# arr = np.array(data)
# print(arr)


# # convert array into dataframe
# DF = pd.DataFrame(arr)
 
# # save the dataframe as a csv file
# DF.to_csv("data1.csv")
csvstr=""
for key,value in indexTable.items():
    s = str(value)
    csvstr += f"{key},{s[1:-1]}" + "\n"


with open('index.csv', 'w',  encoding="utf-8") as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=index_header)
    
    # writerfile = csv.Dictwriter(csvfile)
    writer.writeheader()
    csvfile.write(csvstr)

    # # writerfile.writeheader()
    # # print(",".join(indexTable.keys()))
    # writerfile.writerow(indexTable.keys())
    # writerfile.writerows(zip(*indexTable.values()))
    
# searchable_encryption(document, indexTable)
# print(data.head())

# Doc_1 = "new home sales home forecasts"
# Doc_2 = "home sales rise in july"
# Doc_3 = "increase rise home sales in july"
# Doc_4 = "july new home sales rise"

# Docs =[Doc_1,Doc_2,Doc_3,Doc_4]
# print(Docs)

# rows, cols = (5, 5)
# arr = [[0]*cols]*rows
# print(arr)

# print(len(indexTable))

# arr = np.empty((len(indexTable), 4))
# print(arr)
# it=0
# for key in indexTable:
#     arr[it][0] = key
#     ct=0
#     for val in indexTable[key]:
#         arr[it][ct] = val
#         ct+=1
#     it+=1

# print(arr)