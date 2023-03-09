import socket
import sys

class Connection:
    def socket_builder(self) -> socket:

        sock = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)

        server_address = '/tmp/tcp_socket_file'
        print("connecting to {}".format(server_address))

        try:
            sock.connect(server_address)
        except socket.error as err:
            print(err)
            sys.exit(1)
        return sock

class Sender:
    
    def send_file(self, sock: socket, file_path):

        try:
            message = b'a'
            sock.sendall(message)

            sock.settimeout(2)
            try:
                while True:
                    data = sock.recv(32)
                    if data:
                        print('Server response: ' + data.decode())
                    else:
                        break
            except(TimeoutError):
                print('Socket timeput, ending listening for server messages')
        
        finally:
            print('Closing socket')
            sock.close()
