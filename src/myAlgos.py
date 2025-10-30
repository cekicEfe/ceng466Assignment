
def trace_back(node_set,start,goal):
  current = goal
  weight = 0;
  route = [current]
  while current is not start:

    #node ,edge_weight , cumul_weight(used in ucs and a*)
    if len(node_set[current]) == 3: 
      adjacent,edge_weigth,_ = node_set[current]
    else:
      adjacent,edge_weigth = node_set[current]
    weight += edge_weigth
    current = adjacent
    route.append(current)
  route.reverse()
  return (route,weight)
  
# this is just layer by layer search
# and throws error if it cant find goal 
def bfs(graph,start,goal):
  if start in graph and goal in graph:
    print("Starting from :",start,", Searching : " + goal)

    found_goal = False
    visited_nodes = []
    #current_node , came_from , weigth
    found_nodes = [(start,start,0)] #start from the first node
    path_set = dict()
    
    while len(found_nodes) != 0:

      node = found_nodes.pop(0)
      visited_nodes.append(node[0])

      #is this node goal ?
      if node[0] is goal: #yes its goal

        #update path_set then getout
        path_set[goal] = (node[1],node[2])
        found_goal = True
        break
      else: # no its not goal

        #did we visit this node before?
        if node[0] in path_set: # we did visit this node

          #then dont expend it
          continue
        else: # no we didnt visit this before
          path_set[node[0]] = (node[1],node[2])

          #update path then push its children is not deadend
          if graph[node[0]] is not None:
            for each_child in graph[node[0]]:
                found_nodes.append((each_child[0],node[0],each_child[1]))
          
    if found_goal:
      (resulth,weight) = trace_back(path_set,start,goal)
      print("THE PATH: ",end="");
      print(resulth)
      print("THE WEIGHT: ",end="")
      print(weight)
      print("THE VISITED NODES : ",end="")
      print(visited_nodes)
      return (resulth,weight)
    else:
      print("Couldnt find goal")
      return False
  else:
    raise ValueError('Invalid args')

# stack overflow is going to kill me AND this function but well... it works :(
# IFF python doesnt have tail call recursion
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
    visited_nodes = []
    
    def delve_deeper(current_node,came_from,weight):

      # did we find goal ?
      if current_node is goal: #yes we find the goal
        path_set[current_node] = (came_from,weight)
        return True

      else: #no we didnt
        did_find_goal = False
        if graph[current_node] is not None:
          for each_value in graph[current_node]:
            if each_value[0] in path_set:
              return False              
            else:
              path_set[each_value[0]] = (current_node,each_value[1])
              did_child_find_goal = delve_deeper(each_value[0],current_node,each_value[1])
              did_find_goal = did_find_goal or did_child_find_goal
              if did_find_goal:
                return True
                break
              
        
        

              
    found_goal = delve_deeper(start,start,0)

    if found_goal:
      (resulth,weight) = trace_back(path_set,start,goal)
      print("THE PATH: ",end="");
      print(resulth)
      print("THE WEIGHT: ",end="")
      print(weight)
      print("THE VISITED NODES : ",end="")
      print(visited_nodes)
      return (resulth,weight)
    else:
      print("Couldnt find goal")
      return False

  else:
    raise ValueError('Invalid args')




import heapq

class Node:
  def __init__(self, name ,came_from, weigth , cumulative_weigth):
      self.name = name
      self.came_from = came_from
      self.weigth = weigth
      self.cumulative_weigth = cumulative_weigth

  def __lt__(self, other):
      return self.cumulative_weigth < other.cumulative_weigth

