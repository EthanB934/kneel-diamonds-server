# enum statuses with prebuilt values
from enum import Enum

# Prebuilt url handler functions

from urllib.parse import urlparse, parse_qs

# Root class to enable HTTP communication with server
from http.server import BaseHTTPRequestHandler


# Response codes to notify the client of the request status
class status(Enum):
    HTTP_200_SUCCESS = 200
    HTTP_201_SUCCESS_CREATED = 201
    HTTP_204_SUCCESS_NO_RESPONSE_BODY = 204
    HTTP_400_CLIENT_ERROR_BAD_REQUEST_DATA = 400
    HTTP_404_CLIENT_ERROR_RESOURCE_NOT_FOUND = 404
    HTTP_500_SERVER_ERROR = 500


class HandleRequests(BaseHTTPRequestHandler):
    def response(self, body, code):
        self.set_response_code(code)
        self.wfile.write(body.encode())

    """Receives request. Destructures request into resource"""

    def parse_url(self, path):
        """Parses client request into manageable, readable pieces

        Args:
            path (string): a string representing a client's request that will be broken down
            to isolate the requested resource and any accompanying parameters in that request.
        """
        parsed_url = urlparse(path)
        path_params = parsed_url.path.split("/")
        resource = path_params[1]

        # The request has been broken down into smaller piece. Create a new collection with the
        # relevant pieces

        url_dictionary = {
            "requested_resource": resource,
            "query_parameters": {},
            "primary_key": 0,
        }

        # Query parameters may not always be used, but can be. In the case that they
        # are, we not update the dictionary key, query_parameters to reflect them.

        query = parse_qs(parsed_url.query)

        # Updating the dictionary with the return of parse_qs

        url_dictionary["query_parameters"] = query
        if "primary_key" in query:
            query_list = query["primary_key"]
            url_dictionary["primary_key"] = int(query_list[0])

        return url_dictionary

    def set_response_code(self, status):
        self.send_response(status)
        self.send_header("Content-type", "application/json")
        self.send_header("Access-Control-Allow-Origin", "*")
        self.end_headers()
