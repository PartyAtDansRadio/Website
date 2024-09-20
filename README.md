## To build the site using Docker, follow these steps:

1. Open a terminal or command prompt.
2. Navigate to the directory where your Dockerfile is located.
3. Run the following command to build the Docker image:
    ```
    docker build -t padplayer .
    ```
    This command will build the Docker image using the Dockerfile in the current directory and tag it as `padplayer`.
4. Once the image is built, you can run the container using the following command:
    ```
    docker run -p 8000:8000 -v $(pwd):/usr/src/padplayer padplayer
    ```
    This command will start the container and map port 8000 on your local machine.
    It wil mount the host folder allowing you to make live changes as needed.

* Make sure you have Docker installed and running on your machine before executing these commands.

