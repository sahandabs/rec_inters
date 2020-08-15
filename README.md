# rec_inters
# Rectangles intersection:<br/>
This project is an HTTP server that receives a main rectangle and some input rectangles and then stores input rectangles that have intersect with the main one.<br/>
You can edit hostname and port number of this server  at **server/main.py**.<br/>
The default database is **MySQL** and you can create required tables by importing **my.sql** to your mysql server.<br/>
You can edit database variables at **helper/dbhelper.py**.<br/>
The required packages are available at **requirements.txt**.<br/>
You can run the server by executing **runserver.sh**.<br/>
You can test the server by posting some sample JSON input and see the output in the terminal by running **test.sh**.<br/>
You can see the outputs by visiting **localhost:8080** in your browser.<br/>
![SC Shot](https://github.com/sahandabs/rec_inters/blob/master/sc.jpeg)
