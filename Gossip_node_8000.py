# import the GossipNode class
from Gossip import GossipNode

# port for this node
port = 8000
# ports for the nodes connected to this node
# connected_nodes = [7090, 8010]
connected_nodes = [7080]

node = GossipNode(port, connected_nodes)