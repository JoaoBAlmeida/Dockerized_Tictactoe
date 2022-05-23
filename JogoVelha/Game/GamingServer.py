from concurrent import futures

import logging
import os


import grpc
import redis
from GeneratedFiles import (Gaming_pb2,Gaming_pb2_grpc)

savedBoard = [
        ["-","-","-"],
        ["-","-","-"],
        ["-","-","-"],
    ]

#Connect to redis
r = redis.StrictRedis(host = 'redis', port = 6379, charset="utf-8", decode_responses=True)

def instantiateBoard():
    for i in range(3):
        for j in range(3):
            savedBoard[i][j] = "-"

def printBoard():
    
    print("=======Board Below======")
    for i in range(3):
        print("|".join(savedBoard[i]))
        if(i<2):
            print("------")

def CheckMove(movex, movey, piece):
    if savedBoard[movex][movey] == "-":
        savedBoard[movex][movey] = piece
        return True
    else:
        return False

def exportBoard():
    board = ""
    for i in savedBoard:
        for j in i:
            board += j
    return board

def checkWinner():
    #rows
    for i in range(3):
        if(savedBoard[i][0] != "-" and savedBoard[i][0] == savedBoard[i][1] and savedBoard[i][1] == savedBoard[i][2]):
            return True
    #col
    for i in range(3):
        if(savedBoard[0][i] != "-" and savedBoard[0][i] == savedBoard[1][i] and savedBoard[1][i] == savedBoard[2][i]):
            return True
    #primary diagonal
    if(savedBoard[0][0] != "-" and savedBoard[0][0] == savedBoard[1][1] and savedBoard[1][1] == savedBoard[2][2]):
        return True

    #secundary diagonal
    if(savedBoard[0][2] != "-" and savedBoard[0][2] == savedBoard[1][1] and savedBoard[1][1] == savedBoard[2][0]):
        return True

    for i in range(3):
        for j in range(3):
            if(savedBoard[i][j] == "-"):
                return False

def getServerPiece(piece):
    if(piece == 'x'):
        return 'o'
    else:
        return 'x'


#Class from .proto file
class Gaming(Gaming_pb2_grpc.GamingServicer):
    def SayWelcome(self, request, context):
        r.set('name', request.name)
        return Gaming_pb2.WelcomeReply(message='Welcome, player %s!' %r.get('name'))

    def setDraw(self, request, context):
        instantiateBoard()
        return Gaming_pb2.Board(pieces = "That's a Draw!")

    def makeMove(self, request, context):
        movex = request.boardXMove
        movey = request.boardYMove
        piece = request.piece
        if(not CheckMove(movex, movey, piece)):
            return Gaming_pb2.Board(pieces = "Move Error")
        if(checkWinner()):
            instantiateBoard()
            return Gaming_pb2.Board(pieces = "Winner")

        printBoard()
        #Server side gameset
        Server_piece = getServerPiece(piece)
        MoveError = False
        while(not MoveError):
            Server_movex = int(input("Choose Row: ")) - 1
            Server_movey = int(input("Choose Column: ")) - 1
            MoveError = CheckMove(Server_movex, Server_movey, Server_piece)

        if(checkWinner()):
            instantiateBoard()
            return Gaming_pb2.Board(pieces = "Loser")

        printBoard()
        return Gaming_pb2.Board(pieces = exportBoard())

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=3))
    Gaming_pb2_grpc.add_GamingServicer_to_server(Gaming(), server)
    server.add_insecure_port('[::]:80')
    server.start()
    print("Server Listening at port 80")
    server.wait_for_termination()

if __name__ == '__main__':
    logging.basicConfig()
    serve()