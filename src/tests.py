from myAlgos import *
 
import sys


graph_test_1 = {
  "s" : [("a",3),("b",2)],
  "a" : [("d",4)],
  "b" : [("c",6),("e",4)],
  "c" : [("g",1)],
  "d" : [("f",5)],
  "e" : [("g",2)],
  "f" : [("g",7)],
  "g" : None
}

heuristic_test_1 = {
  "s" : 7,
  "a" : 6,
  "b" : 5,
  "c" : 2,
  "d" : 6,
  "e" : 1,
  "f" : 5,
  "g" : 0
}

zero_heuristic_test_1 = {
  "s" : 0,
  "a" : 0,
  "b" : 0,
  "c" : 0,
  "d" : 0,
  "e" : 0,
  "f" : 0,
  "g" : 0  
}




graph_test_2 = {
  "s" : [("a",3),("b",4),("f",12)],
  "a" : [("b",5),("c",4)],
  "b" : [("d",3),("e",6)],
  "c" : [("f",7),("g",9999)],
  "d" : [("a",9),("c",22),("g",999999)],
  "e" : None,
  "f" : [("g",9),("h",11)],
  "h" : None,
  "g" : None
}

heuristic_test_2 = {
  "s" : 20 ,
  "a" : 17,
  "b" : 30,
  "c" : 14,
  "d" : 24,
  "e" : 9999,
  "f" : 7,
  "h" : 9999,
  "g" : 0
}

zero_heuristic_test_2 = {
  "s" : 0,
  "a" : 0,
  "b" : 0,
  "c" : 0,
  "d" : 0,
  "e" : 0,
  "f" : 0,
  "h" : 0,
  "g" : 0
}


print("****************************************")
print("*Please checkout the graphs at the file*")
print("****************************************")

if(len(sys.argv) == 1):
  print("Expected args are : bfs dfs ucs gbfs astar")

elif sys.argv[1] == "bfs":

  print("BFS version")
  print("Graph 1 : ")
  bfs(graph_test_1,"s","g")

  print(" ")
  
  print("Graph 2 : ")
  bfs(graph_test_2,"s","g")
  

elif sys.argv[1] == "dfs":

  print("DFS version")
  print("Graph 1 : ")
  dfs(graph_test_1,"s","g")

  print(" ")

  print("Graph 2 : ")
  dfs(graph_test_2,"s","g")

  
elif sys.argv[1] == "ucs":

  print("UCS version")

  print("Graph 1 : ")
  ucs(graph_test_1,zero_heuristic_test_1,"s","g")

  print("")
  
  print("Graph 2 : ")
  ucs(graph_test_2,zero_heuristic_test_2,"s","g")
  

elif sys.argv[1] == "gbfs":

  print("GBFS version")
  print("Graph 1 :")
  gbfs(graph_test_1,heuristic_test_1,"s","g")
  
  print(" ")
  
  print("Graph 2 :")
  gbfs(graph_test_2,heuristic_test_2,"s","g")

elif sys.argv[1] == "astar":

  # these doesnt make much sense since heuristic
  # function is determined from distance of s to g...
  print("A* version")
  print("Graph 1 :")
  astar(graph_test_1,heuristic_test_1,"s","g")
  
  print(" ")

  print("Graph 2 :")
  astar(graph_test_2,heuristic_test_2,"s","g")


else:
  print("Expected args are : bfs dfs ucs gbfs astar")
