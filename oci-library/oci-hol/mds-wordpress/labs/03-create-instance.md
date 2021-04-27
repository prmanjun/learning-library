# Compute VM instance

## Create VM Compute Instance and configure Apache and PHP

## Create Compute Instance

### Create Oracle Linux instance to host your Apache web server.

1. Open the Oracle Cloud Infrastructure main menu.

2. Select **Compute** then **Instances**.

3. From the list of instances screen click **Create Instance**.

4. Enter a name for the instance.

5. Select the compartment to create the instance in.

6. In the Configure placement and hardware section, make the following selections:

    * Availability domain Select the Availability domain that you want to create the instance in
    * Fault Domain Optional. Can be left unchecked
    * Image Latest Oracle Linux ( by default the latest supported version will be already selected)
    * Shape Select the desired shape

7. In the **Configure networking ** section, make the following selections:


    * Network Select an existing virtual cloud network
    * Virtual cloud network in Choose the compartent that has the desired VCN
    * Network Select the Virtual Network Cloud Network
    * Subnet in Choose the compartent that has the desired VCN
    * Subnet Select a public subnet
    * Use network security groups to control traffic unchecked
    * Public IP Address |  *Assign a public IPv4 address
    
8. In the **Add SSH keys** section:

    If you don't have a SSH key pair: 
    1. Select **Generate SSH key pair**.
    2. Click on **Save Private Key** and follow the browser propmpt to save the private key.
    3. Click on **Save Public Key** and follow the browser propmpt to save the public key.

    If you have a public key, you can:
    
    1. Select **Choose public key files**
    2. Drag and drop the public key files over or **Or browse to a location.**, find the location and select the files.

    or

    1. Select **Paste public keys**.
    2. Paste the Public Key Value into **SSH keys** (multiple keys can be added by clicking on **Anotehr key**).


9. In the **Configure boot volume**, leave all options unchecked.

10. Click **Create**.

11. You will be taken to the instance's details page. Once the yellow square turns green, your instance will be provisioned, up and running. 


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

10. Install PHP and and WordPress PHP required packages.

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