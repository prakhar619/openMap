import elements
import xml.etree.ElementTree as et
class loader:
    def __init__(self,file):
        self.file = file 
    def matrix_loader(self):
        pass
    def diagram_loader(self):
        graphobj = elements.graph()
        xroot = et.parse(self.file).getroot()
        for elem in xroot:
            if elem.tag == "node":
                newNode = elements.node(elem.get("id"),elem.get("lat"),elem.get("lon"))
                graphobj.allNode.append(newNode)
                for childtag in elem:
                    if childtag.get("k") == "name":
                        node_name = childtag.get("v")
                        newNode.namedNodes(node_name)
                        graphobj.namedPlaces[node_name] = newNode
            if elem.tag == "way":
                flg = 0
                prevId = 0
                wayId = elem.attrib.get("id")
                way_nodeList = []
                for childelem in elem:
                    if childelem.tag == "nd" and flg == 0:
                        flg = 1
                        prevId = childelem.get("ref")
                        way_nodeList += [graphobj.nodebyId(prevId)]
                    if childelem.tag == "nd" and flg == 1:
                        newId = childelem.get("ref")
                        way_nodeList += [graphobj.nodebyId(newId)]
                        graphobj.road_2way(prevId,newId,wayId)
                        prevId = newId      
                    if childelem.tag == "tag":
                        if childelem.get("k") == "name":
                            name_way = childelem.get("v")
                            graphobj.namedPlaces[name_way] = [wayId,way_nodeList]

        return graphobj       
    def list_loader(self):
        pass

file = "./OSM_data/smallmap.osm"
obj = loader(file)
grah = obj.diagram_loader()

for x in grah.namedPlaces:
    print(x)


