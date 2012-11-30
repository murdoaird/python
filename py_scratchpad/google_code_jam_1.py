'''
Created on 23 Nov 2012

@author: murdo
'''
import os

class MyClass(object):
    '''
    classdocs
    '''
    def __init__(self):
        '''
        Constructor
        '''        
        
        
    def do_stuff(self):
        #read file contents into a list
        with open('/tmp/B-large-practice.in') as f:
            content = f.readlines()
        f.close()
        #skip 0 
        start_pos = 1
        #as this is the number of recs
        end_pos = len(content)
        #loop through each item in list (i.e. each line in file)
        while start_pos < end_pos:
            #print content[start_pos]
            #split the line into a list of words
            word_list=content[start_pos].split()
            reverseWord = ""
            #work through the list backwards
            for word in range(len(word_list),0,-1):
                reverseWord=reverseWord+word_list[word-1]+" "
            print "Case #%s: %s" % (start_pos,reverseWord)
            start_pos +=1    
        return -1 
    
def main():
    clsTest = MyClass()
    ret_val = clsTest.do_stuff()
    print ret_val
    
if __name__ == "__main__":
    main()