# my ucs imp is a hot mess
# 
# pushed nodes neads to be compared by their cumulative weigth
# so I had wrap them in a class which utilizes __lt__ field
# so heap can actually sort them
# it works at least
#
# this one should be complete compared to bfs and dfs
# (complate as in : it doesnt break when it cannot find the goal
# or gets stuck on graph loops or expands them for no reason*)
#
# *: it will still expand some nodes if we find its shorter version to update the nodes in it
#
#             vvvvvvvvv surprise for later
def ucs(graph,heuristic,start,goal):
  if (start in graph and goal in graph) and (start in heuristic and goal in heuristic):
    print("Starting from :",start,", Searching : " + goal)
    #current_node , came_from , edge_weight, cumul_weight
    found_nodes = [Node(start,start,0,0)]
    heapq.heapify(found_nodes)
    path_set = dict() # node : (came_from,edge_weight,cumul_weight)
    visited_nodes = []
    found_goal = False

    #did we finish ?
    while len(found_nodes) != 0: #nope

      #look at the current shortest node
      node = heapq.heappop(found_nodes)
      visited_nodes.append(node.name)
  
      #is it goal ?
      if node.name is goal:
        found_goal = True
        #did we find the goal before ?
        if goal in path_set: #yep we found it

          #is this node shorter than our previous vers. of goal ?
          if  (node.cumulative_weigth + heuristic[node.name]) < path_set[goal][2]:#yes

            #update our goal
            path_set[goal] = (node.came_from ,node.weigth ,(node.cumulative_weigth + heuristic[node.name]))

          else:
            #do nothing
            pass

        # this is a new goal!
        else:     
          #set our goal
          path_set[goal] = (node.came_from ,node.weigth ,(node.cumulative_weigth + heuristic[node.name]))


      #nope this not goal
      else:        

        #did we find goal before?
        if goal in path_set:

          # does this node can lead to a shorther path (this.cumulative < goal.cumulative)?
          if (node.cumulative_weigth + heuristic[node.name]) < path_set[goal][2]:#yes!
            #let this node go on
            pass
              
          else: # no it cannot ! skip this node
            continue
          
        else:#no we didnt find goal before...
          pass

        #did we visit this before ?
        if node.name in path_set: #yes we visited this before!

          #is this one shorter than the prev ?
          if  (node.cumulative_weigth + heuristic[node.name]) < path_set[node.name][2]: #yes this is shoreter

            #update the node
            path_set[node.name]= (node.came_from,
                                  node.weigth,
                                  (node.cumulative_weigth + heuristic[node.name]))

            #also start updating its children
            # IF its not a deadend
            if graph[node.name] is not None:
              for each_child in graph[node.name]:
                heapq.heappush(found_nodes,Node(each_child[0],
                               node.name,
                               each_child[1],
                               (node.cumulative_weigth + heuristic[node.name])+each_child[1]))  

          else: #no its not shorter
            #screw that
            pass

        #no we havent visited this before
        else:

          #update the node
          path_set[node.name]= (node.came_from,
                                node.weigth,
                                (node.cumulative_weigth + heuristic[node.name]))
                                   
          # also start pushing its children to the heap
          # IF its not a deadend
          if graph[node.name] is not None:
            for each_child in graph[node.name]:
              heapq.heappush(found_nodes,Node(each_child[0],
                             node.name,
                             each_child[1],
                             (node.cumulative_weigth + heuristic[node.name])+each_child[1]))

    if found_goal:
      (resulth,weight) = trace_back(path_set,start,goal)
      print("THE PATH: ",end="");
      print(resulth)
      print("THE WEIGHT: ",end="")
      print(weight)
      print("VISITED NODES: ",end="")
      print(visited_nodes)

      return (resulth,weight)
    else:
      print("Couldnt find goal")
      return False
  else:    
    raise ValueError('Invalid args')


#overkill as always
class HeuristicNode():
  def __init__(self, name ,came_from, weigth , heuristic):
      self.name = name
      self.came_from = came_from
      self.weigth = weigth
      self.heuristic = heuristic

  def __lt__(self, other):
      return self.heuristic < other.heuristic
    
#this is just dfs that prioritizes heuristic values (list version)
def gbfs(graph,heuristic,start,goal):
  if (start in graph and goal in graph) and (start in heuristic and goal in heuristic):
    print("Starting from :",start,", Searching : " + goal)

    found_goal = False
    path_set = dict()
    found_nodes = [HeuristicNode(start,start,0,heuristic[start])]
    heapq.heapify(found_nodes)
    visited_nodes = []

    while len(found_nodes) != 0:
      #look at the node
      node = heapq.heappop(found_nodes)
      visited_nodes.append(node.name)

      #is current node goal ?
      if node.name is goal : #Yes it is goal

        #update path_set then getout
        path_set[node.name] = (node.came_from,node.weigth)
        found_goal=True
        break

      #no it is not goal
      else:
        
        # push nodes children to the list prioritizing its heuristic value
        # if its not a deadend
        if graph[node.name] is not None:
          for each_child in graph[node.name]:
            path_set[each_child[0]] = (node.name,each_child[1])
            heapq.heappush(found_nodes,HeuristicNode(each_child[0],node.name,each_child[1],heuristic[each_child[0]]))

    if found_goal:
      (resulth,weight) = trace_back(path_set,start,goal)
      print("THE PATH: ",end="");
      print(resulth)
      print("THE WEIGHT: ",end="")
      print(weight)
      print("VISITED NODES: ",end="")
      print(visited_nodes)

      return (resulth,weight)

    else:
      print("Couldnt find goal")
      return False

  else:
    raise ValueError('Invalid args')

# and of course a* is ucs with h(n) value
# in the test cases you will see zero heuristic on ucs
# but on a* you will see a proper one
def astar(graph,heuristic,start,goal):
  ucs(graph,heuristic,start,goal)

