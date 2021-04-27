## Configure Apache with PHP

### Install and configure Apache HTTP server with PHP

1. Open the Oracle Cloud Infrastructure main menu.

2. Select **Compute** then **Instances**.

3. From the list of instances, click on the instance name you want to configure the HTTP server.

4. Once the instance details are loaded, find on **Public IP Address:** on the right side, under **Istance Access**. Copy the Public IP access.

5. From a terminal (Cloud Shell or any other SSH enabled terminal), connect to the instance:

```
ssh -i </path/private key file> opc@<instance's public IP>

```

6. Install Apache HTTP Server and php. Dependencies will be resolved automatically and installed.

```
sudo yum install -y httpd

```
7. Enable and start Apache HTTP Server.

```
sudo systemctl enable httpd --now 

```
8. Allow HTTP and HTTPS in the local iptables firewall 

```
sudo firewall-cmd --permanent --add-port=80/tcp
sudo firewall-cmd --permanent --add-port=443/tcp
sudo firewall-cmd --reload
```

9. Add the extra repositories:

```
sudo yum -y install https://dl.fedoraproject.org/pub/epel/epel-release-latest-7.noarch.rpm
sudo yum -y install https://rpms.remirepo.net/enterprise/remi-release-7.rpm
sudo yum-config-manager --enable remi-php74
```

10. Install PHP

```
sudo yum install -y php 
```

11. Restart Apache

```
sudo systemctl restart httpd
```

12. Create a test php page

```
echo -e '<?php \nphpinfo();' | sudo tee /var/www/html/test.php
```

13. From a web browser, navigate to **http://*public server IP*/test.php**


## Install MySQL and MySQL Shell

### Install MySQL and MySQL Shell

1. Install MySQL release package.


```
sudo yum -y install https://dev.mysql.com/get/mysql80-community-release-el7-3.noarch.rpm
```

2. Install MySQL Shell

```
sudo yum -y install mysql-shell
```