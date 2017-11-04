#! Python3
from __future__ import print_function
import unittest
import pprint
import string


'''
Description:
    This program has a few methods that will analyze a given text. The program will do the following:

    * Leela is the coolest
    * Count the number of words in a text
    * Count the number of unique words in a text
    * Produce a dictioanry of words and the number of times each word is used (in the debugger, or trace)
    * Will count the number of sentences in a text
    * Will give the average number of words per sentence

    The program is test driven, and works with multiple cases demonstrated below.
    
    note: *** NEED *** finish by having program analyze text from a .txt file on the command line
    
                    
Author: Zachary Stall
Version: 2

'''
# trace: if set to true will print information from funcations for debugging
trace  = False
# trace2: if set to true will print out results for methods given texts
trace2 = True

# create a var with the set of punctuation char to be excluded for unique word count
exclude = set(string.punctuation)

# get the total number of words from the text
def countingwords(text):
    numWords = 0                                            # var to store total
    
    words = text.split()                                    # split text into a list of words
    numWords = len(words)                                   # store the length of list to get total words
    return numWords                                         # return total

# method to find only unique words 
def getuniquewords(text):
    wordsDic = {}                                           # create a dictionary to seperate out uniques words

    # remove puncuation, make all lowercase, and put all words into a list
    words = ''.join(ch for ch in text if ch not in exclude).lower().split()
    

    # create a loop to iterate through the list of words and create a dictionary to count unique words
    for i in words: 
        wordsDic.setdefault(i, 0)                           # set a default key value pair for words not yet in dictionary
        wordsDic[i] = wordsDic[i] + 1                       # add to counter if words are re-used

    if trace:
        pprint.pprint(wordsDic)
        print('The number of unique words are: %d' % len(wordsDic))

    return len(wordsDic)


def countingsentences(text):
    msg = type(text)()
    a = 1   # Set length of slices

    # declare all terminating values
    per = '.'
    exc = '!'
    que = '?'
    # create a list and dictionary to store sentences
    senList = []
    senDic  = {}
    # var to store the number of sentences
    numSentences = 0

    # loop to format sentences
    for c in text:
        msg += c                                    # each pass through the loop add a letter to be checked for a terminator
        if c == per or c == exc or c == que:        # check for terminators (end of sentences)
            msg = " ".join(msg.split())             # format sentences to get rid of unwanted white space
            senList.append(msg)                     # add sentence to list
            msg = type(text)()                      # empty msg to load next sentence

    for i in senList:                               # second loop to load sentences into a dictionary
        senDic.setdefault(i, 0)                     # create a key value for each new dictionary
        senDic[i] = senDic[i] + 1                   # each time a phrase is used, increment it
    
    numSentences = sum(senDic.values())             # sum dictionary values to get total sentences

    # print to console if trace is True
    if trace:
        pprint.pprint(senDic)
        print(sum(senDic.values()))

    # return number of sentences
    return numSentences

def avgwords(text):
    avg = 0.0
    sentNum = countingsentences(text)
    if sentNum == 0:
        sentNum = 1
    wordNum = countingwords(text)

    avg = wordNum / sentNum

    if trace:
        print('The average number of words per sentence is: %.2f' % avg)

    return avg
    


def results_words_analyzer(message):
    if trace2:
        text = " ".join(message.split())
        print('*****************************************************************')
        print('For the text: \n' + text)
        print()
        print('The number of sentences is: ' + str(countingsentences(text)))
        print('The number of words is: ' + str(countingwords(text)))
        print('The number of unique words is: ' + str(getuniquewords(text)))
        print('The average words per sentence is: ' + str(avgwords(text)))
        print('*****************************************************************')
        print()


t   = 'Hello world.'
t1  = 'Hello world. How are you? I love that! The world is a big place.' 
t2  = 'Hello you. Hello you. How are you? What did you say!'
t3  = 'Hi. I said hi. Hi!'
t4  = '''   What’s this? A real NFL trade deadline, with real trades?
            Big names on the move? Contenders beefing up for the stretch run?

            This kind of thing is supposed to happen in baseball and basketball,
            but not in the NFL, where the midseason trade deadline traditionally
            comes and goes with all the excitement of a Chicago Bears three-and-out.
            Sunday’s victory over Deshaun Watson’s Texans was breathless, three-hour
            video of Wilson basically screaming, “Get me some help!” After Wilson won that game by himself,
            the Seahawks finally, at long last, made a real investment in their offensive line,
            trading two picks and cornerback Jeremy Lane to Houston for real-life left tackle Duane Brown.
            Nitpick all you want about how Brown held out nearly half the season in Houston and is
            32 years old. He’s Anthony Munoz compared to what the Seahawks have been running out there at
            left tackle the past few years. This can only help Wilson’s protection and the Seattle run game,
            which is currently a myth. '''



class TestWordAnalyzer(unittest.TestCase):
   
    def test_countingwords(self):
        self.assertEqual(countingwords(t), 2)
        self.assertEqual(countingwords(t1), 14)

    def test_getuniquewords(self):
        self.assertEqual(getuniquewords(t3), 3)
        self.assertEqual(getuniquewords(t2), 7)

    def test_avgwords(self):
        self.assertEqual(avgwords(t1), 3.5)

    def test_countingsentences(self):
        self.assertEqual(countingsentences(t2), 4)
        self.assertEqual(countingsentences(t), 1)
        self.assertEqual(countingsentences(" "), 0)
        
    def test_countingsamesentences(self):
        self.assertEqual(countingsentences(t2), 4)
        results_words_analyzer(t2)
        self.assertEqual(countingsentences("Why did you come here?"), 1)
        results_words_analyzer("Why did you come here?")
        self.assertEqual(countingsentences("Are you crazy? I love you!"), 2)
        results_words_analyzer("Are you crazy? I love you!")
    def test_formatingcntsent(self):
        
        self.assertEqual(countingsentences(t4), 10)
        self.assertEqual(countingwords(t4), 167)
        self.assertEqual(getuniquewords(t4), 121)
        results_words_analyzer(t4)           
                
        self.assertEqual(countingsentences(" "), 0)
        results_words_analyzer(" ")

if '__main__' == __name__:
    unittest.main()



    
    
    
    
