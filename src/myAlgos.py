
graph = {
  "s" : [("a",3),("b",2)],
  "a" : [("d",4)],
  "b" : [("c",6),("e",4)],
  "c" : [("g",1)],
  "d" : [("f",5)],
  "e" : [("g",2)],
  "f" : [("g",7)],
  "g" : None
}

heuristic = {
  "s" : 7,
  "a" : 6,
  "b" : 5,
  "c" : 2,
  "d" : 6,
  "e" : 1,
  "f" : 5,
  "g" : 0
}

def trace_back(node_set,start,goal):
  current = goal
  weight = 0;
  route = [current]
  while current is not start:
   #node ,edge_weight , cum_weight(used in ucs and a*)
    adjacent,edge_weigth,_ = node_set[current]
    weight += edge_weigth
    current = adjacent
    route.append(current)
  route.reverse()
  return (route,weight)
  
# this is just layer by layer search
# it does expand expanded nodes :(
# and throws error if it cant find goal 
def bfs(graph,start,goal):
  if start in graph and goal in graph:
    print("Starting from :",start,", Searching : " + goal)

    visited_nodes = []
    found_nodes = [start]
    last_node = start
    path_set = dict([(start,(start,0))])
    get_out = False
    
    while len(found_nodes) != 0 and not get_out :
      last_node = found_nodes[0]

      if found_nodes[0] == goal:
        visited_nodes.append(goal)
        print("Found goal")
        break

      for adjacent in graph[found_nodes[0]]:
        if adjacent is not None:
          if found_nodes[0] == goal:
            print("Found Goal")
            get_out=True
            break
          if adjacent[0] in path_set:
            pass
          else:
            path_set[adjacent[0]] = (last_node,adjacent[1])
          found_nodes.append(adjacent[0])
        else:
          visited_nodes.append(found_nodes.pop(0))
          get_out = True
          break
      visited_nodes.append(found_nodes.pop(0))

    #print("Node set")
    #for myset,came_from in path_set.items():
    #  print(myset,came_from)
  
    print("THE VISITED NODES")
    print(visited_nodes)

    (resulth,weight) = trace_back(path_set,start,goal)
    print("THE PATH: ",end="");
    print(resulth)
    print("THE WEIGHT: ",end="")
    print(weight)


    return trace_back(path_set,start,goal)
  else:
    raise ValueError('Invalid args')

def bfs_test():
  print("BFS version")
  bfs(graph,"s","g")
  print(" ")
  bfs(graph,"b","g")
  print(" ")
  bfs(graph,"g","g")
  print(" ")
  bfs(graph,"a","g")

# stack overflow is going to kill me AND this function but well... it works :(
# of course it is cheatey
# 
# alternative to this would be pushing the found nodes to the position of the popped parent
# like here -> |s| | | | : we find a b
#              |a|b| | | : and push to the s'es position
#              |d|b| | | : we found d from a and pushed
#              |d|c|e| | : we found c and e and pushed to b
# and only stop at the first g
# or when the list is empty which means that there is no way to the goal but
# we technically check it at the function start
# but we must assume that there is a way from start to goal
#
# but I didnt do any of that
# heres just recursive dfs  
def dfs(graph,start,goal):
  if start in graph and goal in graph:
    print("Starting from :",start,", Searching : " + goal)
    path_set = dict()
    visited_nodes = [start]

    def delve_deeper(current_node,came_from,weight):
      path_set[current_node] = (came_from,weight)
      if current_node is goal:
        path_set[goal] = (came_from,weight)
        return True
      else:
        if current_node in graph:
          for each_value in graph[current_node]:
            if each_value is not None:
              if delve_deeper(each_value[0],current_node,each_value[1]) is True:
                return True
        else:
          return False      
        return False

    res = delve_deeper(start,start,0)
    if res is True:
      print(path_set)
      
      (resulth,weight) = trace_back(path_set,start,goal)
      print("THE PATH: ",end="");
      print(resulth)
      print("THE WEIGHT: ",end="")
      print(weight)

      return trace_back(path_set,start,goal)
    else:
      print("There is somehow no way from start to goal")
  else:
    raise ValueError('Invalid args')

