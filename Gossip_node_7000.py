# Imports the Gossip_Main class
from Gossip import Gossip_Main

# node's port
port = 7000
# connected ports/nodes
nodes_connected = [7010, 7020]
node = Gossip_Main(port, nodes_connected)