MIS 543 - Project 2 - Reliable Transport Protocol

In this folder you'll find the sample receiver, code for computing and
validating checksums, as well as sender code.

===============================
Sender.py is the file in which reliable sender is implemented. Sender.py 
provides all the scaffolding you need to handle the command line arguments.

The Receiver
============
Receiver.py is the sample receiver. 

BasicSender and Sender
=======================
The BasicSender class in BasicSender.py is where the reliable sender is built. Provide the following methods:

    __init__(self,dest,port,filename): Creates a BasicSender. Specify the
        destination's hostname, the port at which the receiver is listening,
        and a filename to transmit. If no filename is provided, it will read
        from STDIN.

    receive(self, timeout): Receive a packet. Waits for a packet before
        returning. Optionally you can specify a maximum timeout to wait for a
        packet. Returns the received packet as a string, or None if receive
        times out.

    send(self,message): Sends message to the receiver specified when you
        created the sender.

    make_packet(self,msg_type,seqno,message): Creates a BEARDOWN-TP packet from
        the specified message type, sequence number, and message. Generates the
        appropriate checksum, and returns the full BEARDOWN-TP packet with
        checksum appended.

    split_packet(self,packet): Given a BEARDOWN-TP packet, splits a packet into a
        tuple of the form (msg_type, seqno, data, checksum). For packets
        without a data field, the data element will be the empty string. Note that 
        both make_packet and split_packet deal with the message as a string.

In addition, it defines one method which you must implement:

    start(self): Starts the Sender.



Checksums
=========
Checksum.py includes two functions for validating and generating checksums for
your packets:

    validate_checksum(message): Returns true if the message's checksum matches
        the message, and false otherwise. This function assumes the last field
        of the message is the checksum.

    generate_checksum(message): Returns the checksum string for a message. This
        function assumes the message includes the trailing delimiter. The
        checksum is ONLY valid if you simply append this function's result to
        the message you pass in.

Testing
=======
You are expected to write test cases for your own code to ensure compliance
with the project specifications. To assist you, we've given you a simple test
harness (TestHarness.py). The test harness is designed to intercept all packets
sent between your sender and the receiver. It can modify the stream of packets
and check to ensure the stream meets certain conditions. This is very similar
to the grading script that we will use to evaluate your projects.

We have provided three test cases (BasicTest, RandomDropTest, and RandomCorruptTest) 
as examples of how to use the test harness. These test cases send this README file 
using the specified sender implementation to the specified receiver implementation, 
passing all packets through the forwarder unmodified, dropping random packets, or 
corrupting random packets. They both then verify that the file received by the 
receiver matches the input.

To run a test using this test harness, do the following:

    python TestHarness.py -s YourSender.py -r Receiver.py

where "YourSender.py" is the path to your sender implementation, "Receiver.py"
is the path to the receiver implementation. Inside TestHarness.py, you need to
modify the function "tests_to_run" at the top of the script to include any test
cases you add.



Acknowldgement
==============
This project is based on a project from UC Berkeley CS 168, but with a recent upgrade
to Python 3.
