This will be my first project ever.
Hopes it helps me or someone.

Project will be based on search for direction just like google maps. Data taken is from openStreetMap (Thanks for providing this).
Project is supposed to be very basic. Like reading xml data and basic navigation based on roads. 
Would try to make it scalable so that different ways can be added in future. 
Not only that, would make this project very newbies friendly (i am myself a newby).

Project can go extra large in terms of functionality and optimisation therefore will do implementation in stages
STAGE1 : Node and edges only; no concept of multiple ways; just a connected graph with nodes and edges
            Node and ways represented using matrix or linked list or tree rep
            Node to Node travel only; 
            Independent search algorithm for future optimisation
            Start Node,goal Node  = INPUT
            OUTPUT = All nodes traversed; All ways taken(if changed ways at somepoint then that node)
            OUTPUT = cost where 1node to node = 1 cost
            All nodes will be loaded on RAM (faster)

STAGE2: Node and ways only
            Node to Node,Area travel;
            Independent search algorithm for future optimisation
            Start Node,goal Node,Start Area,goal Area  = INPUT
            OUTPUT = All nodes traversed; All ways taken(if changed ways at somepoint then that node)
            OUTPUT = cost where 1node to node = Distance calculation based on log and lat
            All nodes will be loaded on RAM (faster)

Stage3: not thought off maybe some optimisation on speed or functionality advancment based on way types