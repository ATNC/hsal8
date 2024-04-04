# Project Title

## Introduction

This Docker Compose project orchestrates a web application and an OpenResty server to serve as a reverse proxy and static file server. The configuration facilitates development and deployment processes by encapsulating service dependencies.

## Prerequisites

- Docker
- Docker Compose

Please ensure Docker and Docker Compose are correctly installed on your system.

## Services Overview

### Web Service

- **Image Build Context**: `./app` directory
- **Port**: Internal service port `8000` is mapped to the host's port `8000`.
- **Volumes**: Binds the host's `./app/static` directory to the container's `/app/static` for static file serving.

### OpenResty Service

- **Image Build Context**: `./nginx` directory
- **Port**: Internal service port `80` is mapped to the host's port `80`.
- **Volumes**:
  - Binds the host's `./nginx/nginx.conf` file to the container's `/usr/local/openresty/nginx/conf/nginx.conf` in read-only mode.
  - Shares the `./app/static` directory with the container's `/app/static` in read-only mode for static file serving.
- **Depends On**: Ensures the `web` service is started before the `openresty` service.

## Getting Started

To run the application, execute the following command in the terminal within the project directory:

```
docker-compose up -d
```

This command builds the necessary images (if they are not already built) and starts the containers in detached mode.

To stop and remove the containers, networks, and volumes associated with the application, use:

```
docker-compose down
```

## Additional Notes

- Customize the Nginx configuration as needed by editing the `./nginx/nginx.conf` file.
- Place your application's static files in the `./app/static` directory to ensure they are served correctly by both the `web` and `openresty` services.