def dfs_test():
  print("DFS version")
  dfs(graph,"s","g")
  print(" ")
  dfs(graph,"b","g")
  print(" ")
  dfs(graph,"g","g")
  print(" ")
  dfs(graph,"a","g")
 #print("NO WAY TEST")
 #dfs(graph,"f","s")


# my ucs imp is a hot mess
# but I game my everything for this one !!!!
# 
# pushed nodes neads to be compared by their cumulative weight
# so I had wrap them in a class which utilizes __lt__ field
# so heap can actually sort them
# it works at least
#
# this one should be complete compared to bfs and dfs
# (complate as in : it doesnt break when it cannot find the goal
# or gets stuck on graph loops or expands them for no reason*)
#
# *: it will still expand some nodes if we find its shorter version to update the nodes in it
import heapq

class Node:
  def __init__(self, name ,came_from, weigth , cumulative_weigth):
      self.name = name
      self.came_from = came_from
      self.weigth = weigth
      self.cumulative_weigth = cumulative_weigth

  def __lt__(self, other):
      return self.cumulative_weigth < other.cumulative_weigth

def ucs(graph,start,goal):
  if start in graph and goal in graph:
    print("Starting from :",start,", Searching : " + goal)
    #current_node , came_from , edge_weight, cumul_weight
    found_nodes = [Node(start,start,0,0)]
    heapq.heapify(found_nodes)
    path_set = dict() # node : (came_from,edge_weight,cumul_weight)
    visited_nodes = []

    #did we finish ?
    while len(found_nodes) != 0: #nope

      #look at the current shortest node
      node = heapq.heappop(found_nodes)
      visited_nodes.append(node.name)

      #is it goal ?
      if node.name is goal:

        #did we find the goal before ?
        if goal in path_set: #yep we found it

          #is this node shorter than our previous vers. of goal ?
          if node.cumulative_weigth < path_set[goal][2]:#yes

            #update our goal
            path_set[goal] = (node.came_from ,node.weigth ,node.cumulative_weigth)

          else:
            #do nothing
            pass

        # this is a new goal!
        else:     
          #set our goal
          path_set[goal] = (node.came_from ,node.weigth ,node.cumulative_weigth)

      #nope this not goal
      else:        

        #did we find goal before?
        if goal in path_set:

          # does this node can lead to a shorther path (this.cumulative < goal.cumulative)?
          if node.cumulative_weigth < path_set[goal][2]:#yes!
            #let this node go on
            pass
              
          else: # no it cannot ! skip this node
            continue
          
        else:#no we didnt find goal before...
          pass

        #did we visit this before ?
        if node.name in path_set: #yes we visited this before!

          #is this one shorter than the prev ?
          if node.cumulative_weigth < path_set[node.name]: #yes this is shoreter

            #update the node
            path_set[node.name]= (node.came_from,
                                  node.weigth,
                                  node.cumulative_weigth)

            #also start updating its children
            for each_child in graph[node.name]:
              heapq.heappush(found_nodes,Node(each_child[0],
                             node.name,
                             each_child[1],
                             node.cumulative_weigth+each_child[1]))  

          else: #no its not shorter
            #screw that
            pass

        #no we havent visited this before
        else:

          #update the node
          path_set[node.name]= (node.came_from,
                                node.weigth,
                                node.cumulative_weigth)
                                   
          #also start pushing its children to the heap
          for each_child in graph[node.name]:
            heapq.heappush(found_nodes,Node(each_child[0],
                           node.name,
                           each_child[1],
                           node.cumulative_weigth+each_child[1]))

    #
    #print(path_set)
  
    (resulth,weight) = trace_back(path_set,start,goal)
    print("THE PATH: ",end="");
    print(resulth)
    print("THE WEIGHT: ",end="")
    print(weight)

    return trace_back(path_set,start,goal)  

def ucs_test():
  print("UFS version")
  ucs(graph,"s","g")
  print(" ")
  ucs(graph,"b","g")
  print(" ")
  ucs(graph,"g","g")
  print(" ")
  ucs(graph,"a","g")
  
def gbfs(graph,heuristic,start,goal):
  
