from http.server import HTTPServer
from server import RequestHandler


def main():
    PORT = 8090
    server_address = ("0.0.0.0", PORT)
    server = HTTPServer(server_address, RequestHandler)
    server.serve_forever()


if __name__ == "__main__":
    main()
