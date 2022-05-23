# Dockerized_Tictactoe
Dockerized game made for Sistemas Distribuidos class
GRPC Tools were used for server & client connection
REDIS was implemented to see an alternate way to store variables
DOCKER brought it all under containers

#Using the system (for windows)
After cloning, open the console at the Dockerfile and docker-compose.yml folder, and run the following command
  1. docker-compose build
After it's done, in the same terminal, run the following command to have the redis service up:
  2. docker-compose run --name redis --service-ports redis
And to initialize the server, in another terminal:
  3. docker-compose run --name game-server --service-ports server
Now, to play, in another terminal move to "Game" folder and run:
  4. python GamingClient.py
