from collections import deque


MAX_DEPTH = 6

def breadth_first_search(src, target):
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
            for article in get_links_from(current):
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
            for article in get_links_to(current):
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



    return routes



def find_all_routes_to(depth, visited_vertices_by_depth, routes):
    new_routes = set()
    for current_route in routes:
        for vertex in visited_vertices_by_depth[depth-1]:
            if vertex in get_links_to(current_route[0]):
                new_routes.add((vertex,) + current_route)

    if depth <= 1:
        return new_routes
    return find_all_routes_to(depth-1, visited_vertices_by_depth, new_routes)



def find_all_routes_from(depth, visited_vertices_by_depth, routes):
    
    new_routes = set()

    for current_route in routes:
        for vertex in visited_vertices_by_depth[depth-1]:
            if vertex in get_links_from(current_route[-1]):
                new_routes.add(current_route + (vertex,))

    if depth <= 1:
        return new_routes
    return find_all_routes_from(depth-1, visited_vertices_by_depth, new_routes)



def connect_from_and_to_routes(to_routes, from_routes):
    routes = set()
    for to_route in to_routes:
        for from_route in from_routes:
            routes.add(to_route + from_route[1:])

    return routes

def find_routes(forward_depth, backward_depth, forward_visited_vertices, backward_visited_vertices, current):
    if backward_depth == 0:
        return {(*forward_visited_vertices[0], current)}
    routes_to = find_all_routes_to(forward_depth, forward_visited_vertices, {(current,)})
    routes_from = find_all_routes_from(backward_depth, backward_visited_vertices, {(current,)})
    return connect_from_and_to_routes(routes_to, routes_from)


def retrieve_routes(forward_routes, backward_routes, connectors, src, target):
    routes = set()
    for vertex in connectors:
        current = vertex
        while current != target ### TODODODODO

def get_links_from(vertex_id):
    # TODO

def get_links_to(vertex_id):
    # TODO

