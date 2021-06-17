# import the Gossip_Main class
from Gossip import GossipNode

# Node's port
port = 7050
# Connected ports/nodes
# connected_nodes = [7040, 7060]
nodes_connected = [7040, 7070, 7080]

node = GossipNode(port, nodes_connected)