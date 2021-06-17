# import the GossipNode class
from Gossip import GossipNode

# port for this node
port = 7010
# ports for the nodes connected to this node
connected_nodes = [7000, 7030, 7040]

node = GossipNode(port, connected_nodes)