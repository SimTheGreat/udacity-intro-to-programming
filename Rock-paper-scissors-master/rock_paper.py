#!/usr/bin/env python3
"""This program plays a game of Rock, Paper, Scissors between two Players,
and reports both Player's scores each round."""
moves = ['rock', 'paper', 'scissors']
"""The Player class is the parent class for all of the Players
in this game"""


class Player:
    def init(self):
        # score = 0;
        self.mymove = ""
        self.theirmove = ""

    def move(self):
        return 'rock'

    def learn(self, my_move, their_move):
        self.mymove = my_move
        self.theirmove = their_move


class randomplayer(Player):
    def move(self):
        return random.choice(moves)


class humanplayer(Player):
    def move(self):
        while True:
            move = input("What's your move? ")
            move = move.lower()
            if move in moves:
                return move
            else:
                print("Error - wrong input!")


class reflectplayer(Player):
    def __init__(self):
        self.counter = 0

    def move(self):
        if self.counter < 1:
            self.counter += 1
            return random.choice(moves)
        return self.theirmove


class cycleplayer(Player):
    pass


def beats(one, two):
    return ((one == 'rock' and two == 'scissors') or
            (one == 'scissors' and two == 'paper') or
            (one == 'paper' and two == 'rock'))


class Game:
    score1 = 0
    score2 = 0

    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def play_round(self):
        move1 = self.p1.move()
        move2 = self.p2.move()
        print(f"Player 1: {move1}\nPC 2: {move2}")
        if move1 == move2:
            print(f"Tie,{self.score1}:{self.score2}")
        elif beats(move1, move2) is True:
            self.score1 += 1
            print(f"Win,{self.score1}:{self.score2}")
        else:
            self.score2 += 1
            print(f"Lost,{self.score1}:{self.score2}")
        self.p1.learn(move1, move2)
        self.p2.learn(move2, move1)

    def play_game(self):
        print("Game start!")
        for round in range(3):
            print(f"\n\nRound {round +1}:")
            self.play_round()
        if self.score1 > self.score2:
            print("YOU WON!")
        elif self.score1 == self.score2:
            print("THAT'S A DRAW.")
        else:
            print("YOU LOST!")
        print("Game over!")


if __name__ == '__main__':

    import random
    game = Game(humanplayer(), reflectplayer())
    game.play_game()
