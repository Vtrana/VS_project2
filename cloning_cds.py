# Import libraries
from urllib.request import urlopen
from bs4 import BeautifulSoup as bs
import csv

# Function to upload 5' and 3' ends of the vector to a variables
def vector_ends():
    global vector_5end
    global vector_3end
    vector_5end = open("supp_files/vector_5end.txt").read()
    vector_3end = open("supp_files/vector_3end_rev.txt").read()

# Function to scrap ORF sequence from Origene site
def get_seq():
    page = urlopen(url)
    html_body = page.read()
    html = html_body.decode("utf-8")
    soup=bs(html, "html.parser")
    global cds

    # Find and download ORF sequence
    lines = [i.get_text() for i in soup.find_all('span', {'class' : 'origene-sequence-blue'})]    
    seq=''
    for i in lines:
        seq += ''+ i
        seq_1 = seq.replace("Blue=ORF","") # remove signes at the start of the scraped sequence
        cds = ''.join(seq_1.split()) # remove white spaces in the sequence

# Function to combine all fragments and save fasta sequence in the file       
def cloning():
    name = ">"+x+"_babe \n" # create fasta type heading for the cloned sequence
    cloned = name + vector_5end + cds + vector_3end + "\n\n" # combine all pieces and add space line 
    print(x + ": New ORF is now cloned into vector") # notification for user
    print("ORF size: " + str(len(cloned)))

    file = open("supp_files/cloned_seq.txt", "a") # create file for saving cloned sequences
    file.write(cloned)
    file.close()  
    
# Main code: open file with information (gene names and URLs) and perform web scraping and cloning
vector_ends()
with open("Gene_list.csv") as f:
    reader = csv.reader(f, delimiter="\t")
    next(reader) # skip row with column names
    n = 0 # variabel to hold amount of processed sequences
    for i in reader:
        n += 1
        x = (i[0]) # assign gene name from 1st column to a variable
        url = (i[1]) # get url link for scraping sequence
        print("\nCloning: ", x) # notification for user
        name = ">"+x+"_babe \n" # header for the fasta file
        get_seq()
        cloning()
    print("\n----------------\nJob completed. Processed sequences: ", n)
        

    
