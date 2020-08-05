import os

from RequestProcessor import RequestProcessor

from CheckEnvs import check_env

from DataModels import Route
from DataModels import Stop

class TransportQuery:
    """
    This class is responsible for building queries against a transit system API.
    """
    def __init__(self):
        """
        When initializing it is expected that the ROUTE_REQUEST_URL
        and STOPS_REQUEST_URL environment variables are set.
        """

        # This class is resposible for final construction of payload
        # and sending it off to the API.
        self.request_processor = RequestProcessor()

        self.route_url = check_env('ROUTE_REQUEST_URL')
        self.stops_url = check_env('STOPS_REQUEST_URL')

    def generate_route_by_type_url(self, route_types):
        """
        Build second part of API plus querystring for
        filtering routes based on type.
        """
        return f"{self.route_url}?filter[type]={','.join(map(str, route_types))}"

    def get_routes_by_type(self, route_types):
        """
        We are going to let the MBTA handle the business logic of what 
        the rail types are, so we use their filter parameter.

        Build the API call to get the routes and return as Route objects.
        """

        # This runs the call to the API.
        route_results = self.request_processor.make_request(self.generate_route_by_type_url(route_types))

        # Pull the JSON results in Route objects.
        routes = [Route(route["id"],route["attributes"]["long_name"]) for route in route_results.json()["data"]]

        # Return list of Route objects.
        return routes
    
    def generate_stop_by_route_url(self, route):
        """
        Build second part of API plus querystring for
        getting stops by a single route.
        """
        return f"{self.stops_url}?fields[stop]=name&filter[route]={route.id}"

    def parse_stops(self, stops_json):
        """
        Take the JSON return from a call to the stops endpoint and
        convert to a list of Stop objects.
        """
        return [Stop(stop["id"],stop["attributes"]["name"]) for stop in stops_json]
            
    def get_stops_by_routes(self, routes):
        """
        Get all the stops serviced by our list of routes. Put them
        into a dictionary of dictionary[route] = [Stop, Stop, Stop...]
        """
        all_routes = {}

        for route in routes:
            # This isn't great to repeat this API call but I couldn't
            # see the Route ID in the results and we need it to make
            # the data object work.
            stops = self.request_processor.make_request(self.generate_stop_by_route_url(route)).json()["data"]

            # Parse the returns into a list of stops.
            all_routes[route] = self.parse_stops(stops)
            
        return all_routes
            
