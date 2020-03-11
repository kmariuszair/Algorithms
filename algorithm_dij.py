"""
Implements Dijkstra algorith of finding the shortest way between two graph vertices
"""

from typing import Dict, List, Tuple

vertex_t = int
cost_table_t = List[Tuple[int,float]]

def Dijkstra(adjacency_list: Dict[vertex_t, cost_table_t], begin_vertex: vertex_t, end_vertex: vertex_t) -> List[Tuple[vertex_t,vertex_t]]:
    # dictionary, that represents algorithm talbe
    # the keys are vertices (mean vertices, that there was no shortest path found)
    # the values are tuples of [0]-last vertex, that the shortest path from begin to the vertex go through, [1]-cost of that path
    path_table = { i+1:(0,float('inf')) for i in range(len(adjacency_list) )}
    path_table[begin_vertex] = (0,float('nan'))

    # store here vertices, that make the shortest path, elements added in separete loop
    shortest_path = list()

    # store here in values the previos vertex in shortest path between begin and vertex in key
    previos_vertices_table = {begin_vertex: 0}

    # strore here vertices, that are already checked
    checked_vertices = list()

    # cost to get from begin vertex to vertex from key
    vertex_cost = {begin_vertex: 0}

    # begin algorith with begin_vertex
    vertex_to_check = begin_vertex

    # we want to make sure, that we know the shortest way to end_vertex
    while(end_vertex != vertex_to_check):

        # add current checked vertex to shorte
        # actualize path_table
        for neighboor_vertex, cost in adjacency_list[vertex_to_check]: 
            # if the cost in path table is higher than in adjacency list of vertex, that is being checked
            if path_table[neighboor_vertex][1] > cost + vertex_cost[vertex_to_check]:
                # mark the shortest path between vertex_to_check and neighboor_vertex
                path_table[neighboor_vertex] = (vertex_to_check, cost + vertex_cost[vertex_to_check])
        
        # check most optimal vertex
        min_cost = float('inf')
        for neighboor_vertex, (_, cost) in path_table.items():
            if cost < min_cost:
                min_cost   = cost
                min_vertex = neighboor_vertex 

        checked_vertices.append(vertex_to_check)

        # store here the vertex, that the shortest path to begin was found
        previos_vertices_table[min_vertex] = path_table[min_vertex][0]
        vertex_cost[min_vertex] = path_table[min_vertex][1]
        path_table[min_vertex] = (previos_vertices_table[min_vertex], float('nan'))

        vertex_to_check = min_vertex

    # construct shortest path from end_vertex to begin_vertex
    shortest_path.insert(0,end_vertex)
    last =  previos_vertices_table[end_vertex]
    while(begin_vertex not in shortest_path):
        shortest_path.insert(0,last)
        last = previos_vertices_table[last]

    return shortest_path