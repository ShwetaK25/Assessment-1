"""
Date: 2/22/2020
Shweta Katkade
"""
import re


def longest_word(text):
    """
    This function finds & returns the longest word in a sentence and its length.
    :param text: input sentence
    :return: longest word in a sentence and its length
    """
    try:
        #replace special characters in the input sentence
        text = re.sub('[^A-Za-z0-9]+', ' ', text)

        #split the text by spaces and put it in a list
        text_list=set(text.split(' '))

        #remove blanks from list
        if "" in text_list:
            text_list.remove("")

        #find longest word's length
        x= len(max(text_list, key=len))

        #form a list of word matching with maximum length
        matches=[]
        for i in set(text_list):
            if len(i)==x:
                matches.append(i)
        matches.sort()
        return("Longest word/s: " +str(matches)+" & its length is: "+str(x))
    except:
        return None

        
def shortest_word(text):
    """
    This functions finds & returns the shortest word in a sentence and its length.
    :param text: input sentence
    :return: shortest word in a sentence and its length
    """
    try:
        #replace special characters in the input sentence
        text = re.sub('[^A-Za-z0-9]+', ' ', text)
    
    
        #split the text by spaces and put it in a list
        text_list=set(text.split(' '))

        #remove blanks from list
        if "" in text_list:
            text_list.remove("")
          
        #find & return shortest word & its length
        x= len(min(text_list, key=len))

        #form a list of word & length matching with minimum length
        matches=[]
        for i in text_list:
            if len(i)==x:
                matches.append(i)
        matches.sort()
        return("shortest word/s: " +str(matches)+" & its length is: "+str(x))

    except:
        return None
        
        
if __name__ == '__main__':
    text = input("Please enter the text: ")
    print(longest_word(text))
    print(shortest_word(text))
    
    

        

        
