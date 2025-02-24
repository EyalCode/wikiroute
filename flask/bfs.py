from db import dbConnector
from collections import deque


MAX_DEPTH = 6


def get_routes(src, target, connector):
    src_id = connector.get_id_from_title(src)
    target_id = connector.get_id_from_title(target)
    routes = breadth_first_search(src_id, target_id, connector)
    
    # Routes to actual names
    for route in routes:
        for title in route:
            title = connector.get_title_from_id(title)

    return routes


def breadth_first_search(src, target, connector):
    """Returns a list of pages of the first Route to be found, with . 

    Args:
        src: The page to find links from.

    Returns:
        List of links.

    """

    depth = 0

    src = int(src)
    target = int(target)

    forward_queue = deque()
    forward_queue.append(src)
    backward_queue = deque()
    backward_queue.append(target)

    forward_visited = {src}
    backward_visited = {target}

    current_depth_visited = set()
    print(forward_visited)

    forward_depth_indicator = src
    backward_depth_indicator = target
    tmp_indicator_holder = src

    forward_routes = {

    }

    backward_routes = {

    }

    connections = set()
    route_found = False
    forward = True

    while forward_queue and backward_queue and depth < MAX_DEPTH:
        if forward:
            current = forward_queue.popleft() 
            
            ## Add all new articles to queue
            for article in connector.get_links_from(current):
                tmp_indicator_holder = article
                if article in forward_visited:
                    continue
                if article in backward_visited or route_found: # Route Found!
                    if article in backward_visited:
                        connections.add(article)
                    route_found = True
                if article in forward_routes:
                    forward_routes[article].add(current)
                else:
                    forward_routes[article] = {current}

                if article not in current_depth_visited:
                    forward_queue.append(article)
                    current_depth_visited.add(article)
                
            if current == forward_depth_indicator:
                if route_found:
                    break
                depth += 1
                forward_depth_indicator = tmp_indicator_holder
                forward_visited.update(current_depth_visited)
                current_depth_visited.clear()
                forward = False
        else:
            current = backward_queue.popleft() 
            
            ## Add all new articles to queue
            for article in connector.get_links_to(current):
                tmp_indicator_holder = article
                if article in backward_visited:
                    continue
                if article in forward_visited or route_found: # Route Found!
                    if article in forward_visited:
                        connections.add(article)
                    route_found = True
                if article in backward_routes:
                    backward_routes[article].add(current)
                else:
                    backward_routes[article] = {current}

                if article not in current_depth_visited:
                    backward_queue.append(article)
                    current_depth_visited.add(article)
                
            if current == backward_depth_indicator:
                if route_found:
                    break
                depth += 1
                backward_depth_indicator = tmp_indicator_holder
                backward_visited.update(current_depth_visited)
                current_depth_visited.clear()
                forward = True



    return retrieve_routes(forward_routes, backward_routes, connections, src, target)




def retrieve_routes(forward_routes, backward_routes, connections, src, target):
    routes = []
    for vertex in connections:
        backward = retrieve_backwards(forward_routes, vertex, src)
        forward = retrieve_forward(backward_routes, vertex, target)
        routes_to_add = [ backward_route[:-1] + forward_route for backward_route in backward for forward_route in forward ]
        routes += routes_to_add

    return routes


def retrieve_backwards(backward_routes, current, target):
    routes = []
    if current == target:
        return [[current]]
    
    for vertex in backward_routes[current]:
        for route in retrieve_backwards(backward_routes, vertex, target):
            routes.append(route + [current])
    
    return routes


def retrieve_forward(forward_routes, current, target):
    routes = []
    if current == target:
        return [[current]]
    
    for vertex in forward_routes[current]:
        for route in retrieve_backwards(forward_routes, vertex, target):
            routes.append([current] + route)
    
    return routes


