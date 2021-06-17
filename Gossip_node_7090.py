# import the GossipNode class
from Gossip import GossipNode

# port for this node
port = 7090
# ports for the nodes connected to this node
# connected_nodes = [7080, 8000]
connected_nodes = [7080,8010,8020]
node = GossipNode(port, connected_nodes)