class Graph:
    def __init__(self, edges):
        self.edges = edges
        self.graph_dict = {}
        
        for start, end in self.edges:
            if start in self.graph_dict:
                self.graph_dict[start].append(end)
            else:
                self.graph_dict[start] = [end]
                
        print("Graph dict: ", self.graph_dict)
        
    def get_paths(self, start, end, path = []):
        path = path + [start]
        
        if start == end:
            return [path]
        
        if start not in self.graph_dict:
            return []
        
        paths = []
        for node in self.graph_dict[start]:
            if node not in path:
                new_paths = self.get_paths(node, end, path)
                for p in new_paths:
                    paths.append(p)
            
        return paths
          
          
    def get_shortest_path(self, start, end, path=[]):
        path = path + [start]
        if start==end:
            return path
        
        if start not in self.graph_dict:
            return None  
        
        shortest_path = None
        for node in self.graph_dict[start]:
            if node not in path:
                sp = self.get_shortest_path(node, end, path)
                if sp:
                    if shortest_path is None or len(sp)<len(shortest_path):
                        shortest_path = sp
            
        return shortest_path
            
            

if __name__ == "__main__":
    routes = [
        ("Mumbai", "Paris"),
        ("Mumbai", "Dubai"),
        ("Paris", "Dubai"),
        ("Paris", "New York"),
        ("Dubai", "New York"),
        ("New York", "Toronto")
    ]
    
    route_graph = Graph(routes)
    d = {
        "Mumbai": ["Paris", "Dubai"],
        "Paris": ["Dubai", "New York"]
    }
    
    start = "Mumbai"
    start2 = "Toronto"
    start3 = "Mumbai"
    end = "Mumbai"
    end2 = "Mumbai"
    end3 = "New York"
    
    
    # print(f"Paths between {start} and {end} : ", route_graph.get_paths(start, end))
    # print(f"Paths between {start2} and {end2} : ", route_graph.get_paths(start2, end2))
    # print(f"Paths between {start3} and {end3} : ", route_graph.get_paths(start3, end3))
    
    s1 = "Toronto"
    s2 = "New York"
    s3 = "Mumbai"
    s4 = "Paris"
    e1 = "New York"
    e2 = "New York"
    e3 = "Toronto"
    
    
    print(f"Shortest Paths between {s1} and {e1} : ", route_graph.get_shortest_path(s1, e1))
    print(f"Shortest Paths between {s2} and {e2} : ", route_graph.get_shortest_path(s2, e2))
    print(f"Shortest Paths between {s3} and {e2} : ", route_graph.get_shortest_path(s3, e2))
    print(f"Shortest Paths between {s4} and {e3} : ", route_graph.get_shortest_path(s4, e3))
    

    