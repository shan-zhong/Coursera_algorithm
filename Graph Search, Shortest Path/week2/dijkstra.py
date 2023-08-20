from ast import literal_eval

class Dijkstra():
    def __init__(self, input_file):
        self.graph = {}
        with open(input_file) as file:
            for line in file:
                line_content = line.split()
                self.graph[int(line_content[0])] = [eval(edge) for edge in line_content[1:]]
        self._source_vertex = next(iter(self.graph.keys()))

    def compute_shortest_paths(self, source=None):
        if source is None:
            source = self._source_vertex
        shortest_paths = {}
        visited = set()
        for vertex in self.graph.keys():
            shortest_paths[vertex] = [9999999999, []]
        shortest_paths[source] = [0, []]
        visited.add(source)
        while set(self.graph.keys() - visited):
            source, min_edge = -1, []
            for vertex in visited:
                for edge in self.graph[vertex]:
                    if edge[0] in visited:
                        continue
                    if not min_edge or shortest_paths[vertex][0]+edge[1] < min_edge[1]:
                        min_edge = [edge[0], shortest_paths[vertex][0] + edge[1]]
                        source = vertex
            shortest_paths[min_edge[0]] = (min_edge[1], shortest_paths[source][1] + [min_edge[0]])
            visited.add(min_edge[0])
        return shortest_paths
    
if __name__ == '__main__':
    path_finder = Dijkstra('assignment2.txt')
    paths = path_finder.compute_shortest_paths()
    actual = {vertex: distance[0] for (vertex, distance) in paths.items()}
    print(f"{actual[7]},{actual[37]},{actual[59]},{actual[82]},{actual[99]},{actual[115]},{actual[133]},{actual[165]},{actual[189]},{actual[197]}")
 
'''Output 2599
2610
2947
2052
2367
2399
2029
2442
2505
3068
'''