# Overview
##### Objective:
* Generate a network consisting of 16 nodes running simultaneously where one node can at maximun know only three other nodes and disseminate broadcast message using gossip protocol. 

##### Methodology: 
* Each node has two API methods `submit_message` and `get message`. They can be viewed in `Gossip.py`
* UDP for communication
* Every node will receive the message, a node transmits using gossip dissemination.
# Instructions

### Step 1: Start the Gossip Nodes
#TODO(Koushikg): dockerize nodes so it is easier to setup env
* start nodes separately in each terminal 

```shell
python Gossip_node_7000.py
```
### Step 2: Enter a message
* Enter a message from any node and view other node's terminal as the message is received
```shell
Node started on port 7000
Susceptible nodes => [7010, 7020]
Enter a message to send:

hello from 7000
```
# Resources used

* https://stackoverflow.com/questions/31121906/how-to-guarantee-that-all-nodes-get-infected-in-gossip-based-protocols

* https://signalprocessingsociety.org/CAMSAP2013/papers/1569808853.pdf

* https://www.gsd.inesc-id.pt/~ler/reports/LPR_GossipBasedBroadcast.pdf

* https://codereview.stackexchange.com/questions/95671/gossip-algorithm-in-distributed-systems


