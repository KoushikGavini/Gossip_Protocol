# import the GossipNode class
from Gossip import GossipNode

# port for this node
port = 8020
# ports for the nodes connected to this node
# connected_nodes = [8010, 8030]
connected_nodes = [7090, 8030, 8040]

node = GossipNode(port, connected_nodes)