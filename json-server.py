import json

# This initial setup allows for requests to be sent

# Import HTTPServer class to access serve_forever method
from http.server import HTTPServer

# Inherit class from HTTPServer
from nss_handler import HandleRequests, status

# Import functions that will be upon request
from views import list_metals, retrieve_metal

# The database has been created, now we have to make the data accessible to the client.


class JSONServer(HandleRequests):
    def do_GET(self):
        response_body = ""
        url = self.parse_url(self.path)

        # Compare requested resource to database entries
        if url["requested_resource"] == "metals":
            if url["primary_key"] != 0:
                response_body = retrieve_metal(url["primary_key"])
                return self.response(response_body, status.HTTP_200_SUCCESS.value)
            response_body = list_metals()
            return self.response(response_body, status.HTTP_200_SUCCESS.value)
        if url["requested_resource"] == "styles":
            pass
        if url["requested_resource"] == "sizes":
            pass
        if url["requested_resource"] == "orders":
            pass


def main():
    host = ""
    port = 8000
    HTTPServer((host, port), JSONServer).serve_forever()


if __name__ == "__main__":
    main()
