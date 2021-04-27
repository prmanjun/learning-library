# MySQL Database Service

## Create and Configure MySQL Database Service

## MDS Required policy

1. Open the navigation menu. Under **Governance and Administration**, go to **Identity** and click **Policies**. 

2. On the Policies Page, under List Scope, select the Compartment(root) and click on the Create Policy button.

3. Enter the following information:

* **Name**: policy name
* **Compartment**: (root)

4. In the **Policy Builder**, click **Customize (Advanced)**

5. Enter the following required MySQL Database Service policies:


On Create Policy , enter  , , select the Root comaprtment, and click on Customize (Advanced) button. 
    
4. Enter the following required MySQL Database Service policies:
|Policy Statements|
```
Allow group Administrators to {COMPARTMENT_INSPECT} in tenancy
Allow group Administrators to {VCN_READ, SUBNET_READ, SUBNET_ATTACH, SUBNET_DETACH} in tenancy
Allow group Administrators to manage mysql-family in tenancy
```

5. Click **Create**

## Create MDS

### Create your MySQL Database Service

1. Open the navigation menu. Under **Database**, go to **MySQL** and click **DB Systems**
    
2. On the **DB Systems** page, select the compartment and click on **Create MySQL DB System**.

3. Enter the following information:

* **Name DB system**: name
* **Description**: MySQL system Description
* **Compartment**: select the compartment
* **Select an Availability Domain**: select the availability domain
* **Fault Domain**: Optional. Can be left unchecked
* **Select a Shape**: choose the desired shape by clicking on **Change Shape**
* **Data Storage Size (GB)**: Enter the desired storage size
* **Maintenance Window Start Time**: None

4. Click **Next** to advance to **Database Information** screen

5. Enter the following information:

* **Username**: administrator user name
* **Password**: admin password
* **Confirm Password**: admin password
* ***Virtual Cloud Network in** select the VCN compartment
* **Virtual Cloud Network** select the a private VCN
* **Hostname**: hostname name
* **MySQL Port**: 3306
* **MySQL X Protocol Port**: 33060

6. Click **Next** to advance to **Backup Information** screen

7. Enter the following information:

* **Enable Automatic Backups**: checked
* **Backup retention period**: 7
* **Default Backup Window**: checked


8. You will be taken to the MySQL DB System's details page. Once the yellow hexagon turns green, your DB system will be provisioned, up and running.
