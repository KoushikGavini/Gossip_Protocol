# import the GossipNode class
from Gossip import GossipNode

# port for this node
port = 7020
# ports for the nodes connected to this node
connected_nodes = [7000]

node = GossipNode(port, connected_nodes)