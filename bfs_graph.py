

G = {
 0:[1,2],
 1:[4,3],
 2:[5,6],
 3:[7],
 4:[8],
 5:[8],
 6:[10],
 7:[9,11],
 8:[9],
 9:[],
 10:[],
 11:[]

}

marked = [False] * 16
def bfs(G,v):
  ans =[]
  queue=[]
  queue.append(v)
  while len(queue) > 0:
    v = queue.pop(0)
    if not marked[v]:
      ans.append(v)
      #  print(v)
      marked[v]= True
    for w in G[v]:
        if not marked[w]:
              queue.append(w)
  return ans


print(bfs(G,0))