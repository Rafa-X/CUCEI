# Report - Mastering Chaos, A Netflix Guide to Microservices
## Begins of Netflix and its monolithic architecture

<p align="center" style="margin-bottom: 0px !important;">
  <img width=50% src="images/monolitic_architecture.png" align="center">
</p>

In the 2000’s, with the beginning of Netflix they opted to make the whole system of its company with the monolithic architecture. With everybody contributing to one single codebase there was plenty of difficulties, between them was the difficult to diagnose errors caused when a change was introduced, troubleshooting that taking pieces of code, running isolated tests and more took extended periods of time and a big team. <br>

Their database was also monolithic, one single hardware, running one big Oracle database. The main problem: when this went down, all the business went down. Also, as demand increases, more and bigger hardware were needed to afford with their demand, so regardless of options they seem obligated to vertically scales its resources. <br>

This is a good example of **how not** to build a services-based company today. <br>

## What are microservices ?
```The microservice architecture style is an approach to developing a single application as a suit of small services, each running in its own process and communicating with lightweight mechanisms, often an HTTP resource API.  -Martin Fowler``` <br>

Resiliency, isolation and scalability are some of the requirements intended for the new kind of application architectures. With this in mind a group of software architects created the term “microservices” in 2012, but didn’t became well known until Martin Fowler, software developer and known author of the community, started using the term in some of his web page publications. <br>

The services are built according to the capabilities of the business and are deployed independently by a fully automated deployment mechanism. There is minimal centralized management of these services, which may be written in different programming languages and use different data storage technologies. <br>

There were several critical things that encourages the software architects to create the microservices style there are:
-	Separation of concerns: Modularity and encapsulation. Being capable to isolate data structures behind something that deals with all the components coordination. 
-	Scalability: Horizontal scaling and workload partitioning. Increasing application capacity by adding machines to the system and then to balance the workload, as a distributed system, break the work in to smaller components so it can be more manageable.   
-	Virtualization and elasticity: Microservices are way to easier to manage in this kind of virtualized environment, because there is needed to automate operations as well the on-demand provisioning.

## Microservices and abstraction
Microservices are essentially an abstraction. From a simple point of view this kind of system may look like a horizontal scaled microservice, but it's not that simple. Database, stored data, service client, client cache all of it are a bunch of machines working together responding to the client’s application in which are embedded. 

<p align="center" style="margin-bottom: 0px !important;">
  <img width=45% src="images/microservice_abstraction.png" align="center">
</p>

Its important to realize that this set of technologies is a microservice, not this simple stateless thing which is nice from a user perspective, but it actually has these sorts of complex structures. 

## Cascading failure and Histrix
This disaster scenario in which one service fails and make others to fail too. Improper defenses cause a service to fail and scale to a cascade failure which can ends taking down the entire service. One single service may not affect severely the others, but actually increases the probability that the others components does, the more components fail, the greater the probability of a service failure.

To deal with this Netflix created Hystrix, a library designed to control the interactions between these distributed services, it was created and evolved out of the need for resiliency, greater tolerance of latency and failure. It does this by isolating points of access between the services, stopping cascading failures across them, and providing fallback options, all of which improve the system’s overall resiliency.

<p align="center" style="margin-bottom: 0px !important;">
  <img width=45% src="images/hystrix_flow_chart.png" align="center">
</p>

## Critical services
Microservices have two types of importance in services: normal services and critical services. The first ones are all that give added value to the service but are not essential, this is the main difference with the seconds, these are necessary to have the basic functionality work.

<p align="center" style="margin-bottom: 0px !important;">
  <img width=30% src="images/critical_micro.png" align="center">
</p>

## Network Partition
In the presence of a network partition, must be choose between consistency and availability. What if a connection to some component can’t be reached, its better to just let it fail and give back an error, or connect to the ones can be reached and then fix it up backwards.

Netflix choose the latter and solve this by using the NoSQL distributed database Cassandra, embracing the concept of “Eventual Consistency”, which means the ensuring that the updates made to distributed NoSQL databases will eventually be reflected across all nodes.

<p align="center" style="margin-bottom: 0px !important;">
  <img width=35% src="images/eventual_consistency.png" align="center">
</p>

