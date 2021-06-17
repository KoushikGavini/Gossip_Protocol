import random
import socket
from threading import Thread
import time


class GossipNode:
    # Array holds infected nodes
    infected_nodes = []

    """Init method passes the port of the node and the ports of the nodes 
    which has a connection to it
    """
    def __init__(self, port, connected_nodes):
        # Creates a socket instance and utilizes SOCK_DGRAM to transmit data 
        self.node = socket.socket(type=socket.SOCK_DGRAM)

        # Sets the address with hostname and port
        self.hostname = socket.gethostname()
        self.port = port

        # Binds the address to the socket which was just created
        self.node.bind((self.hostname, self.port))

        # Sets the ports of the nodes connected as susceptible nodes
        self.susceptible_nodes = connected_nodes

        print("Node started on port {0}".format(self.port))
        print("Susceptible nodes are", self.susceptible_nodes)

        self.start_threads()

    def input_message(self):
        while True:
            # Desired message that is going to sent to all nodes
            message_to_send = input("Enter a message to send:\n")

            # Calls send message method and passes the input message with encoding message into ascii.
            self.submit_message(message_to_send.encode('ascii'))

    def get_messages(self):
        while True:
            # Uses 'recvfrom' to receive UDP messages
            message_to_forward, address = self.node.recvfrom(1024)

            # removes the node/port of the sent node
            # from the list of susceptible nodes and
            # appends it to the list of infected nodes
            self.susceptible_nodes.remove(address[1])
            GossipNode.infected_nodes.append(address[1])

            # Sleeps for 2 seconds so time difference can be shown
            time.sleep(2)

            # Prints current time and decodes message
            print("\nMessage: '{0}'.\nReceived [{1}] from [{2}]\n"
                  .format(message_to_forward.decode('ascii'), time.ctime(time.time()), address[1]))

            # Calls send message to forward the message to other connected/suspectiable nodes
            self.submit_message(message_to_forward)

    def submit_message(self, message):
        # Utilizes random gossip distribution methodology
        while self.susceptible_nodes:
            # Uses 'sendto' inorder transmit the UDP message by connectionless protocol 
            selected_port = random.choice(self.susceptible_nodes)
            # Terminal information being outputted
            print("\n")
            print("-"*50)
            print("Susceptible nodes =>", self.susceptible_nodes)
            print("Infected nodes =>", GossipNode.infected_nodes)
            print("Port selected is [{0}]".format(selected_port))

            # Uses 'sendto' inorder transmit the UDP message by connectionless protocol 
            self.node.sendto(message, (self.hostname, selected_port))

            # Removes destination node from the list of susceptible nodes then appends it to list of infected nodes
            self.susceptible_nodes.remove(selected_port)
            GossipNode.infected_nodes.append(selected_port)

            print("Message: '{0}' sent to [{1}].".format(message.decode('ascii'), selected_port))
            print("Susceptible nodes =>", self.susceptible_nodes)
            print("Infected nodes =>", GossipNode.infected_nodes)
            print("-"*50)
            time.sleep(2)
            print("\n")

    def start_threads(self):
        # Sets two threads for entering and getting a message. 
        # Enables node to send message and recieve message
        Thread(target=self.input_message).start()
        Thread(target=self.get_messages).start()