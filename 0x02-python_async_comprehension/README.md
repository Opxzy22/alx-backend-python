<!DOCTYPE html>
<html lang="en">
    <head>
    </head>
    <body> 
       <h1 class="gap">0x02. Python - Async Comprehension</h1>
      <div id="project_id" style="display: none" data-project-id="1231"></div>
      <div class="panel-body">
        <p><img src="https://s3.amazonaws.com/alx-intranet.hbtn.io/uploads/medias/2019/12/ee85b9f67c384e29525b.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOUSBVO6H7D%2F20240125%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20240125T171647Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=bb4226acf12148165db5ce5be0386548518d441090e7fd158755691d29dd8268" alt="" loading='lazy' style="" /></p>
        <h2>Resources</h2>
        <p><strong>Read or watch</strong>:</p>
    <ul>
<li><a href="/rltoken/hlwtED-iLsdORSgly8DsyQ" title="PEP 530 -- Asynchronous Comprehensions" target="_blank">PEP 530 &ndash; Asynchronous Comprehensions</a></li>
<li><a href="/rltoken/0OkbObYzCKtO7ZUAxfKvkw" title="What’s New in Python: Asynchronous Comprehensions / Generators" target="_blank">What’s New in Python: Asynchronous Comprehensions / Generators</a></li>
<li><a href="/rltoken/l4Fnno568VbVIn9GvrFVtQ" title="Type-hints for generators" target="_blank">Type-hints for generators</a></li>
</ul>

<h2>Learning Objectives</h2>

<p>KNOWLEDGE CHECK</p>

<ul>
<li>How to write an asynchronous generator</li>
<li>How to use async comprehensions</li>
<li>How to type-annotate generators</li>
</ul>

<h2>Requirements</h2>

<h3>General</h3>

