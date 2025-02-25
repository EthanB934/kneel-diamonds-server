# Prebuilt url handler functions

from urllib.parse import urlparse, parse_qs

# Root class to enable HTTP communication with server
from http.server import BaseHTTPRequestHandler


class HandleRequests(BaseHTTPRequestHandler):
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
            url_dictionary["primary_key"] = query["primary_key"]

        return url_dictionary
