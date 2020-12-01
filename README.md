# Python-Projects
_This repo use to be my private hacking repository for Personal Python Hacking Projects and Scripts_
_I have now made it public for those who which to make use of some of the scripts_
_I cannot be held liable for any use of these scripts for malicious purposes, they should be strictly used for educational purposes!_

![Python Powered Scripts](https://www.python.org/static/community_logos/python-powered-w-200x80.png)


## Markdown Resources and Examples
:panda_face:

* [Emoji cheatsheet](https://www.webfx.com/tools/emoji-cheat-sheet/)
* [Mastering Markdown Github Guide](https://guides.github.com/features/mastering-markdown/)
* [Markdown Cheatsheet](https://www.markdownguide.org/cheat-sheet/)


**Bold**

*Beautiful*

**Bold and _Beautiful_**

Test plain text

**HTML Tags also seem to work in markdown**

*Image below ise inserted and formated with HTML img tag*

 <img src="Images\rick-sanchez.png" alt="Rick Sanchez" height="200"/>

This line is inspired by Rick Sanchez:
> To life is to risk it all, otherwise you are an inherent chuck of particles drifting wherver the universe takes you.

### Code Block Example
*Syntax highliting can be achieved by putting the programming language name beind the 3 ```*


```python
import socket

print "System Initializing"
print "Establashing server"
print "Hello World"


def make_server(address, port):
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((address, port))
    server.listen(5)


make_server("localhost", 1337)
print "We are listing"

````

```
No language indicated, so no syntax highlighting in Markdown Here (varies on Github). 
But let's throw in a <b>tag</b>.
```

## Tables

> There must be at least 3 dashes separating each header cell.
> The outer pipes (|) are optional, and you don't need to make the 
> raw Markdown line up prettily. You can also use inline Markdown.


Markdown | Table | Pretty
--- | --- | ---
*Still* | `renders` | **nicely**
1 | 2 | 3
