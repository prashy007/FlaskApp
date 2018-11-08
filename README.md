# FlaskApp

##Once you are in the server, let's start with an update and upgrade:
sudo apt-get update && sudo apt-get upgrade

##Since I have used mysql database in this application:
sudo apt-get install mysql-client mysql-server
##Once installation is complete, it will prompt for root user password.
sudo apt-get update
##Get python3.6 and pip
sudo apt-get install python3.6 python-dev python-pip
##Now that we have Python 3.6, we will install our webserver. For this, I have used Apache:
sudo apt-get install apache2 apache2-dev
##In order for our apps to talk with Apache, we need an intermediary, a gateway interface called WSGI (Web Server Gateway Interface). We will install WSGI for Python:
pip install mod_wsgi
##After installing wsgi mod, Restart Apache with:
service apache2 restart
##Now our web server and the interface are ready, we just need our web app. Since I have build using Flask, 
pip install Flask
###Now,
##Create a configuration file inside ###/etc/apache2/sites-available/
mkdir /etc/apache2/sites-available/FlaskApp.conf
nano /etc/apache2/sites-available/FlaskApp.conf


##Inputting:
<VirtualHost *:80>
		ServerName IP of machine
		ServerAdmin admin@mywebsite.com
		WSGIScriptAlias / /var/www/FlaskApp/flaskapp.wsgi
		<Directory /var/www/FlaskApp/FlaskApp/>
			Order allow,deny
			Allow from all
		</Directory>
		Alias /static /var/www/FlaskApp/FlaskApp/static
		<Directory /var/www/FlaskApp/FlaskApp/static/>
			Order allow,deny
			Allow from all
		</Directory>
		ErrorLog ${APACHE_LOG_DIR}/error.log
		LogLevel warn
		CustomLog ${APACHE_LOG_DIR}/access.log combined
</VirtualHost>

###Save and Exit
##Now let's enable the site:
sudo a2ensite FlaskApp
##Restart Apache service:
service apache2 restart
##Now we will start preparing our Flask application. Let’s set up some directories:
mkdir /var/www/FlaskApp
cd /var/www/FlaskApp
nano flaskApp.wsgi
##Now we will setup WSGI to interface with our application:
##In flaskApp.wsgi,  put:
#!/usr/bin/python
import sys
import logging
logging.basicConfig(stream=sys.stderr)
sys.path.insert(0,"/var/www/FlaskApp/")

from FlaskApp import app as application
##Save and exit. Our FlaskApp.conf file points to this WSGI file. This WSGI script imports app from FlaskApp. 

##Now we will setup our FlaskApp application:
mkdir /var/www/FlaskApp/FlaskApp 
cd /var/www/FlaskApp/FlaskApp
mkdir /var/www/FlaskApp/FlaskApp/static
mkdir /var/www/FlaskApp/FlaskApp/templates
###The directory structure for FlaskApp programing should be.
/var/www/
|--------FlaskApp
|----------------FlaskApp
|-----------------------static –This contains css and js folder.
|-----------------------templates –This contains all html files.
|-----------------------__init__.py –This is our main flask program.
|----------------flaskapp.wsgi
   
###I have used bootstrap for css and js. Download bootstrap and extract css and js folders to static folder create above.
###Now:
cd /var/www/FlaskApp/FlaskApp
nano __init__.py   –> Write code here. Please find codes uploaded.
###Now run:
service apache2 stop
service apache2 start
#Now we will be able to visit http://IP of machine for our WebApp.
=======================================================
**_We can create Docker image for this. Please refer to Dockerfile created._**
=======================================================
