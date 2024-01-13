import fullLoader
from collections import deque
class search:
    def __init__(self,graph,startId,goalId):
        self.graph = graph
        self.start = startId
        self.goal = goalId
    def dfs(self):
        stack = deque()
        stack.append(self.start)
        visited = []
        actionTostate = {}
        actionTostate[self.start] = {self.start:0}
        while( len(stack) != 0):
            currentNode = stack.pop()
            visited += [currentNode]
            if currentNode == self.goal:
                print("Goal Found:",currentNode)
                break
            for neighbours,way in  self.graph.nodebyId(currentNode).neighbour.items():
                if not neighbours in visited:
                    stack.append(neighbours)
                    actionTostate[neighbours]= actionTostate[currentNode] | {neighbours:way}
        return actionTostate[self.goal]


file = "./OSM_data/smallmap.osm"
obj = fullLoader.loader(file)
grah = obj.diagram_loader()
searchobj = search(grah,"5810338229","5810338217")
final_dict = searchobj.dfs()
for node,way in final_dict.items():
    print(node,waycl)