<ul>
    <li>Allowed editors: <code>vi</code>, <code>vim</code>, <code>emacs</code></li>
    <li>All your files will be interpreted/compiled on Ubuntu 18.04 LTS using <code>python3</code> (version 3.7)</li>
    <li>All your files should end with a new line</li>
    <li>The first line of all your files should be exactly <code>#!/usr/bin/env python3</code></li>
    <li>A <code>README.md</code> file, at the root of the folder of the project, is mandatory</li>
    <li>Your code should use the <code>pycodestyle</code> style (version 2.5.x)</li>
    <li>The length of your files will be tested using <code>wc</code></li>
    <li>All your modules should have a documentation (<code>python3 -c &#39;print(__import__(&quot;my_module&quot;).__doc__)&#39;</code>)</li>
    <li>All your functions should have a documentation (<code>python3 -c &#39;print(__import__(&quot;my_module&quot;).my_function.__doc__)&#39;</code></li>
    <li>A documentation is not a simple word, it&rsquo;s a real sentence explaining what&rsquo;s the purpose of the module, class or method (the length of it will be verified)</li>
    <li>All your functions and coroutines must be type-annotated.</li>
</ul>
<h2 class="gap">TASKS</h2>
     <div data-role="task11630" data-position="1" id="task-num-0">
      <div class="panel panel-default task-card " id="task-11630">
        <span id="user_id" data-id="251885"></span>
    </div>
    </div>

  <div class="panel-heading panel-heading-actions">
    <h3 class="panel-title">
      0. Async Generator
    </h3>
    <div>
        <span class="label label-info">
          mandatory
        </span>
    </div>
  </div>
  </div>
  </div>
  <p>Write a coroutine called <code>async_generator</code> that takes no arguments. </p>
<p>The coroutine will loop 10 times, each time asynchronously wait 1 second, then yield a random number between 0 and 10. Use the <code>asyncio.sleep</code> function to do this.</p>
        <div class="modal-body">
        
  <div class="panel-heading panel-heading-actions">
    <h3 class="panel-title">
      1. Async Comprehensions
    </h3>
     <div>
        <span class="label label-info">
          mandatory
        </span>
    </div>
  </div>
  <p>Import <code>async_generator</code> from the previous task and then write a coroutine called <code>async_comprehension</code> that takes no arguments. </p>

<p>The coroutine will collect 10 random numbers using an async comprehensing over <code>async_generator</code>, then return the 10 random numbers.</p>
<h3 class="panel-title">
    2. Run time for four parallel comprehensions
</h3>
   <div>
        <span class="label label-info">
          mandatory
        </span>
    </div>
  </div>
    <!-- Task Body -->
    <p>Import <code>async_comprehension</code> from the previous file and write a <code>measure_runtime</code> coroutine that will execute <code>async_comprehension</code> four times in parallel using <code>asyncio.gather</code>.</p>

<p><code>measure_runtime</code> should measure the total runtime and return it.</p>

<p>Notice that the total runtime is roughly 10 seconds, explain it to yourself.</p>

<h2>NOTES</h2>
<h3>ASYNCHRONOUS COMPREHENSIONS PEP 530</h3>
<li>Async comprehensions are a new feature of Python 3.6.</li>

 ## ABSTRACT
  <li>The async comprehensions feature allows us to write asynchronous code that looks like synchronous code. </p>
  <li>introduced support for native coroutines and asynchronous generators using <code>async</code> / <code> await</code> syntax.
  <li>It allows to add asynchronous versions of list, set, dict comprehensions and generator expressions.
  </li>
<li>

## RETIONALE AND GOALS
allow production of lists, dict and sets with a simple and conscise syantax
<li>produsing a similar syntactic constructions for the asynchronous code</li>
EXAMPLE
<pre> 
result =[]
async or i in aiter():
  if i % 2:
    result.append(i)
</pre>
with the proposed <code>asynchronous comprehension syntax</code> it can be written as <br> <pre> result = [i async for i in aite() if i % 2] </pre>
It can be written using <code> await</code> expression as follows: <pre> result = [await func() for fun in funcs] </pre>

## SPECIFICATION
## Asynchronous Comprehension
Allow using of <code> async for </code> inside <li>lists</li> <li>sets</li> <li>dict</li> comprehensions
EXAMPLE OF CREATION OF <code> Asynchronous GENERATOR EXPRESSIONS </code>
<li> set comprehension: <code> {i async for i agen()};</code>
<li> list comprehension: <code> [i async for i in agen()]; </code>
<li> dict comprehension: <code>{i: i ** 2 async for i in agen()}; </code>
<li> generator expression: <code>(i ** 2 async for i in agen())</code> <br>
<br>
<code> async for </code> can be used along with <code> if </code> and <code> for<code> clauses in <code> asynchronous comprehensions </code> and <code>generator expressions :</code>
<pre>
dataset = {data for line in aiter()
                ansyc for data in line
                if check(data)}
</pre>
asynchronous comprehensions are allowed only inside an <code>async def </code> function

## <code>await</code> in Compehensions
this is allows using <code> await </code> in asynchronous and synchronous compehension. <br>
EXAMPLE
<pre>
<u># only valid in <code> async def </code> fucntion body </u>
<br>

result = [await fun() for fun in funcs]
result = {await fun() for fun in funcs}
result = {fun: await fun() for fun in funcs}

result = [await fun() for fun in funcs if await smth]
result = {await fun() for fun in funcs if await smth}
result = {fun: await fun() for fun in funcs if await smth}

result = [await fun() async for fun in funcs]
result = {await fun() async for fun in funcs}
result = {fun: await fun() async for fun in funcs}

result = [await fun() async for fun in funcs if await smth]
result = {await fun() async for fun in funcs if await smth}
result = {fun: await fun() async for fun in funcs if await smth}
</pre>
## GRAMMAR UPDATES
<code> async for </code> can be used along with <code> if </code> and <code> for<code> clauses in <code> asynchronous comprehensions </code> and <code>generator expressions :</code><br>

It requiresone change on the grammarlevel: eg is addingthe optional<code>async</code> keyword to the <code>comp_for</code> clause.
EXAMPLE
<pre> comp_for: [ASYNC] 'for' exprlist 'in' or_test [comp_iter]
</pre>
the comprehension AST node will have the new <code>is_async</code> argument
## BACKWARDS COMPATIBILITY
the proposal is fully backwards compatible
</body>
</html>
