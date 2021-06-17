# import the GossipNode class
from Gossip import GossipNode

# port for this node
port = 8040
# ports for the nodes connected to this node
# connected_nodes = [8030, 8050]
connected_nodes = [8020]

node = GossipNode(port, connected_nodes)