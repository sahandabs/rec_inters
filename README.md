# rec_inters
Rectangles intersection
This project is an HTTP server that receives a main rectangle and some input rectangles and then stores input rectangles that have intersect with the main one.
You can edit hostname and port number of this server  at server/main.py
The default database is MySQL and you can create required tables by importing my.sql to your server.
You can edit database variables at helper/dbhelper.py.
The required packages are available at requirements.txt.
You can run the server by executing runserver.sh.
You can test the server by posting some sample JSON input and see the output in the terminal.
You can see the outputs by visiting localhost:8080 in your browser.
