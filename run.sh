#!/bin/bash

# Remove dangling images
docker image prune -f

# Build the Docker image
docker build -t padplayer .

# Run the Docker container with volume mount in detached mode
docker run -d -p 8000:8000 -v $(pwd):/usr/src/padplayer --name padplayer_container padplayer