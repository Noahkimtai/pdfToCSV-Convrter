# to use this function to convert pdf into a csv or xlxs format you must have java installed on your machine
# install tabula using a package management system such as conda or pip
#change the page value according to the pages in your doucment
# to use relative file path have the files you want to convert in the same folder as your code
# after reading the pdf file saving to a csv or xlxs format using to_excel() or to_csv()
import tabula
import glob
import pandas as pd
#you can check all the pdf files and their name inside your working directory using .glob() function
pdfFiles = glob.glob('*.pdf')
def pdfToDataframe (pdfFileName):
    dataframe = tabula.read_pdf(pdfFileName, pages=1,lattice = True)[0]
    dataframe.to_csv('csvfile.csv')
    return
pdfToDataframe('Licensed Facilities 2021- Hotel & Other Accomodations.pdf')  