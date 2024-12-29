1) Webserver functionalities
    Web Serving
    Reverse Proxying
    Cahcing
    Load Balancing
    Media Streaming

2) Browser  --- Nginx ---  uWSGI --- Django/React App

3) Nginx has master and worker process (default = 4), master process takes care of startup/shutdown, maintainance, Read/Evaluate configuration, Main worker processes. 
   The Worker process process request. Default 512 max number of connection.
    
   We can set the total number of workers in the nginx.conf file default it is auto, which will create workers based on the number of cpu cores in the system