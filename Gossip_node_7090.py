# import the Gossip_Main class
from Gossip import Gossip_Main

# Node port
port = 7090
# Connected node/ports
# connected_nodes = [7080, 8000]
nodes_connected = [7080,8010,8020]
node = Gossip_Main(port, nodes_connected)