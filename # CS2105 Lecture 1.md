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