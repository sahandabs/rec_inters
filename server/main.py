import server
from server import csHandler
from http.server import HTTPServer
# host and port for server(change if required)
host = "localhost"
port = 8080

if __name__ == '__main__':
    #create server with csHandler and provided port and host
    server = HTTPServer((host, port), csHandler)
    print('Starting server, use <Ctrl-C> to stop')
    # start server
    server.serve_forever()
