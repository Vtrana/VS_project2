# VS_project2
subproject for "Python for Biologists HT22"

## Program aim
Program allows automatic subcloning of ORF sequences into predefined vector.

ORF sequences are "scrapped" and uploaded from the Origene.com web page.

All created sequences saved in a fasta format in new "cloned_seq.txt" file located in the "supp_files" folder.

## Installation of required libraries (Windows)
pip install urllib3 

pip install beautifulsoup4

pip install python-csv

## Files used in the program
Located in Folder **"supp_files"**

**Gene_list.csv** - holds gene names and corresponding links to the web page with sequence information

**vector_5end.txt**, **vector_3end_rev.txt** - 5' and reverse seq of 3' ends of the vector (can be modified and adopted according to the needs)

## How to run
python cloning_cds.py
