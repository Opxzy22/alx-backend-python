<h1><u>0x01. Python - Async</u><h1>
<h2>NOTES</h2>
<b><u>CONCURRENCY</u><b> <br>
    its says that tasks have the ability to run in an overlapping manner
    <br>
<b><u>THREADING</u></b> <br>
    is a concurrency model where tasks take s turn to execute
    one process can contain multiple threads
    <br>
<b><u>ASYNC IO</u></b><br>
    is  a single threaded single process design
    it uses cooperative multitasking
<br>
 <b><u>ASYNCHRONOUS</u></b> <br>
    * routines areable to pause while waiting on their ultimate result and let the other routines run in the meantime
    * it facilitates concurrent execution
    <hr>

   <caption>CONCEPTS AND IMPLEMENTATION </caption>
   <table>
    <tr>
        <td> CONCEPT</td>
        <td> IMPLEMENTATION </td>
    </tr>
    <tr>
        <td> CONCURRENCY </td>
        <td> Theading, Async IO </td>
    </tr>
    <tr>
        <td> PARALLELISM </td>
        <td> Multiprocessing </td>
    <tr> 
</table> 
<hr>

### ASYNC IO
it is built under concpet like
    <li> CALLBACKS
    <li> EVENTS 
    <li> TRANSPORT
    <li> PROTOCOLS and fetaures

<li>Is about comminucation with other task to make sure they take tuens to execute and each run after the other 
<li> Fuction wait for each other and run in their order of execution 
<li> A good function is supposed to block any function from running on its optimal time
<li> It only let other functions run after it has finiched runing and is in waiting mode

### The asyncio Package and async/await
 <h3> SYNTAX </h3>

### COROUTINES
 <li> A coroutine is a specialized version of a Python generator function
 <li> it is a function that can suspend its execution before reaching return
 <li> it can indirectly pass control to another coroutine for some time

 ### RULES OF ASYNC IO
 <i>def</i> introduces either a native coroutine or an asynchronous generator <br>
 <i>await</i> pass control back to the even loop
 it suspends the execution until its waiting for the next function

 <li> using <i>await &| return </i> creates a coroutine function
 <li> to call the coroutine function you <i>await</i> it to get its results
 <li> you can use yield in def block and this will create asynchronous generator that you iterate with <i>sync for</i>
 </li>
 it is a Syntax error to use<i>await</i> outside an <i>async</i> def coroutine and to use <i>yield</i> outside of a def function
 
