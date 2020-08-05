# broad-code-test

This is a python docker for running the Broad's MBTA code test.

# Requirements to run

You'll need docker and docker-compose installed to run this code.

You need to create a .env file in this directory with the following entries (Replace YOUR_API_KEY with a real API Key, one is required to run the code.)

```bash
BASE_REQUEST_URL=https://api-v3.mbta.com/
ROUTE_REQUEST_URL=routes
STOPS_REQUEST_URL=stops
API_KEY=YOUR_API_KEY
RAIL_STOP_1=Davis
RAIL_STOP_2=Kendall
```

# Building and running

I've supplied a docker-compose file so you should be able to run the following

```bash
docker-compose build mbta
docker-compose run mbta python main.py
```

# Question 3

I didn't get a chance to implement this but did think about it and supplied some pseudo code in main.py

```
QUESTION 1

Routes
Red Line
Mattapan Trolley
Orange Line
Green Line B
Green Line C
Green Line D
Green Line E
Blue Line


QUESTION 2

Most Stops
('Green Line B', 24)


Fewest Stops
('Mattapan Trolley', 8)


Connecting Stops


Stop : Park Street
----
Red Line
Green Line B
Green Line C
Green Line D
Green Line E


Stop : Downtown Crossing
----
Red Line
Orange Line


Stop : Ashmont
----
Red Line
Mattapan Trolley


Stop : State
----
Orange Line
Blue Line


Stop : Haymarket
----
Orange Line
Green Line C
Green Line E


Stop : North Station
----
Orange Line
Green Line C
Green Line E


Stop : Saint Paul Street
----
Green Line B
Green Line C


Stop : Kenmore
----
Green Line B
Green Line C
Green Line D


Stop : Hynes Convention Center
----
Green Line B
Green Line C
Green Line D


Stop : Copley
----
Green Line B
Green Line C
Green Line D
Green Line E


Stop : Arlington
----
Green Line B
Green Line C
Green Line D
Green Line E


Stop : Boylston
----
Green Line B
Green Line C
Green Line D
Green Line E


Stop : Government Center
----
Green Line C
Green Line D
Green Line E
Blue Line
```