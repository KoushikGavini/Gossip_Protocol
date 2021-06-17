# import the Gossip_Main class
from Gossip import Gossip_Main

# Node's port
port = 7080
# Connected nodes/port
# connected_nodes = [7070, 7090]
nodes_connected = [7050, 7090, 8000]
node = Gossip_Main(port, nodes_connected)