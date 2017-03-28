'''
The data that the algorithm is going to “learn” from is a set of 8,529 movie reviews
(provided in the file movieReviews.txt posted under Programming Projects in Piazza) 
in which the sentiment	of each	review	has been manually rated	on a scale	
from 0 to 4. The sentiment labels are:
0	- negative
1	- somewhat	negative
2	- neutral
3	- somewhat	positive
4	- positive 
The goal of the	assignment is to use the provided data file to develop 
an algorithm that will automatically score the sentiment of a new 
review that the	user inputs'''
import os, re, sys, codecs,  argparse, operator

class MovieReview:
    def _init_(self,pos_score,neg_score):
        self.pos_score = pos_score
        self.neg_score = neg_score
        self.obj_score = 1.0 - (self.pos_score + self.neg_score)
        
    def __str__(self):
        """Prints just the Pos/Neg scores for now."""
        s = ""
        s += self.synset.name + "\t"
        s += "PosScore: %s\t" % self.pos_score
        s += "NegScore: %s" % self.neg_score
        return s    
        
    def word_feats(words):
        return dict([(word, True) for word in words])    
    
        
def main():
    #open the file
    fin = open("moviesReviews.txt","r")
    #read the file into text
    text = fin.read()
    
    total = 0 
    count = 0
    #Make string uniform and split words into tokens based on spaces.
    lines = text.split('\n')
   
    
    
    #dictionary key : line value: count
    dict = {}
    wordToken=[]
    sentences=[]
    for line in lines:
    # skip empty words
        if line != '':
            if not line in dict.keys():
            # first time entry
                dict[line] = 1
            else:
            # increment the value(count) if line exists in the dictionary
                dict[line] += 1
        
# looping the dictionary(dict)
    for key in dict.keys():
        
        
    # printing key(word), value(count)
        print (dict[key],key)
    for line in fin:
        # tokenize each review
        reviewToken = line.split()
        if reviewToken[0].isdigit():
            count = count + 1    
        
            print(count)    
    
    
    
    
        #
    
"""   # for word in lines:
     #   if word not in dict:
     #       dict[word] = 1
      #  else:
      #      dict[word] += 1
        """
    
    
    
    
main()