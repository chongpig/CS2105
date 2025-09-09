# CS2105 Lecture 1

## 1. Internet :"nuts and bolts" View
* The Internet is a network of connected computing decives , such devices are known as hosts/end systems.
* Hosts run network applications  

## 2. Network Edge(Access Network)
Host access the Internet through Access Network

## 3. Network core
* A mesh of interconnected routers
* How is data transmitted through network?
  * Circuit switching: dedicate circuit per call: End-end resources allocated to and reserved for "call" between source & dest
    1. call steup required
    2. circuit-like (guaranteed) performance
    3. circuir segment idle if not used by call
    4. commonly used in traditional telephone
  * Packet switching: date sent thru net in discrete chunks, Host sending function:
    1. breaks application message into smaller chunks, known as packets, of length L bits
    2. transmits packets onto the link at transmission rate R,link transmission rate is aka link capacity or link band width
    packet transmission delay = time needed to transmit L-bit packet into link = L(bits)/R(bits/sec)
    3. Packets are passed from one router to the next across links on path from source to destination
    4. Store and forward: entire packet must arrive at a router before it can be transmitted one the next link
    5. Routers determine source-destination route taken by packets
      * Routing algorithms
    6. Adressing  each packet needs to carry source and destination information
* Internet Structure : Network of Networks
  * Host connest tto Internet via access ISPs(Internet Service Providers)
  * Access ISPs in turn must be interconnected
  * Resulting network of networks is very complex
  * Therefore the Internet is a network of networks

## 4. Delay, Loss and Throughput in Networks
  1. How do Delay and Loss Occur:
  * Packet queue in router buffers: wait for turn to be sent out one by one
  * Packet arriving to full queue will be dropped(lost)
  2. Four Sources of Packet Delay: 
* trans mission delay
* propagation delay
* processing delay 
* queueing delay


    $$ 
    d_trans : transmission delay 
    L:packet length(bits)
    R:link bandwidth(bps)
    d_trans = L/R
    
    d_prop : propagaation delay
    d:length of physical link
    s:propagation speed in medium
    d_drop = d/s
    $$

3. Throughput:

   Throughput: how many bits can be transmitted per unit time.
   * Throughput  is measured fir end-to-end  communication
   * Link capacity(bandwidth) is meant for a specific link.

## 5. Network Protocols
* Network apps exchange messages and communicate among peers according to protocols.
	* A protocol defines format and order of messages exchanged and the actions taken after messages are sent or received.
* Protocols in the Internet are logicallt organized into 5 "layers" according to their purposes.
	1. applications
	2. transport
	3. network
	4. link
	5. physical
	    Two additional layers not present in Internet Protocol Stack: presentation/session
---
# L2
## 1.Principles of network applications
###  Classic structure of network applications
Client-Server Architecture:
1. Server:
	* Wait for incoming requests
	* Provides requested service to client
	* data centers for scaling
2. Client:
	* Initiates contact with server("speaks first")
	* Typicallt requests service from server
	* For Web client is usually implemented in browser

P2P Architecture:
* No always on server
* Arbitrary end systems directly communicate
* Peers requeest service form other peers, provide service in return to other peers
* Peers are intermittently connected and change IP addresses
### What transport service does an app need
* Data integrity:
	1. Some apps (e.g. transfer, web transcations) require 100% reliable data transfer
	2. other apps can tolerate some data loss
* Throughput:
	1. some apps (e.g. multimedia) require minimum amount of bandwidth to be effctive
	2. other apps (e.g. file transfer) make use of whatever throughput available
* Timing :
	1. some apps (e.g. onlime interactive games) require lowdelay to be effective
* Security: 
	1. encryption, data integrity authentication
### Transport layer protocols: TCP/UDP
App-layer protocols ride on transport layer protocols:
TCP Service:
* reliable data transfer
* flow control: sender won't overwhelm receiver
* congestion control: throttle sender when network is overloaded
* does not provide: timing, minimum throughput

UDP Service:
* unreliable data transfer
* no flow control
* no congestion control
* does not provide : timing, throughput guaranatee or security

## Web and http
### Some jargon
* A web page typically consists of :
	* base HTML file, and
	* several referenced objects
* An object can be HTML file,JPEG image, Java applet, audio file
* Each object is addressable by a URL, e.g.
### HTTP
#### Hypertext transfer protocol:
* Web's application layer protocol
* Client/server model:
	* client: usually is browser that requestss, receives and displays Web objects
	* server: web serve sends objects in response to requests
* http 1.0: RFC1945
* http 1.1 : RFC 2616
#### Http Over TCP
HTTP uses TCP as transport service
* Client initiates TCP connection to server
* Server acceptsTCP connection request from client
* HTTPmessages are exchanged between browser (HTTP client) and Web server(HTTP server) over TCP connection
* TCP connection closed
#### Two types of HTTP Connections
* Non-persistent HTTP(1.0):
	* at most one object sent  over a TCP connection, connection then closed
	* downloading multiple objects required multiple connections
