from db import dbConnector
from bfs import breadth_first_search, get_routes



if __name__ == "__main__":
    with dbConnector() as connector:
        routes = get_routes(2236172, 58021, connector)
        for route in routes:
            print(route)



