import csv


def readAndPassArgument():
    with open('ScrapperSheet2.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        # line_count = 0
        for row in csv_reader:
            print(f'{row[1]}')
            
            # line_count += 1
            # print(f'Processed {line_count} lines.')


# function call
readAndPassArgument()














#----------------------------------------------------------------------------------------------------------------------------------------#
# productFile = open('scrappersheet2.csv')
#     productReader = csv.reader(productFile)
#     # productData = list(productReader)
#     for partNum in productReader[][2]:
#         print(str(partNum)) #prints second column: part number
