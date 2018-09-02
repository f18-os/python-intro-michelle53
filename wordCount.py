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
import re         # regular expressions

# Check if the number of arguments is correct
if ( len( sys.argv ) ) is not 3:
    print( "Please input correct number of arguments \n" )
    print( "Example: python wordCount.py input.txt output.txt" )
    exit()   

# Word Count Dictionary creation based on input
def word_count_dictionary( inputFileName ):
    wordDictionary = {} # Initialize Dictionary
    inputFile = open( inputFileName, 'r' ) # Open input file
    with inputFile as inputText: # traverse file
        for line in inputText: # traverse lines of file
            lineArray = re.split( '[ -.,;:"\n]', line ) # split the line into words based on a space seperation
            for word in lineArray:
                word = re.split('[.,;:"\n]', word)
                word = word[0].lower()
                if word == '': # Avoid empty strings
                    print()
                elif word in wordDictionary: # If word already in dictionary add 1
                    wordDictionary[ word ] += 1
                else:
                    wordDictionary[ word ] = 1 #If word not in dictionary initialize to 1
    
    inputFile.close()
    return wordDictionary

# Save dictionary to output file
def save_dictionary( wordDictionary, outputFileName ):
    with open( outputFileName, 'w' ) as output:
        for word, counts in sorted( wordDictionary.items() ): # save sorted dictionary
            output.write( word + ' ' + str( counts ) + '\n')

# Program's main
if __name__ == '__main__':
    # Open the files 
    inputFileName  = sys.argv[ 1 ]
    outputFileName = sys.argv[ 2 ]

    #Check if input file exists
    if not os.path.exists( inputFileName ):
        print ("File: " + inputFileName + " does not exist!")
        exit()

    wordDictionary = word_count_dictionary( inputFileName )
    save_dictionary( wordDictionary, outputFileName )

