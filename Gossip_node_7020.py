# import the Gossip_Main class
from Gossip import GossipNode

# Node's port
port = 7020
# Connected ports/nodes
nodes_connected = [7000]

node = GossipNode(port, nodes_connected)