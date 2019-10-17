import csv


def readAndPassArgument():
    productFile = open('scrappersheet2.csv')
    productReader = csv.reader(productFile)
    productData = list(productReader)
    print(productData)
