import myAlgos
import sys

print("I couldnt test these algorithms for cyclic? graphs or graphs with dead ends !!!")
print("And \"tests\" is just this graph with these start and goals")

print("Graph : ")
print(myAlgos.graph)

print("Heuristic : ")
print(myAlgos.heuristic)

print("Tests : ")
print("search : s "," find : g")
print("search : b "," find : g")
print("search : g "," find : g")
print("search : a "," find : g")

print("")

if(len(sys.argv) == 1):
  print("Expected args are : bfs dfs ucs gbfs astar")
elif sys.argv[1] == "bfs":
  myAlgos.bfs_test()
elif sys.argv[1] == "dfs":
  myAlgos.dfs_test() 
elif sys.argv[1] == "ucs":
  myAlgos.ucs_test()
elif sys.argv[1] == "gbfs":
  myAlgos.gbfs_test()
elif sys.argv[1] == "astar":
  myAlgos.astar_test()
else:
  print("Expected args are : bfs dfs ucs gbfs astar")
