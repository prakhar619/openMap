class node:
#each node will have its own properties and list of its known neighbours (only id) and way name (edge name)
    def __init__(self,id,lat,lon):
        self.id = id
        self.lat = lat
        self.lon = lon
        self.neighbour = {}     #This dictionary for nodes stores neighbour node id and wayid by which they are connected
        #    print("Node Loaded:",id)
    def namedNodes(self,name):
        self.name = name

class graph:
    def __init__(self):
        self.allNode = []       #list of all nodes (as objects)
        self.namedPlaces = {}   #dict of named nodes (as objects) and list of nodes of named ways    { name: nodeId, name: nodeId, name: [wayId,[nodeId,nodeId,nodeId]}
       
    def nodebyId(self,id):
        for node in self.allNode:
            if node.id == id:
                return node
        #print("Node not Found")

    def road_2way(self,nodeId1,nodeId2,wayId):
        self.nodebyId(nodeId1).neighbour[nodeId2] = wayId
        self.nodebyId(nodeId2).neighbour[nodeId1] = wayId
        #print("Road (2 way) added")
