"""A web server capable of serving files from a given directory."""

import socket
import os.path
import sys

DOCUMENT_ROOT = '/tmp'
RESPONSE_TEMPLATE = """HTTP/1.1 200 OK
Content-Length: {}

{}"""

def main():
    """Main entry point for script."""
    listen_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    listen_socket.bind(('', int(sys.argv[1])))
    listen_socket.listen(1)

    while True:
        connection, address = listen_socket.accept()
        request = connection.recv(1024)
        start_line = request.split('\n')[0]
        method, uri, version = start_line.split()
        path = DOCUMENT_ROOT + uri
        if not os.path.exists(path):
            connection.sendall('HTTP/1.1 404 Not Found\n')
        else:
            with open(path) as file_handle:
                file_contents = file_handle.read()
                response = RESPONSE_TEMPLATE.format(
                    len(file_contents), file_contents)
                connection.sendall(response)
        connection.close()

if __name__ == '__main__':
    sys.exit(main())

