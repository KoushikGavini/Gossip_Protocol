# import the GossipNode class
from Gossip import GossipNode

# port for this node
port = 8010
# ports for the nodes connected to this node
# connected_nodes = [8000, 8020]
connected_nodes = [7090]
node = GossipNode(port, connected_nodes)