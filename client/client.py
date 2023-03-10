import socket
import sys
from connector import Connection, Sender
from file_creator import FileCreator

def main():
    sock = Connection.socket_builder()
     
    # file = FileCreator.create_json()
    file = "./json/request.json"
    Sender.send_file(sock, file)

if __name__ == '__main__':
    main()
