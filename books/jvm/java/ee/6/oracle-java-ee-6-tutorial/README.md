# Part I Introduction
## Chapter 1: Overview
### [Java EE 6 Platform Highlight](https://docs.oracle.com/javaee/6/tutorial/doc/giqvh.html)
*Web profile* is the sub-set of *full profile*. The web profile defines the scope of Java EE technologies for some light-weight web server to support.

**NOTE! Different Java EE version have different web profile**

# Part IV Enterprise Beans
## Chapter 24: Running the Enterprise Bean Examples
### A *Singleton* Session Bean Example: Counter

Exam Question Source : https://www.examtopics.com/exams/oracle/1z0-900/view/14/

### Using the Timer Service
**My own summary on `TimerService`**
 
EJB version | Java EE version | method
------------|-----------------|--------------
EJB 2.1 ?   | 1.4             | `createTimer`
EJB 2.1 ?   | 1.4             | `getTimers` 
EJB 3.1     | 6               | `createCalendarTimer`
EJB 3.1     | 6               | `createIntervalTimer`
EJB 3.1     | 6               | `createSingleActionTimer(Date expiration, TimerConfig timerConfig)`
EJB 3.1     | 6               | `createSingleActionTimer(long duration, TimerConfig timerConfig)`

Exam Question Source :