* Persistent HTTP(1.1):
	* Multiple objects can be sent over single TCP connection beetween client, server
#### Response Time for non-perisistent HTTP:
RTT: time for a packet to travek from client to server and go back
HTTP response time:
* one RTT to establish TCP connection
* one RTT for HTTP request and the first few bytes of HTTP response to return
* file transmission time
* non-persistent HTTP response time = 2 * RTT + file transmission time
#### HTTP request message:
request line (GET method) : method URL version \r\n
header lines: header field name value \r\n
entity body
(\r\n newline indicators)
#### HTTP response status code
200: OK; 301: MOved Permanently; 403: Forbidden; 404: Not Found
#### Cookies:
* HTTP is designed to be stateless:
	Server maintains no information about past client requests
* Sometimes it's good to maintain states(history) at serber/client over multiple transactions
* Cookie: http messages carry "state"
	1. cookie header field of HTTP request /reponse messages
	2. cookie file kept on user's host, managed by user's browser
	3. back-end database at Web site
#### Conditional GET:
* Goal : dont send object if (client) cache has up-to-date cached version
* cache: specify date og cached copy in HTTP request
* server : response contains no object of cached copy os up-to-date
---
# L3
## 1. Domain name system
### 1.1 Two ways to identify a host
	* Host name: e.g. www.example.org
	* IP address e.g. 93.184.216.34
### 1.2DNS translates between the two
* Mapping between host names and IP addresses(and others) are stired as resource records(RR)
	RR format: (name, value, type, ttl)
	type = A
		name is hostname
		value os IP address
	type = CNAME
		name is alias name(e.g. name is alias name)
		value is canonical name(e.g. mgnzsqc.s.incapdns.net)
	type = NS
		name is domain(e.g. nus.edu.sg)
	type = MX
		value is name of mail server associated with name
### 1.3 Distributed HIerarchical Database
* DNS stored RR in distributed dartabases implemented in hierarchy of many name servers
Root DNS servers -> com/org/edu
* quereis root server -> queries DNS server -> get IP address
* TLD and authoritative servers
	* Top level domain(TLD) servers e.g. uk sg, jp
	* Authoritative servers:
		Organization's own DNS servers, providing authoritative hostname to IP mappings for organization's named hosts
		can be maintained by organization or service provider
* DNS caching
	Once a name server learns mapping, it caches mapping
* DNS Name resolution:
	iterative query/recursive query
## 2. socket programming
### 2.1 processes
* program running within a host
	* Within the same host, two processes communicate using inter-process communication
	* Processes in differert hosts communicate by sxchanging messages
* Addressing processes
	* IP address is used to identify  a host
	* A process is idenetify by(IP address , port number)
* Postal service:
	* deliver letter to the doorstep: home address
	* dispatch letter to the right person in the house: name of the receriver as stated on the letter
* Protocol service:
	* deliver packet to the right host: IP  address of the host
	* dispatch packet to the right process in the host: port number of the process

### 2.2 Sockets:
* Socket is the software interface between app processes and transport layer protocols(The conbination of an IP address and a port number)
	* Process sends/receives messages to/from its socket
	* Programming-wise: a set of APIs
* Apps (or processes)treat the Interneet as a nnlack box,sending and receiving messages through sockets
* Two types of sockets: 
	* TCP: reliable, byte stream-oriented socket
	* UDP: unreliable datagram socket
* UDP: no "connection" between cliednt and server
	Sender(client) explicitly attaches destination IP address and porrt number to each packet\
	Recerver(server) extracts sender IP address and port number from the recerved packet
* TCP: 
	When client creates socket, client TCP establishes a connection to server TCP
	When contacted by client, server TCP creates a new socket for server process to communicate with that client: allows server to talk with mulriple clients individually
	
# L3 Transport layer
## 3.1 Transport layer services
* Deliver messages between applicaation processes running on different hosts
	* Two popuar protocols: TCP, UDP
* Transpert layer protocols run in hosts
	* Sender side: breaks app message into segments, passed them to network layer
	* Receiver side: reassembles segments into message, passes it to app layer
	* Packet switches(routers) in between: only check destination IP address to decide routing.

* UDP adds very little service on top of IP
	* multiplexing at sender: UDP gathers data from processes, forms packets and passes then to IP
	* De-multiplexing ar receiver: UDP receives packets from lower layer and dispatches them to the right processes
	* Cheksum
* UDP is unreliable

* Connectionless De-multiplexing
	* When UDP receiver receives a UDP segment:
		* Checks destnition port in segment
		* Directs UDP segment to the socket with that port
		* IP datagrams with the same dsstnition port will be directed to the same UDP socket at destinition

* UDP header
1			16			32
source port #		dest port #
length 				checksum
Application data(message)

