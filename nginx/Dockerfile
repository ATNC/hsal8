# Use a base image with essential build tools
FROM debian:buster as builder

# Set environment variables for versions
ENV OPENRESTY_VERSION 1.19.9.1
ENV NGX_CACHE_PURGE_VERSION 2.3

# Install dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    libpcre3-dev \
    libssl-dev \
    perl \
    wget \
    zlib1g-dev

# Download OpenResty and ngx_cache_purge
RUN wget https://openresty.org/download/openresty-${OPENRESTY_VERSION}.tar.gz && \
    tar -xzvf openresty-${OPENRESTY_VERSION}.tar.gz && \
    wget http://labs.frickle.com/files/ngx_cache_purge-${NGX_CACHE_PURGE_VERSION}.tar.gz && \
    tar -xzvf ngx_cache_purge-${NGX_CACHE_PURGE_VERSION}.tar.gz

# Compile OpenResty with ngx_cache_purge module
RUN cd openresty-${OPENRESTY_VERSION} && \
    ./configure --add-module=../ngx_cache_purge-${NGX_CACHE_PURGE_VERSION} \
    --with-http_ssl_module && \
    make && make install

# Use the official OpenResty image to run our custom build
FROM openresty/openresty:buster

# Copy the custom OpenResty build from the builder stage
COPY --from=builder /usr/local/openresty /usr/local/openresty

# Expose HTTP and HTTPS ports
EXPOSE 80 443

# Set the working directory and default command for the container
WORKDIR /usr/local/openresty/nginx
CMD ["/usr/local/openresty/bin/openresty", "-g", "daemon off;"]
