# Imports the Gossip_Main class
from Gossip import GossipNode

# Node's port
port = 7010
# Connected ports/nodes
nodes_connected = [7000, 7030, 7040]

node = GossipNode(port, nodes_connected)