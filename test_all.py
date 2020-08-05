import pytest

from CheckEnvs import check_env
from CheckEnvs import MissingEnvVar

from TransportQuery import TransportQuery

from DataModels import Route
from DataModels import Stop

from main import find_most_stops
from main import find_min_stops
from main import find_stop_intersection

# Speaking of environment variables, my tests don't specify defaults. 
# I think best practice would be mocking those.

class TestCheckEnvs:
    """
    Test the Check Envs functionality
    """
    def test_check_env(self):
        # Do we return a value when present?
        assert check_env('BASE_REQUEST_URL') is not None
        
        # Do we raise an error when not present?
        with pytest.raises(MissingEnvVar):
            check_env('FOO') is not None

class TestTransportQuery:
    def test_get_routes_by_type(self):
        new_transport_query = TransportQuery()
        # Does the function to generate a query return the right string?
        assert new_transport_query.generate_route_by_type_url([0,1]) == "routes?filter[type]=0,1"

        routes = new_transport_query.get_routes_by_type([0,1])
        # Does the function that queries the routes return the right results? This requires API access!
        assert [str(route) for route in routes] == ['Red Line', 'Mattapan Trolley', 'Orange Line', 'Green Line B', 'Green Line C', 'Green Line D', 'Green Line E', 'Blue Line']
    
    def test_generate_stop_by_routes(self):
        route = Route("Red", "Red Line")

        new_transport_query = TransportQuery()
        # Does the function to generate a query return the right string?
        assert new_transport_query.generate_stop_by_route_url(route) == "stops?fields[stop]=name&filter[route]=Red"

        stops = new_transport_query.get_stops_by_routes([route])
        # Does the query to get stops return the right count as a proxy for working function?
        assert len(stops["Red"]) == 22

class TestMain:

    route_stops = {Route("Red", "Red Line"): [Stop("1", "stop1"), Stop("2", "stop2"), Stop("3", "stop3")],
                        Route("Blue", "Blue Line"): [Stop("2", "stop2"), Stop("4", "stop4")],
                        Route("Green", "Green Line"): [Stop("5", "stop5")]}

    def test_max_stops(self):
        # Do we find the correct max stops route?
        assert find_most_stops(self.route_stops) == ("Red Line", 3)

    def test_min_stops(self):
        # Do we find the correct min stops route?
        assert find_min_stops(self.route_stops) == ("Green Line", 1)
    
    def test_find_stop_intersection(self):
        # Do we find the intersections?
        intersections = find_stop_intersection(self.route_stops)
        assert intersections[0][0] == "stop2"
        assert intersections[0][1][0].id == "Red"
        assert intersections[0][1][1].id == "Blue"