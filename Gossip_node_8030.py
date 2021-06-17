# import the Gossip_Main class
from Gossip import Gossip_Main

# Node Port
port = 8030
# Connected nodes/ports
# connected_nodes = [8020, 8040]
nodes_connected = [8020, 8050]

node = Gossip_Main(port, nodes_connected)