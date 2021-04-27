# Wordpress

## WordPress Installation

## Install WordPress in your Oracle Linux instance


1. From your SSH enabled terminal, SSH to the Oracle Linux instance where wordpress will be installed.

```
ssh -i <path/private key> opc@<instance public IP>
```

2. Install Wordpress required packages

```
sudo yum install -y php-mysqlnd php-zip php-gd php-mcrypt php-mbstring php-xml php-json
```

2. Dowload the latest Worpress.

```
curl -O https://wordpress.org/latest.tar.gz
```

3. Extract latest.tar.gz to /var/www/html (Apache Document Root)

```
sudo tar zxf latest.tar.gz -C /var/www/html/ --strip 1
```

4. Adjust ownership

```
sudo chown apache. -R /var/www/html/
```

5. Create upload directory, adjust ownership. 

```
sudo mkdir /var/www/html/wp-content/uploads
sudo chown apache:apache /var/www/html/wp-content/uploads
```

6. Adjust SE Linux

```
chcon -t httpd_sys_rw_content_t /var/www/html -R
```

6. Allow Apache to connect to an external database.

```
sudo setsebool -P httpd_can_network_connect_db 1
```

7. Connect to the MDS database using MySQL Shell

```
mysqlsh --sql -u admin -h <MDS end point IP>
```

8. Create Wordpress database and user

```
create database wordpress;
create user wordpress IDENTIFIED BY 'ComplexPass0rd!';
GRANT ALL PRIVILEGES ON wordpress.* To wordpress;
\quit
```

9. From a browser access http://*instance public IP*/wp-admin/setup-config.php

10. Click **Let's Go**

11. Fill the following information:

|Field | Name |
| --- | --- |
| Database Name database you created for WordPress
| Username Your database username
| Password Your database password
| Database HostMDS IP address
| Table Prefixleave as is. only need to change if multiple WordPress running on the same database

12. Click **Run the installation**

13. Fill the following information in the welcvome screen

|||
|---|---|
| Site Title WordPress site title
| Username WordPresss admin
| Password *WordPresss admin password*
| Your Email your email

14. Click **Install WordPress**
 	
15. From a browser access http://*instance public IP*/wp-login.php and star managing your new WP installation
