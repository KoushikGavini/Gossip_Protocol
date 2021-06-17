# import the Gossip_Main class
from Gossip import Gossip_Main

# Node port
port = 8040
# Connected nodes/ports
# connected_nodes = [8030, 8050]
nodes_connected = [8020]

node = Gossip_Main(port, nodes_connected)