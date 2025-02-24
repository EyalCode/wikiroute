from db import dbConnector
from bfs import breadth_first_search



if __name__ == "__main__":
    with dbConnector() as connector:
        routes = breadth_first_search(2236172, 58021, connector)
        for route in routes:
            print(route)



