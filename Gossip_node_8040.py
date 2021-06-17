# import the Gossip_Main class
from Gossip import GossipNode

# Node port
port = 8040
# Connected nodes/ports
# connected_nodes = [8030, 8050]
nodes_connected = [8030,8050]

node = GossipNode(port, nodes_connected)