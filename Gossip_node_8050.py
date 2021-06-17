# import the GossipNode class
from Gossip import GossipNode

# port for this node
port = 8050
# ports for the nodes connected to this node
# connected_nodes = [8040]
connected_nodes = [8030]

node = GossipNode(port, connected_nodes)