* UDP Checksum
	Goal: to detect "errors"(filpped bits) in transmitted segment
	Sender:
		* compute checksum value
		* put check value into UDP checksunmu field
	Receiver:
		* compute checksum oif receive segment
		* check if computed checksum equals checksem field value
			* NO - error detected
			* YES- no error detected(but may exists error)
* How is UDP checksum computed:
	1. Trear UDP segment as asequence of 16-bit integers
	2. Apply binary addition on every 16-bit integer
	3. Carry from the most significant bit will be added to the result(add 1 or 0 to the result)
	4. Compute 1's complement to get UDP checksum

## 3.2 Principles of Reliable Data Transfer
* Transport vs. Network layer
	* Transport layer resides on end hosts and provides process to process communication
	* Network layer provides hots to host, best effort and unreliable communication
	* Underlying network may:
		* corrupt packets
		* drop packets
		* re-order packets
		* deliver packets after an arbitrarily long delay
	* End-to-End reliable transport service should
		* guarrantee packets delivery and corrextness
		* deliver packets (to receiver application) in the same ordre they are sent
	
* Reliable Data transfer protocols
	* rdt
* Finite State Machine
* rdt1.0: Perfectly reliable channel
	* Assume underlying channel is perffectly reliable
	* Seperate FSMs for sender, receiver:
		* Sender sends data into inderlying(perfect) channel
		* Receiver reads data from underlying(perfect) channel
* rdt 2.0 Channel with bit errors
	* Assumption:
		* underlying channel mahy flip bits in packets
		* other than that, the channel is perfect
	* Receiver may us checksum to detect bit errors
	* Ackonwledgement(ACKs) : receiver explicitly tells sender that packet has errors
	* Negative acknowledgements(NAKs): recerver explicitly tells sender that packet has errors
		Sender retransmits packet on receipt of NAK
	* rdt 2.0 has a fatal flaw
		* If ACK/NAK is corrupted, may cause retransmission of correctly received packet.
* rdt 2.1: rdt2.0 + Packet Seq.
	* To handle duplcates:
		* Sender retransmits current packet if ACK/NAK is garbled
		* Sender adds sequence number to each packet
		* Receiver discards duplicated packet
* rdt 2.2 : a NK-free Protocol
	* Samw assumption and functionality as rdt 2.1, but use ACKs only
	* Instead of sending NAK, receiver sends ACK for the last packet received OK
		* Now receiver must explicitly include seq. # of the packetbeing ACKed
	* Duplicate ACKs at sender results in same action as NAK; retransmit current pkt.
* rdt 3.0 Channel with errors and loss
	* Assumption: undrelying channel:
		* may flip bits in packets
		* may lose packets
		* may incur arbitrarily long packet delay
		* but won't reorder packets
	* To handle packet loss:
		* Sender waits "reasonable" amount of time for ACK
		* Sender retransmits if no ACK is received till timeout
# L4
* Performance of rdt 3.0:
	rdt 3.0 works, but performance stinks
* Pipelining: Increased Utilization:
	sender allows multiple, "in-flight" , yet-to-be-acknowledged packets
	* range of sequence numbers must be increased
	* buffering at sender and/or receiver

* Benchmark pipelined protocols
	* Tow generic forms of pipelined protocols:
		* Go-back-N (GBN)
		* Selective repeat (SR)
	* Assumption(same as rdt 3.0) : underlying channel
		* may flip bits in packets
		* may lose packets
		* may incur arbitrarily long packet delay
		* but wont reorder packets
* Go-Back-N
	GBN sender
	* can have up to N unACKed packets in pipeline
	* insert k-bits sequence number in packet header
	* use a "sliding window" to keep track of unACKed packets
	* keep a timer for the oldest unACKed packet
	* timeout(n) : retransmit packet n and all subsequent packets in the window
	GBN Receiver
	* Only ACK packets that arrive in order
	* discard out-of-order packets and ACK the last in-order seq.
* Selective Repeat:
	* Receiver individually acknowledges all correctly received packets
		Buffers out-of-order packets, as needed, for eventual in-order delivery to upper layer
	* Sender maintains timer for each unACKed packet
		When timer expires, retransmit only that unACKed packet

## TCP
* Point -to -point
* Connection-oriented
* Full duplex service
* Reliable, in-order byte system

* A TCP connection(socket) is identified by 4-tuple
	* srcIPAddr,srcPort,destIPAddr,destPort
	* Receiver uses all four values to direct a segment to the appropriate socket

* TCP send and receive buffers

* TCP Sequence Number
	"Byte number" of the first byte of data in a segment
	Initial seq # is randomly chosen
* TCP ACK Number
	TCP ACKs up to the first missing byte in the stream(cumulative ACK)
* TCP Timeout Value
	TCP computes(and keeps updating) timeout interval based on estimated RTT	
* TCP Fast Retransmit
* Before exchanging app data, TCP sender receiver "shake hands"