# import the Gossip_Main class
from Gossip import Gossip_Main

# Node port
port = 8020
# Connected nodes/ports
# connected_nodes = [8010, 8030]
nodes_connected = [7090, 8030, 8040]

node = Gossip_Main(port, nodes_connected)