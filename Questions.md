Questions to answer
==================================

These are the questions related to the M/M/1 queueing model using SimPy.

You will need to answer the questions in this file. Your answers will be graded. 

You can answer in English or French.


1-Implement the M/M/1 queueing model in SimPy
---------------------------------------------

### The implementation in the file `models/simpy_m_m_1.py` counts for 4 points maximum. (4p)


2-Validate the simulation model
-------------------------------

#### Show at least 3 different simulation results with different parameters and compare them with the analytical model. (6p)

As we've seen in the course, we can calculate the `mean response time` and the `mean number of clients` with the 
following equations:  
##### Mean Response Time
$\frac {1}{\mu - \lambda}$
##### Mean Number of Clients in the System (per second)
$\frac {\frac {\lambda} {\mu}} {1 - \frac {\lambda} {\mu}}$

- With Default values:  
Expected values:  
$\frac {1} {50 - 10}s = \frac {1} {40}s$  
$\frac {\frac {10} {50}} {1 - \frac {10} {50}} = \frac {\frac {1} {5}} {1 - \frac {1} {5}} = \frac {1} {4}$
```
# Actual output
Mean response time: 0.2759 seconds
Mean number of clients in the system: 2.8057
```
- With Arrival Rate = 50  
Expected value:  
$\frac {1} {50 - 50} = \frac {1} {0}$ => tends to infinity  
$\frac {\frac {50} {50}} {1 - \frac {50} {50}} = \frac {\frac {1} {1}} {1 - \frac {1} {1}} = \frac {1} {0}$ => tends to infinity

What we need to understand with this one is that we will have a growing number of people and waiting time as long as 
the service is running with no possibility to come back to a stable state.
```
# Actual output
Mean response time: 57.6865 seconds
Mean number of clients in the system: 2861.2594
```
- With Service Rate = 20  
$\frac {1} {20 - 10}s = \frac {1} {10}s$  
$\frac {\frac {10} {20}} {1 - \frac {10} {20}} = \frac {\frac {1} {2}} {1 - \frac {1} {2}} = 1$

```
# Actual output
Mean response time: 0.9931 seconds
Mean number of clients in the system: 9.9151
```

3-Evaluate the impact of an load increase
-----------------------------------------

#### What are the simulation results when running with `ARRIVAL_RATE = 30/s` and `SERVICE_RATE = 50/s`? (2p)

```
Mean response time: 1.4264 seconds
Mean number of clients in the system: 42.7753
```

#### What are the simulation results when running with a 40% increased `ARRIVAL_RATE`? (2p)
If the 40% increased is to be done on the `30/s arrival rate` of the previous question, here are the result for a 
`42/s arrival rate`.  
```
Mean response time: 5.2184 seconds
Mean number of clients in the system: 221.6942
```

#### Interpret and explain the results. (3p)

With an `arrival rate` of 42/s, we are running our service at 84% which is a point at which we can see the quality 
of our service degrading fast (as seen in the course). Which explains the almost tripling time and clients 
in the system compared to before as it follows an exponential curve. 


4-Doubling the arrival rate
---------------------------

#### What are the simulation results when running with `ARRIVAL_RATE = 40/s` and `SERVICE_RATE = 50/s`? What is the utilization of the server? (2p)

```
Mean response time: 4.1403 seconds
Mean number of clients in the system: 165.9753
```

80%

#### What is the value of `SERVICE_RATE` that achieves the same mean response time when doubling the `ARRIVAL_RATE` to `80/s`? What is the server utilization in that case? (2p)

The `service rate` is at `100.0` to achieve the same `Mean response time`.  
$\frac {80} {100} = 80\%$

#### Use the analytical M/M/1 model to confirm your findings. (3p)

With the following equations:
##### Mean Response Time
$\frac {1}{100 - 80}s = \frac {1} {20}s = 0,05\ s = 50\ ms$
##### Mean Number of Clients in the System (per second)
$\frac {\frac {80} {100}} {1 - \frac {80} {100}} = \frac {0,8} {0,2} = 4$

#### Describe and interpret the results. (3p)

The results do not align with the mathematical results. Those deltas could be due to the computer running other 
programs or not having enough resources to handle the workload required to match the mathematical results.


5-Rule of Bertsekas and Gallager
--------------------------------

#### Describe your experiments and results. (2p)

As we can see, by augmenting the `service rate`, to match the `response time` between `40/s` and `80/s` `arrival 
rate`, we can treat more requests (client in the system) without impacting the quality of the service.  
We do need to provide not only a faster line (`arrival rate`) but also a more performant server (`service_rate`) to 
handle that increase otherwise the last part of the rule *"avec un délai moyen par paquet k fois plus petit"* could 
not remain true.

#### Provide an analytical explanation of your findings. (2p)

See explanation above and the maths of the previous point.


Conclusion
----------

#### Document your conclusions here. What did you learn in this lab? (2p)

I learned how to simulate a queue through simPy to simulate and "test out" an application for it's needs.  
Through the lab I can now clearly see how impactful is the augmentation of *ARRIVAL_RATE* whereas the augmentation 
of *SERVICE_RATE* can be less demanding to get back to a *QoL* equivalent of what was used prior to the 
*ARRIVAL_RATE* surge.
