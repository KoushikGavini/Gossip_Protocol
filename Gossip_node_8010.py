# import the Gossip_Main class
from Gossip import GossipNode

# Node Port
port = 8010
# Nodes Connected/Port
# connected_nodes = [8000, 8020]
nodes_connected = [7090]
node = GossipNode(port, nodes_connected)