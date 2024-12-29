STEPS FOLLOWED IN THIS COURSE
CHAPTER 1
1) docker pull nginx ---> Pull latest nginx image
2) docker run -it -d --rm -p 8080:80 --name=website nginx
        ---> it stands for interactive, -d for detached mode --rm will remove existing containers browser port is 8080 and nginx port will be 80 and the name of the container is website and the image name is nginx.
3) docker exec -it website bash ---> To access the terminal of the container.
4) Few Commands
        nginx -v ---> Version
        nginx -V ---> Version with more details
        nginx -t ---> Configuration
        nginx -T ---> Config with more detail
        nginx -h ---> Will open help menu
        service nginx start ---> Start the nginx webserver
        service nginx stop  ---> Stop the nginx webserver, this will also stop the container.
5) After creating Dockerfile and docker-compose.yaml 
        docker-compose up  ---> Will create a image and start the container based on the dockerfile and yaml file.

        docker-compose down ---> Will stop the started container
        docker build -t webserver . ---> Will build a image with the name webserver with the current    config.
        
    
Chapter 2

1) docker top website ---> To view the running process in a container. Nginx has a master process and 4 worker process.

2) ps -C nginx -f  ----> With external library procps we can see it more clearly, the master and worker processes.

3) nginx -s reload ----> To reload the nginx (master process) based on the configuration. -s stand for signal.