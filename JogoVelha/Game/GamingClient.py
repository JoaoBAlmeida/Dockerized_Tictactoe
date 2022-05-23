from __future__ import print_function

import logging

import grpc
from GeneratedFiles import (Gaming_pb2,Gaming_pb2_grpc)

def printBoard(Board):
    print(Board.pieces[0] + "|" + Board.pieces[1] + "|" + Board.pieces[2])
    print("------")
    print(Board.pieces[3] + "|" + Board.pieces[4] + "|" + Board.pieces[5])
    print("------")
    print(Board.pieces[6] + "|" + Board.pieces[7] + "|" + Board.pieces[8])

def run():
    with grpc.insecure_channel('localhost:80') as channel:
        stub = Gaming_pb2_grpc.GamingStub(channel)
        name = input("Enter your name: ")
        response = stub.SayWelcome(Gaming_pb2.UserRegistry(name = name))
        print(response.message)
        typo = "-"
        while(True):
            if(typo == "x" or typo == "o"):
                break
            typo = input("What's your piece, x or o: ")

        #Variable to keep server running
        keepGoing = True
        turn = 1
        
        #Gaming loop
        while(keepGoing):
            
            if turn >= 5:
                response = stub.setDraw(Gaming_pb2.Board(pieces = "Draw"))
                print(response.pieces)
                break

            movex = int(input("Choose Row: ")) - 1
            movey = int(input("Choose Column: ")) - 1

            response = stub.makeMove(Gaming_pb2.UserRegistry(name = name, 
            boardXMove = movex, 
            boardYMove = movey, 
            piece = typo))

            if(response.pieces == "Move Error"):
                print("Movement not allowed")
                continue
            elif(response.pieces == "Winner"):
                print("Congrats on winning")
                keepGoing = False
            elif(response.pieces == "Loser"):
                print("Sorry, you lost")
                keepGoing = False
            else:
                printBoard(response)
                turn += 1
            

if __name__ == '__main__':
    print("===== Client Started =======")
    logging.basicConfig()
    run()