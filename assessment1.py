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
        # replace special characters in the input sentence
        text = re.sub('[^A-Za-z0-9]+', ' ', text).lower()

        # split the text by spaces and put it in a list
        text_list = list(set(text.split(' ')))

        # remove blanks from list
        if "" in text_list:
            text_list.remove("")

        # find longest word's length & longest word
        matches = []
        if len(text_list) != 0:
            text_list.sort(key=len, reverse=True)
            x = len(text_list[0])
            for i in text_list:
                if len(i) == x:
                    matches.append(i)
                else:
                    break
            matches.sort()
            return ("Longest word/s: " + str(matches) + " & its length is: " + str(x))
        else:
            return None
    except Exception as e:
        print("Following exception occured while finding longest word - {}".format(e))
        return None

        
def shortest_word(text):
    """
    This functions finds & returns the shortest word in a sentence and its length.
    :param text: input sentence
    :return: shortest word in a sentence and its length
    """
    try:
        # replace special characters in the input sentence
        text = re.sub('[^A-Za-z0-9]+', ' ', text).lower()

        # split the text by spaces and put it in a list
        text_list = list(set(text.split(' ')))

        # remove blanks from list
        if "" in text_list:
            text_list.remove("")

        # find longest word's length & longest word
        matches = []
        if len(text_list) != 0:
            text_list.sort(key=len)
            x = len(text_list[0])
            for i in text_list:
                if len(i) == x:
                    matches.append(i)
                else:
                    break
            matches.sort()
            return ("Shortest word/s: " + str(matches) + " & its length is: " + str(x))
        else:
            return None
    except Exception as e:
        print("Following exception occured while finding shortest word - {}".format(e))
        return None
        
        
if __name__ == '__main__':
    text = input("Please enter the text: ")
    print(longest_word(text))
    print(shortest_word(text))
    
    

        

        
