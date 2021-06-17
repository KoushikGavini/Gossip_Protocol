# import the GossipNode class
from Gossip import GossipNode

# port for this node
port = 7040
# ports for the nodes connected to this node
# connected_nodes = [7010, 7050]
connected_nodes = [7010, 7050, 7060]

node = GossipNode(port, connected_nodes)