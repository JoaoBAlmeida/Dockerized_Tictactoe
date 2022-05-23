FROM python:latest

WORKDIR /av02
ADD . /av02

RUN pip install --upgrade pip
RUN pip install grpcio
RUN pip install grpcio-tools
RUN pip install redis

ENTRYPOINT [ "python", "Game/GamingServer.py" ]