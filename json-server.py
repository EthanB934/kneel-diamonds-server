import json

# This initial setup allows for requests to be sent

# Import HTTPServer class to access serve_forever method
from http.server import HTTPServer

# Inherit class from HTTPServer
from nss_handler import HandleRequests, status

# Import functions that will be upon request
from views import list_metals, retrieve_metal, update_metal, create_metal, delete_metal
from views import list_styles, retrieve_style, update_style, create_style, delete_style
from views import list_sizes, retrieve_size, update_size, create_size, delete_size
from views import list_orders, retrieve_order, update_order, create_order, delete_order

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
            if url["primary_key"] != 0:
                response_body = retrieve_style(url["primary_key"])
                return self.response(response_body, status.HTTP_200_SUCCESS.value)
            response_body = list_styles()
            return self.response(response_body, status.HTTP_200_SUCCESS.value)
        if url["requested_resource"] == "sizes":
            if url["primary_key"] != 0:
                response_body = retrieve_size(url["primary_key"])
                return self.response(response_body, status.HTTP_200_SUCCESS.value)
            response_body = list_sizes()
            return self.response(response_body, status.HTTP_200_SUCCESS.value)
        if url["requested_resource"] == "orders":
            if url["primary_key"] != 0:
                response_body = retrieve_order(url["primary_key"])
                return self.response(response_body, status.HTTP_200_SUCCESS.value)
            response_body = list_orders()
            return self.response(response_body, status.HTTP_200_SUCCESS.value)

    def do_PUT(self):
        # Request to update data in SQL

        # Initialize Return String
        response_body = ""
        url = self.parse_url(self.path)

        # Capture Request Body, needed values to process update
        # Finds length of request body
        content_len = int(self.headers.get("content-length", 0))
        # Reads request body as far as the length was previously calculated
        request_body = self.rfile.read(content_len)
        # Converts to JSON string
        request_body = json.loads(request_body)

        if url["requested_resource"] == "metals":
            # Requires primary key.
            if url["primary_key"] != 0:
                updated_metal = update_metal(url["primary_key"], request_body)
                # Was the update successful?
                if updated_metal:
                    return self.response("", status.HTTP_200_SUCCESS.value)
        if url["requested_resource"] == "styles":
            if url["primary_key"] != 0:
                updated_style = update_style(url["primary_key"], request_body)
                # Was the update successful?
                if updated_style:
                    return self.response("", status.HTTP_200_SUCCESS.value)
        if url["requested_resource"] == "sizes":
            if url["primary_key"] != 0:
                updated_size = update_size(url["primary_key"], request_body)
                # Was the update successful?
                if updated_size:
                    return self.response("", status.HTTP_200_SUCCESS.value)
        if url["requested_resource"] == "orders":
            if url["primary_key"] != 0:
                updated_order = update_order(url["primary_key"], request_body)
                # Was the update successful?
                if updated_order:
                    return self.response("", status.HTTP_200_SUCCESS.value)

    def do_POST(self):
        response_body = ""
        url = self.parse_url(self.path)

        # Creates a new resource in database
        # Request body is required

        content_len = int(self.headers.get("content-length", 0))
        request_body = self.rfile.read(content_len)
        request_body = json.loads(request_body)

        if url["requested_resource"] == "metals":
            create_metal(request_body)
            return self.response("", status.HTTP_201_SUCCESS_CREATED.value)
        if url["requested_resource"] == "styles":
            create_style(request_body)
            return self.response("", status.HTTP_201_SUCCESS_CREATED.value)
        if url["requested_resource"] == "sizes":
            create_size(request_body)
            return self.response("", status.HTTP_201_SUCCESS_CREATED.value)
        if url["requested_resource"] == "orders":
            create_order(request_body)
            return self.response("", status.HTTP_201_SUCCESS_CREATED.value)

    def do_DELETE(self):
        response_body = ""
        url = self.parse_url(self.path)

        if url["requested_resource"] == "metals":
            if url["primary_key"] != 0:
                successfully_deleted = delete_metal(url["primary_key"])
                if successfully_deleted:
                    return self.response("", status.HTTP_200_SUCCESS.value)
        if url["requested_resource"] == "styles":
            if url["primary_key"] != 0:
                successfully_deleted = delete_style(url["primary_key"])
                if successfully_deleted:
                    return self.response("", status.HTTP_200_SUCCESS.value)
        if url["requested_resource"] == "sizes":
            if url["primary_key"] != 0:
                successfully_deleted = delete_size(url["primary_key"])
                if successfully_deleted:
                    return self.response("", status.HTTP_200_SUCCESS.value)
        if url["requested_resource"] == "orders":
            if url["primary_key"] != 0:
                successfully_deleted = delete_order(url["primary_key"])
                if successfully_deleted:
                    return self.response("", status.HTTP_200_SUCCESS.value)


def main():
    host = ""
    port = 8000
    HTTPServer((host, port), JSONServer).serve_forever()


if __name__ == "__main__":
    main()
