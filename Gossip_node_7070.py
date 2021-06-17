# import the GossipNode class
from Gossip import GossipNode

# port for this node
port = 7070
# ports for the nodes connected to this node
# connected_nodes = [7060, 7080]
connected_nodes = [7050]
node = GossipNode(port, connected_nodes)