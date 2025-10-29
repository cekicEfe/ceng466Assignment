import myAlgos
import sys

if(len(sys.argv) == 1):
  print("Expected args are : bfs dfs ucs gbfs astar")
elif sys.argv[1] == "bfs":
  myAlgos.bfs_test()
elif sys.argv[1] == "dfs":
  myAlgos.dfs_test() 
elif sys.argv[1] == "ucs":
  myAlgos.ucs_test()
else:
  print("Expected args are : bfs dfs ucs gbfs astar")
