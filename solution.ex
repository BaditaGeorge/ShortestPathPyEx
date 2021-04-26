defmodule Solution do
  def read_data(path) do
    data = String.split(File.read!(path),"\r\n")
    data
  end

  def add_Neighbor(graph,key,new_value) do
    Map.put(graph,key,Map.get(graph,key) ++ [new_value])
  end

  def construct_graph(graph,[]) do
    graph
  end

  def construct_graph(graph,[head|tail]) do
    [nodeA,nodeB] = String.split(head)
    graph = if Map.has_key?(graph,nodeA) == false, do: Map.put(graph,nodeA,[]), else: graph
    graph = if Map.has_key?(graph,nodeB) == false, do: Map.put(graph,nodeB,[]), else: graph
    graph = add_Neighbor(graph,nodeA,nodeB)
    graph = add_Neighbor(graph,nodeB,nodeA)
    construct_graph(graph,tail)
  end

  def compute_Distance(q,distances,neighbor,curr_distance) do
    if Map.has_key?(distances,neighbor) == false, do: [q ++ [neighbor],Map.put(distances,neighbor,curr_distance + 1)], else: [q,distances]
  end

  #Here i enqueue unvisited neighbors and use compute_Distance function to update queue and set distance for new visited node.

  def enque_neighbors([],_,distances,q) do
    [q,distances]
  end

  def enque_neighbors([frst|rest],curr_distance,distances,q) do
    [q,distances] = compute_Distance(q,distances,frst,curr_distance)
    enque_neighbors(rest,curr_distance,distances,q)
  end

  #This is the root of my recursive bfs implementation.
  #I add to the queue unvisited neihgbors of the current node and continue my iteration throught queue.

  def bfs_shortestPath(_,[],_,_) do
    -1
  end

  def bfs_shortestPath(graph,[current|q],target,distances) do
    [q,distances] = enque_neighbors(graph[current],Map.get(distances,current),distances,q)
    if target == current do
      distances[target]
    else
      bfs_shortestPath(graph,q,target,distances)
    end
  end

  def get_shortestPath(graph,startNode,stopNode) do
    distances = Map.put(%{},startNode,0)
    bfs_shortestPath(graph,[startNode],stopNode,distances)
  end

  def solve(path) do
    lines = read_data(path)
    graph = %{}
    graph = construct_graph(graph,lines)
    IO.inspect(get_shortestPath(graph,"A","T"))
    IO.inspect(get_shortestPath(graph,"B","H"))
  end
end

Solution.solve("./data.txt")
