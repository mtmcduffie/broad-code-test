import math
import collections

from TransportQuery import TransportQuery

# These three functions take a dictionary of dictionary[route] = [Stop, Stop, Stop...]
# and calculate the most and least stops as well as intersection of routes.
def find_most_stops(route_stops):

    max_length = 0
    max_route = None

    for route in route_stops:
        if len(route_stops[route]) > max_length:
            max_route = route
            max_length = len(route_stops[route])

    return max_route.long_name, max_length

def find_min_stops(route_stops):

    min_length = math.inf
    min_route = None

    for route in route_stops:
        if len(route_stops[route]) < min_length:
            min_route = route
            min_length = len(route_stops[route])

    return min_route.long_name, min_length

def find_stop_intersection(route_stops):
    
    stop_overlap_checks = collections.defaultdict(list)

    for route in route_stops:
        for stop in route_stops[route]:
            stop_overlap_checks[stop.name].append(route)
    
    return [(stop_overlap_check, stop_overlap_checks[stop_overlap_check]) for stop_overlap_check in stop_overlap_checks if len(stop_overlap_checks[stop_overlap_check]) > 1]

new_transport_query = TransportQuery()

# Question 1
print("QUESTION 1")
print("\nRoutes")
routes = new_transport_query.get_routes_by_type([0,1])
for route in routes:
    print(route.long_name)
print("\n")

# Question 2
print("QUESTION 2\n")
route_stops = new_transport_query.get_stops_by_routes(routes)

print("Most Stops")
print(find_most_stops(route_stops))
print("\n")

print("Fewest Stops")
print(find_min_stops(route_stops))
print("\n")

print("Connecting Stops")
print("\n")
intersections = find_stop_intersection(route_stops)
for intersection in intersections:
    print(f"Stop : {intersection[0]}")
    print("----")
    for route in intersection[1]:
        print(route.long_name)
    print("\n")
print("\n")

# Question 3

# Take first stop and find all routes that service it.
# Take second stop and find all routes that service it.
# Are any the same? If so, just take that one.

# Now we need we need to jump from one line to another to reach our destination.

# A) Grab the first/next route that services the first stop.
# Find a transfer station for that route
# B) Take the first/next route at the transfer station and find all stops
# Is our second stop there?
# If yes, we know the jump we had to take to get there.
# If no, Repeat the above from B.
# Still nothing? Repeat the above from A.

# At some point you have to handle if you have to make more than one jump.
