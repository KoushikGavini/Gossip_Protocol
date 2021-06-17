# import the Gossip_Main class
from Gossip import GossipNode

# Node's port
port = 7040
# Connected ports/nodes
# connected_nodes = [7010, 7050]
nodes_connected = [7010, 7050, 7060]

node = GossipNode(port, nodes_connected)