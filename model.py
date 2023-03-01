import pygame
import sys

class Model():
    maxScore = 0
    p1Score = 0
    p2Score = 0


    def __init__(self):
        self.maxScore = 5

    def addScorep1(self):
        self.p1Score += 1
        print("Player 1 Scores!")

    def addScorep2(self):
        self.p2Score += 1
        print("Player 2 Scores!")

    def detWinner(self):
        if(self.p1Score >= self.maxScore):
            print("Player 1 wins!")
            return True
        elif(self.p2Score >= self.maxScore):
            print("Player 2 wins!")
            return True
        return False


