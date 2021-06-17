# import the GossipNode class
from Gossip import GossipNode

# port for this node
port = 8030
# ports for the nodes connected to this node
# connected_nodes = [8020, 8040]
connected_nodes = [8020, 8050]

node = GossipNode(port, connected_nodes)