# import the Gossip_Main class
from Gossip import GossipNode

# Node port
port = 8020
# Connected nodes/ports
# connected_nodes = [8010, 8030]
nodes_connected = [7090,8030]

node = GossipNode(port, nodes_connected)