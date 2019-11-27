import socket
import _thread
import select

__version__ = '0.1.0 Draft 1'
BUFFER_LEN = 8192
VERSION = 'Python Proxy/'+__version__
HTTP_VERSION = 'HTTP/1.1'


class ConnectionHandler:
    """ Docstring """

    def __init__(self, connection, timeout):
        self.client = connection
        self.timeout = timeout
        self.client_buffer = ''
        self.method, self.path, self.protocol = self.get_base_header()
        if self.method == 'CONNECT':
            self.method_connect()
        elif self.method in ('OPTIONS', 'GET', 'HEAD', 'POST', 'PUT', 'DELETE', 'TRACE'):
            self.method_others()
        self.client.close()
        self.target.close()

    def get_base_header(self):
        while 1:
            self.client_buffer += self.client.recv(BUFFER_LEN)
            end = self.client_buffer.find('\n')
            if end != -1:
                break
        print('{client_buffer'.format(client_buffer=self.client_buffer[:end]))
        data = (self.client_buffer[:end+1]).split()
        self.client_buffer = self.client_buffer[end+1:]
        return data

    def method_connect(self):
        self._connect_target(self.path)
        self.client.send("{http_version} 200 Connection established\nProxy-agent: {version}\n\n".format(
            http_version=HTTP_VERSION,
            version=VERSION
        ))
        self.client_buffer = ''
        self._read_write()

    def method_others(self):
        self.path = self.path[7:]
        i = self.path.find('/')
        host = self.path[:i]
        path = self.path[i:]
        self._connect_target(host)
        self.target.send("{method} {path} {protocol}\n{client_buffer}".format(
            method=self.method,
            path=path,
            protocol=self.protocol,
            client_buffer=self.client_buffer).encode("UTF-8")
                         )
        self.client_buffer = ''
        self._read_write()

    def _connect_target(self, host):
        i = host.find(':')
        if i!=-1:
            port = int(host[i+1:])
            host = host[:i]
        else:
            port = 80
        (soc_family, _, _, _, address) = socket.getaddrinfo(host, port)[0]
        self.target = socket.socket(soc_family)
        self.target.connect(address)

    def _read_write(self):
        time_out_max = self.timeout/3
        socs = [self.client, self.target]
        count = 0
        while 1:
            count += 1
            (receive, _, error) = select.select(socs, [], socs, 3)
            if error:
                break
            if receive:
                for in_ in receive:
                    data = in_.recv(BUFFER_LEN)
                    if in_ is self.client:
                        out = self.target
                    else:
                        out = self.client
                    if data:
                        out.send(data)
                        count = 0
            if count == time_out_max:
                break


def start_server(host='localhost', port=8080,
                 ipv6=False, timeout=60,
                 handler=ConnectionHandler):
    if ipv6:
        soc_type = socket.AF_INET6
    else:
        soc_type = socket.AF_INET
    soc = socket.socket(soc_type)
    soc.bind((host, port))
    print("Serving on {host}:{port}.".format(host=host, port=port))
    soc.listen(0)
    while 1:
        _thread.start_new_thread(handler, (soc.accept()[0], timeout))


if __name__ == '__main__':
    start_server()
