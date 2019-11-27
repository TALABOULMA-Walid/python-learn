"""A web server capable of serving files from a given directory."""

import logging
import os.path
import socket
import sys

RESPONSE_TEMPLATE = """HTTP/1.1 200 OK
{headers}

{content}"""

LOGGER = logging.getLogger(__name__)

HTML_CONTENT_TYPES = ('text/html')
JSON_CONTENT_TYPES = ('application/json')

def parse_headers(request):
    """Return a dictionary in the form Header => Value for all headers in
    *request*."""
    headers = {}
    request = request.decode("utf-8")
    for line in request.split('\n')[1:]:
        # blank line separates headers from content
        if line == '\r':
            break
        header_line = line.partition(':')
        headers[header_line[0].lower()] = header_line[2].strip()
    return headers

def is_content_type_negotiable(accepts, extension):
    """Return the content-type we must reply with or None if no acceptable
    content-type can be chosen."""

    # For now, just check if the extensions is included somewhere in the Accepts
    # header, or that Accepts is "*/*"
    return extension in accepts or accepts == '*/*'

def response_with_cookies(content):
    return RESPONSE_TEMPLATE.format(headers='Set-Cookie: HasVisited = 1;',
            content=content)

def main():
    """Main entry point for script."""
    listen_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    listen_socket.bind(('', int(sys.argv[1])))
    listen_socket.listen(1)
    document_root = sys.argv[2]

    while True:
        connection, address = listen_socket.accept()
        request = connection.recv(1024)
        headers = parse_headers(request)
        cookies = None
        if 'cookie' in headers:
            cookies = {e.split('=')[0]: e.split('=')[1] for e in headers['cookie'].split(';')}
        try:
             if 'HasVisited' in cookies:
                print ('User has already visited!')
        except:
             print("Cookie None")
        request = request.decode("utf-8")
        start_line = request.split('\n')[0]
        print(start_line)
        method, uri, version = start_line.split()
        print(method, uri, version)
        path = document_root + uri[1:]
        extension = os.path.splitext(path)[1][1:]
        if 'accept' not in headers or not is_content_type_negotiable(
                headers['accept'], extension):
            connection.sendall(b'HTTP/1.1 406 Not Acceptable\n')
        elif not os.path.exists(path):
            print(path)
            connection.sendall(b'HTTP/1.1 404 Not Found\n')
        else:
            with open(path) as file_handle:
                print(path)
                file_contents = file_handle.read()                
                connection.sendall(response_with_cookies(file_contents).encode("utf-8")) 
        connection.close()

if __name__ == '__main__':
    sys.exit(main())
