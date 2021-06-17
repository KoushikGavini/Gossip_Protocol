# Imports the Gossip_Main class
from Gossip import GossipNode

# node's port
port = 7000
# connected ports/nodes
nodes_connected = [7010, 7020]
node = GossipNode(port, nodes_connected)