#!/bin/bash
# Install Nginx if not already installed

apt-get update
apt-get install -y nginx

mkdir -p /data/web_static/releases/test
mkdir -p /data/web_static/shared

sudo echo "Welcome to my World!" | sudo tee /data/web_static/releases/test/index.html

# Create or recreate the symbolic link
if [ -L /data/web_static/current ]; then
    rm /data/web_static/current
fi

ln -s /data/web_static/releases/test /data/web_static/current

chown -R ubuntu:ubuntu /data/

printf %s "server {
    listen 80 default_server;
    listen [::]:80 default_server;

    server_name _;

    location /hbnb_static {
        alias /data/web_static/current;
    }

    location / {
        return 404;
    }
}"

sudo service nginx start
