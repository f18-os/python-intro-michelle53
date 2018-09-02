"""
Title: Word Count Program
Author: Michelle Patino
Last Modified: September 1, 2018
Specifications:
-takes as input the name of an input file and output file
    -$ python wordCount.py input.txt output.txt
-keeps track of the total the number of times each word occurs in the text file
-excluding white space and punctuation
-is case-insensitive
-print out to the output file (overwriting if it exists) the list of words 
    sorted in descending order with their respective totals separated by a space,
    one word per line
"""
import sys        # command line arguments
import os         # checking if file exists

# Check if the number of arguments is correct
if ( len( sys.argv ) ) is not 3:
    print( "Please input correct number of arguments \n" )
    print( "Example: python wordCount.py input.txt output.txt" )
    exit()   

# Word Count Dictionary creation based on input
def word_count_dictionary( inputFileName, outputFileName ):
    
    word_dictionary = {} # Initialize Dictionary
    inputFile = open( inputFileName, 'r' ) # Open input file

    with inputFile as inputText: # traverse file
        for line in inputText: # traverse lines of file
            lineArray = line.split( ' ' ) # split the line into words based on a space seperation
            for word in lineArray:
                if word.lower() in word_dictionary: # If word already in dictionary add 1
                    word_dictionary[ word.lower() ] += 1
                else:
                    word_dictionary[ word.lower() ] = 1 #If word not in dictionary initialize to 1
    
    inputFile.close()

# Program's main
if __name__ == '__main__':
    # Open the files 
    inputFileName  = sys.argv[ 1 ]
    outputFileName = sys.argv[ 2 ]

    #Check if input file exists
    if not os.path.exists( inputFileName ):
        print ("File: " + inputFileName + " does not exist!")
        exit()

    word_count_dictionary( inputFileName, outputFileName  )

