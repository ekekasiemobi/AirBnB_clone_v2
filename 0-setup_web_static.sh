#!/usr/bin/env bash
# Install Nginx if not already installed

apt-get update
apt-get install -y nginx

mkdir -p /data/web_static/releases/test
mkdir -p /data/web_static/shared

sudo echo "Welcome to my World!" | sudo tee /data/web_static/releases/test/index.html

if [ -L /data/web_static/current ]; then
    rm /data/web_static/current
fi

echo "$config_content" > /etc/nginx/sites-available/my_config

ln -s /data/web_static/releases/test /data/web_static/current

chown -R ubuntu:ubuntu /data/

config_content="
server{
    listen 80 default_server;
	listen [::]:80 default_server;

	server_name _;
	index index.html index.htm;
	error_page 404 /404.html;
	add_header X-Served-By \$hostname;

	location / {
		root /var/www/html/;
		try_files \$uri \$uri/ =404;
	}

	location /hbnb_static/ {
		alias /data/web_static/current/;
		try_files \$uri \$uri/ =404;
	}

	if (\$request_filename ~ redirect_me) {
		rewrite ^ https://sketchfab.com/bluepeno/models permanent;
	}

	location = /404.html {
		root /var/www/error/;
		internal;
	}
}"

sudo service nginx start
