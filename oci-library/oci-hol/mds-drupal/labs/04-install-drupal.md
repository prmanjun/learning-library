# Drupal

## Drupal Installation

## Install Drupal in your Oracle Linux instance


1. From your SSH enabled terminal, SSH to the Oracle Linux instance where wordpress will be installed.

```
ssh -i <path/private key> opc@<instance public IP>
```


2. Install Drupal required packages

```
sudo yum install -y  php-mbstring php-gd php-xml php-pear php-fpm php-mysql php-pdo php-opcach           
```

3. Edit the httpd.conf

```
sudo vim /etc/httpd/conf/httpd.conf
```

4. Locate the section **<Directory "/var/www/html">** and in that section change **AllowOverride All** to **AllowOverride None**. You can navigate on the file until you find it or press "**/**", and enter **Options Indexes FollowSymLinks**. It should be a few lins bellow

5. Restart Apache

```
sudo systemctl restart httpd
```

6. Dowload the latest Drupal from  

```
curl -L -o drupallatest.tar.gz  https://www.drupal.org/download-latest/tar.gz
```

3. Extract latest.tar.gz to /var/www/html (Apache Document Root)

```
sudo tar zxf drupallatest.tar.gz -C /var/www/html/ --strip 1
```

4. Adjust ownership

```
sudo chown apache. -R /var/www/html/
```

5. Create settings.php

```
cd /var/www/html/sites/default/
cp default.settings.php settings.php
```

4. Adjust ownership

```
sudo chown apache. -R /var/www/html/
```

6. Adjust SE Linux

```
sudo chcon -R -t httpd_sys_content_rw_t /var/www/html/sites/
```

6. Allow Apache to connect to an external database.

```
sudo setsebool -P httpd_can_network_connect_db 1
```

7. Connect to the MDS database using MySQL Shell

```
mysqlsh --sql -u admin -h <MDS end point IP>
```

8. Create Drupal database and user

```
create database drupal;
create user drupaluser IDENTIFIED BY 'ComplexPass0rd!';
GRANT ALL PRIVILEGES ON drupal.* To drupaluser;
\quit
```

9. From a browser access http://*instance public IP*/

10. Choose language and Click **Save and Continue**

11. **Select an installation profile**, select **Standard** profile and Click **Save and Continue**

12. If all settings are corret, you see the database configuration page. Fill the following information:

* **Database type** : MySQL, MariaDB, Percona Server, or equivalent
* **Database name**: drupal
* **Database username**: drupaluser
* **Database password**: ComplexPass0rd!

Expand **Advanced options**

* **Host**: MDS IP address

13. Click **Install site** 

14. Configure the site by entenring the following information:

* Site name: Choose your site name
* Site email address: email account for automated emails sent by the site
* Username: Drupal admininistrator
* Password : Drupal admininistrator password
* Confirm password: confirm password
* Email address: youremail address
* Default country: choose the country
* Default time zone: choose the timezone
* Check for updates automatically: checked
* Receive email notifications : unchecked

15. Click on **Save and continue**

15. From a browser access http://*instance public IP*/, login with your admin user and start customizing the website
