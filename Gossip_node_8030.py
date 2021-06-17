# import the Gossip_Main class
from Gossip import GossipNode

# Node Port
port = 8030
# Connected nodes/ports
# connected_nodes = [8020, 8040]
nodes_connected = [8020,8040]

node = GossipNode(port, nodes_connected)