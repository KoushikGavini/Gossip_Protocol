# import the Gossip_Main class
from Gossip import Gossip_Main

# Node port
port = 7070
# Connected ports/nodes
# # connected_nodes = [7060, 7080]
nodes_connected = [7050]
node = Gossip_Main(port, nodes_connected)