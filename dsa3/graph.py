#=========================GRAPH IMPLEMENTATION FROM SCRATCH========================

# class Graph:
#     def __init__(self):
#         self.graph={}

    
#     def add_node(self,node):
#         if node in self.graph:       #in keys, duplicate keys are not accepted
#             print("this key i already present in graph")
#         else:
#             self.graph[node]=[]          ##no edges are created, only added a node. self.graph[node] here self.graph is dict and node is the key . [] is the value. currently no edges are there and also no adjascent node are create for the new node

    
#     def add_edges(self,n1,n2):           #undirectional unweighted graph
#         if n1 not in self.graph:
#             print(n1," is not present in graph")
#         elif n2 not in self.graph:
#             print(n2," is not present in graph")
#         else:
#             self.graph[n1].append(n2)
#             self.graph[n2].append(n1)


#     def delete_node_undirect(self,n1):           #undirection unweighted
#         if n1 not in self.graph:
#             print(n1,"is not present in the graph")
#         else:
                
#             for node in self.graph:            #loop through keys(here keys are node)
#                 if n1 in self.graph[node]:          #checking the n1 is there in each key's dictionary
#                     self.graph[node].remove(n1)

#             self.graph.pop(n1)             #deleting that node fully


#     def delete_edge_undirect(self,n1,n2):            #undirect unweighted
#         if n1 not in self.graph:
#             print(n1,"is not present in the graph")
#         elif n2 not in self.graph:
#             print(n2,"is not present in the graph")
#         else:
#             if n1 in self.graph[n2]:
#                 self.graph[n2].remove(n1)         #removing specified element from specified node    

#             if n2 in self.graph[n1]:
#                 self.graph[n1].remove(n2)     



#     def display(self):
#         return self.graph




# g1=Graph()
# g1.add_node("A")
# g1.add_node("B")
# g1.add_node("C")
# g1.add_node("D")
# g1.add_node("E")
# g1.add_edges("A","B")
# g1.add_edges("A","C")
# g1.add_edges("C","D")
# # g1.delete_node_undirect("A")
# print(g1.display())



# #==================DFS TRAVERSAL=================
# # Push node → Pop node → Mark visited → Push UNVISITED adjacent nodes to stack → Repeat

# def dfs_traversal(graph,node):
#     visited=set()        #to avoid duplicate value
#     stack=[]

#     if node not in graph:
#         print(node,"is not present in the graph")
#         return
    
#     stack.append(node)             #this step is same as bottom step.
#     while len(stack)>0:
#         current=stack.pop()
#         if current not in visited:
#             print(current,end=" ")
#             visited.add(current)

#             for i in graph[current]:           #go and visit list of that node to get the adjascent list of that node
#                 if i not in visited:           #why this check bcos if we are adding already visited node to the stack, which will create messy. it will work without this line also.
#                     stack.append(i)            #this step is same as top step. from here loop again iterate


# graph={
#     "A":["B","C"],
#     'B': ['A', 'D', 'E'],
#     'C': ['A', 'F'],
#     'D': ['B'],
#     'E': ['B'],
#     'F': ['C']
# }

# dfs_traversal(graph,"B")



# #==================BFS TRAVERSAL===================
# # Enqueue node → Dequeue node → Visit it → Enqueue UNVISITED adjacent nodes (and mark them visited immediately) → Repeat
# from collections import deque

# def bfs_traversal(graph,node):
#     visited=set()
#     queue=deque()

#     if node not in graph:
#         print(node,"is not present in graph")
#         return
    
#     queue.append(node)         #this step and below step is same as bottom step
#     visited.add(node)            #should visit starting node first

#     while queue:
#         current=queue.popleft()
#         print(current,end=" ")

#         for i in graph[current]:
#             if i not in visited:
#                 queue.append(i)         #this step and below step is same as top step. from here same pattern works
#                 visited.add(i)



# graph={
#     "A":["B","C"],
#     'B': ['A', 'D', 'E'],
#     'C': ['A', 'F'],
#     'D': ['B'],
#     'E': ['B'],
#     'F': ['C']
# }

# bfs_traversal(graph,"A")



#CHECK A GRAPH IS CYCLIC OR NOT. DFS traversal + parent tracking + visited check inside pop loop
def is_cyclic(graph):
    visited=set()
    stack=[]

    for start in graph:               #loop through 1st node
        if start not in visited:
            stack.append((start,None))

            while len(stack)>0:
                current,parent=stack.pop()

                if current not in visited:
                    visited.add(current)

                for i in graph[current]:
                    if i not in visited:
                        stack.append((i,current))
                    elif i!=parent:
                        return True
                    
    return False


graph = {
    "a": ["b", "c"],
    "b": ["a", "c"],
    "c": ["a", "b"],
    "d": []
}

print(is_cyclic(graph))
    



#SHORTEST PATH BETWEEN 2 NODES
# from collections import deque

# def shortest_path(graph,node,target):
#     if node not in graph or target not in graph:
#         print(node,"is not present in the graph")
#         return
    
#     visited={}
#     visited[node]=None           #used to track the parent node
#     queue=deque()
#     queue.append(node)

#     while queue:
#         current=queue.popleft()

#         if current==target:
#             path=[]
#             while current:
#                 path.append(current)
#                 current=visited[current]
#             return path[::-1]

#         for i in graph[current]:
#             if i not in visited:
#                 visited[i]=current
#                 queue.append(i)
    

# graph={
#     "A":["B","C"],
#     'B': ['A', 'D', 'E'],
#     'C': ['A', 'F'],
#     'D': ['B'],
#     'E': ['B'],
#     'F': ['C']
# }

# print(shortest_path(graph,"D","A"))