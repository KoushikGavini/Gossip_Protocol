# import the Gossip_Main class
from Gossip import GossipNode

# Node's port
port = 7030
# Connected ports/nodes
nodes_connected = [7010]

node = GossipNode(port, nodes_connected)