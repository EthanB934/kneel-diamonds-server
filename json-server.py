import json

# This initial setup allows for requests to be sent

# Import HTTPServer class to access serve_forever method
from http.server import HTTPServer

# Inherit class from HTTPServer
from nss_handler import HandleRequests

# The database has been created, now we have to make the data accessible to the client.


class JSONServer(HandleRequests):
    def do_GET(self):
        response_body = ""
        url = self.parse_url(self.path)
        return url


def main():
    host = ""
    port = 8000
    HTTPServer((host, port), JSONServer).serve_forever()


if __name__ == "__main__":
    main()
