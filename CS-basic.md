# System Design (Frontend to Backend):

## Front-Back-End website response system

DNS: Domain Name System is a phonebook to look up IP address depending on the domain names.

CDN: Content Delivery Network refers to a group of servers distributed in different cities which work together to provide fast delivery of Internet content, like images, videos and webpages. Like a cache system for data center. CDN has very fast data path like optical fiber between them. Protect from DDOS attack.

Load Balancer: can efficiently distribute incoming network traffic across a group of backend servers.





<img src="https://s2.loli.net/2022/04/03/l3kBbau8r9e6y4O.png" alt="image-20220331224749074" style="zoom:40%;" />

**Description**: Of course. After users give a url to the browser, the browser will first use recursive lookup to check the cache of browser and the cache of computer. If it didn't find the corresponding content, it will then delivery this url to the DNS translating domain name to IP address. After that, the request command will first go into CDN, which like a cache system for data center. If the request command can find the internet content, it will return the result from this step. If not, this request will further pass to the data center. In data center, the request will first pass to load balancer, which can efficiently distribute incoming network traffic across a group of backend servers, then the backend services will connect to the content storage and return the target by hash code. Finally, the content of request will pass back to the users' browser.



## API test platform system

### Real-Time Application Monitor

Propose: collect & refine Logfile to analysis and make the visualization in dashboard

ELK Stack: A stack that comprises of several popular projects 

- **Beats**: is a family of lightweight data shippers
- **Kafka**: is a distributed system which allow to capture data in real-time from event sources like databases, mobile devices, cloud services, and software applications in the form of streams of events.
- **Logstash** acts as a data aggregation and transformation agent
- **Elasticsearch** provides the time series data storage and data indexing engine
- **Kibana** helps you analysis and visualize the data that you have

#### Pipeline:

<img src="https://s2.loli.net/2022/04/03/CWQZkLiNHqb6guV.png" alt="image-20220401153143693" style="zoom:50%;" />

The ELK stack is popular because it fulfills a need in the log management and analytics space. In cloud-based environments, performance isolation is extremely difficult to reach, like infrastructure servers and some micro-servers in the cloud. However, ELK can help with such infrastructure problems and different operating system log files.



### Real-Time Application Monitoring & Alerting System

**Pipeline**:

<img src="https://s2.loli.net/2022/04/03/hSL32lemdB4a1VE.png" alt="image-20220402102722640" style="zoom:50%;" />

**Kubernetes**:

**Prometheus**: is a monitoring and alerting toolkit

**Grafana**: is a metrics visualization system



## Fronted-System

HTML: HyperText Markup Language
HTML like a framework to structure data

CSS: Cascading Style Sheet

JS: JavaScript
Allow to have interaction with users and functional programming, like search bar

DOM: Document Object Model



## Concepts:

1. The difference of SQL and NoSQL:

   **SQL databases** means relational databases which support ACID guarantees. SQL databases tend to have rigid, complex, tabular schemas and typically require expensive vertical scaling.
   **ACID Guarantees: Atomicity, Consistency, Isolation, Durability**

   **NoSQL databases** means non-relational databases which don't have rigid schemas and focus on scaling, fast queries, allowing for frequent application changes, like JSON format.
   **CAP theorem: Consistency, Availability and Partition Tolerance, MongoDB only support CP**
   Use master-slave architecture, support sharding or partitioning.

   

2. The difference of HTTP and HTTPS:

   **HTTPS** is HTTP with encryption. The only difference between the two protocols is that HTTPS uses TLS  to encrypt normal HTTP requests and responses. As a result, HTTPS is far more secure than HTTP.

   **TLS**: Transport Layer Security

   TLS is a widely adopted security protocol designed to facilitate privacy and data security for communications over the Internet. A primary use case of TLS is encrypting the communication between web applications and servers, such as web browsers loading a website.
   <img src="https://s2.loli.net/2022/04/03/BQl12fVhxMIYbDG.png" alt="image-20220402135657031" style="zoom:50%;" />

   

3. TCP  and UDP:

   TCP: Transmission Control Protocol
   TCP has built-in systems to check for errors and to guarantee data will be delivered in the order it was sent, making it the perfect protocol for transferring information like emails, data files, and web pages.

   UDP: User Datagram Protocol 
   UDP is a simpler, connectionless Internet protocol which error-checking and recovery services are not required. There is no overhead for opening a connection, maintaining a connection, or terminating a connection. Data is continuously sent to the recipient, whether or not they receive it. Used in virtual meeting and video meeting.

   1. TCP is a connection-oriented protocol, whereas UDP is a connectionless protocol.
   2. A key difference between TCP and UDP is speed, TCP is slower than UDP.
   3. TCP provides an ordered delivery of data from user to server, whereas UDP is not. 

   

4. The structure of OSI and TCP/IP:

   | OSI          | TCP/IP         | Protocol                     |
   | ------------ | -------------- | ---------------------------- |
   | Application  | Application    | HTTP FTP SMTP                |
   | Presentation |                | POP3 NFS SSH                 |
   | Session      |                |                              |
   | Transport    | Transport      | TCP UDP                      |
   | Network      | Internet       | IP ICMP                      |
   | Data Link    | Network Access | LAN: Ethernet, tokening, ARP |
   | Physical     |                | WAN: ISDN, ATM               |

