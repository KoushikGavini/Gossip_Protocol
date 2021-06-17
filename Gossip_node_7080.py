# import the GossipNode class
from Gossip import GossipNode

# port for this node
port = 7080
# ports for the nodes connected to this node
# connected_nodes = [7070, 7090]
connected_nodes = [7050, 7090, 8000]
node = GossipNode(port, connected_nodes)