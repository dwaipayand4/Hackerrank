# -*- coding: utf-8 -*-
"""Untitled9.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1OAogHWpoZ_dIFOe3gQrsdjX_H-zsvWIU
"""

class Solution:
    def findSecretWord(self, words: List[str], master: 'Master') -> None:
        for i in range(3000):
            c = 0
            for j in range(0, len(words)):
                if(j!=0):

                    wordCheck = words[j]
                    if (secretCandidate[0] == wordCheck[0]):
                        c=c+1
                    if (secretCandidate[1] == wordCheck[1]):
                        c=c+1
                    if (secretCandidate[2] == wordCheck[2]):
                        c=c+1
                    if (secretCandidate[3] == wordCheck[3]):
                        c=c+1
                    if (secretCandidate[4] == wordCheck[4]):
                        c=c+1
                    if (secretCandidate[5] == wordCheck[5]):
                        c=c+1

                    if(c == k):
                        k = master.guess(words[j])

                        if(k == 6):
                            print('You guessed the secret word correctly.')
                            return
                        elif(k == -1):
                            print('Either you took too many guesses, or you did not find the secret word.')
                            return
                        else:
                            secretCandidate = words[j]

                else:
                    k = master.guess(words[j])

                    if(k == 6):
                        print('You guessed the secret word correctly.')
                        return
                    elif(k == -1):
                        print('Either you took too many guesses, or you did not find the secret word.')
                        return
                    else:
                        secretCandidate = words[j]



        print('Either you took too many guesses, or you did not find the secret word.')