5. TCP communication process:
   Three-way Handshake:

   <img src="https://s2.loli.net/2022/04/03/jraoq82nGlSBeXI.png" alt="image-20220402141102467" style="zoom:50%;" />

   **Step 1**: Acknowledged the ability of send from client
   First, we need to establish a connection between server and client, so the client node sends a **SYN** (Synchronize Sequence Number) data packet over an IP network to a server. The objective of this packet is to ask if the server is open for new connections.

   **Step 2**: Acknowledged the ability of receive and send from server (server is live)
   When the server receives the SYN packet from the client node, it responds and returns a confirmation message – the SYN/ACK packet. This packet includes two sequence numbers.

   The first one is ACK (Acknowledgement Sequence Number) which is set by the server to one more than the sequence number it received from the client.

   The second one is the SYN sent by the server, which is another random sequence number.

   This sequence indicates that the server correctly acknowledged the client’s packet, and that is sending its own to be acknowledged as well.

   **Step 3**: Acknowledged the ability of receive from client (client is live)

   The client node receives the SYN/ACK from the server and responds with an ACK packet which is set by the client to one more than the sequence number it received from the server.

   All these steps are necessary to verify the stability of the connection.

   

   Four-Way Wavehand: (Can be Three-Way Wavehand)
   <img src="https://s2.loli.net/2022/04/03/w4Zap5rjBkKAJST.png" alt="image-20220402143630748" style="zoom:50%;" />

   **Step 1**:
   Client node sends a **FIN** data packet to the server which indicates the data sending process is finished.

   **Step 2**:
   Sever sends a **ACK** data packet to the client which indicates server has received the **FIN** avoiding server received duplicated messages.

   **Step 3**:
   Sever sends a **FIN** data packet to the client which indicates server finished the data received and will not send data anymore.

   **Step 4**:
   Client sends a **ACK** data packet to the server which indicates received the **FIN** and server can close the connection. Client wait for 2MSL time and closed.

   

6. IP Address
   Net_ID(Domain) + Host_ID

   

7. Microservers:

   Pros: These microservers can be used by other different applications (more general)

   Cons: Hard to debug to find the problems

   

8. API type:

   **Open APIs**: are available to developers and other users with minimal restrictions.

   **Internal APIs**: They are used within a company to share resources and hidden from external users. They allow different teams or sections of a business to consume each other’s tools, data and programs.

   **Partner APIs**: feature restricted access, often controlled through a third-party API gateway.

   **Composite APIs**: Composite APIs allow developers to access several endpoints in one call. These could be different endpoints of a single API, or they could be multiple services or data sources. 

   

9. API Structure

   **REST** (representational state transfer) is a very popular web API architecture. To be a REST API, an API must adhere to certain architectural constraints:

   * **Client-server architecture**: the interface is separated from the backend and data storage to make it be more flexibility.
   * **Statelessness**: no client context is stored on the server between requests.
   * **Cacheability**: clients can cache responses, so a REST API response must explicitly state whether it can be cached or not.
   * **Layered system**: the API will work whether it is communicating directly with a server, or through an intermediary such as a load balancer.

   **RPC** is a remote procedural call protocol, like XML-RPC uses XML to encode its calls, while JSON-RPC uses JSON for the encoding.

   **SOAP** (simple object access protocol) is an established web API protocol.

   
   

10. United test and Integrated test

    Unit testing is to evaluate individual pieces of code in isolation to ensure they operate correctly. This type of testing focuses on a single component and only considers whether a unit functions correctly on its own.

    Integration testing evaluates the overall functionality of an application. I means whether various units of code work together correctly. Integration testing usually occurs after unit testing and before system testing.

    Difference: Scope, External dependencies

    

11. Deadlock Bugs:
    Four conditions for deadlock to occur:

    * Mutual Exclusion
    * Hold and wait
    * No preemption (Resource can't be released while holding)
    * Circular Wait

    Prevention (make any of the condition doesn't hold):

    * Provide a total ordering on lock acquisition - Circular Wait
    * Using lock-free data structure - Mutual Exclusion

12. HTTP Response Code

    * 100 - 199: informational responses: stop resend of INVITE requests.
    * 200 - 299: successful responses
    * 300 - 399: redirection responses
    * 400 - 499: client error responses
    * 500 - 599: server error responses

13. HTTP Request

    * POST: Create a new resource
    * GET: Read a resource
    * PUT: Update an existing resource
    * DELETE: Delete a resource

14. Real-time Live-stream Testing & Metric

    

15. Abstract class and interface (OOP)

    

16. Override and Overload (OOP)

    

17. Quicksort / Quickselect / heap

    

18. Project

    



# Data Structure & Algorithm

## Steps of coding part:

1. Write down & speak out your solution step by step, confirm them with your recruiter.
2. Compute the time and space complexity
3. Write down your code step by step



## Critical Question :

1. Data structure class implementation (priority-queue, heap)
2. Tree, BFS, DFS
3. Quicksort
4. OA questions
5. No DP









