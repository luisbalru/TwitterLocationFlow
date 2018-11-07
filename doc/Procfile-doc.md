# Procfile DOC

As we can see, my Procfile's content is the following:

`web: gunicorn app:app`

Let's have a look on this sentences:

- Procfile starts with web due to the fact that TwitterLocationFlow is a web app. Besides, as I'm using Python, *gunicorn* is used as [WSGI](https://en.wikipedia.org/wiki/Web_Server_Gateway_Interface) characterised by having a simple Python configuration,  an automatic worker process management and being natively supportive of WSGI and web2py.   
- With *app:app* it is indicated where to find the main web app (which is in the root directory in this case).  