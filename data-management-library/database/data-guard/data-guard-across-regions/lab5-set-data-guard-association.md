

# Enable Oracle Data Guard for Oracle Database Cloud Service

Setting up Data Guard for Database Cloud Service is a simple process.  We enable Data Guard in the primary database and the standby database is automatically created.

Prerequisite

- VCN for both the primary and standby regions are created

- Database Cloud Service Enterprise Edition or higher is created

- DRGs and RPCs are created

- RPC connection is peered

- Route Rules and Security List are configured for secure communication between primary and standby VCNs


Navigate to your Database Cloud Service in your primary region.



![image-20210121190217365](./images/image-20210121190217365.png)



1. Go to your database details page.

2. Select your database under resources.




![image-20210121190255856](./images/image-20210121190255856.png)

3. Select Data Guard Associations.

4. Click Enable Data Guard for your database.



![image-20210121190326859](./images/image-20210121190326859.png)

Data Guard is defaulted to Maximum Performance Protection Mode which means the redo log is transmitted to the standby immediately and does not wait for the standby to complete the redo apply.  It is also set the Async Transport type.  Maximum Protection mode is not available at this time.

5. Enter a name for your peer standby database.

6. Enter the region of your standby.

7. Enter the availability domain you want to install the standby.  Some regions only have one availability domain.

8. Select the shape or size of the standby database.

9. Click enable.



![](./images/image-20210121182459418.png)



Because the networking and remote peering connection is configured, the standby database and Data Guard will automatically be created.

Check your standby region.  A standby database should be creating and updating.



![image-20210121190528443](./images/image-20210121190528443.png)



Check the Data Guard association.  You will see the primary being associated.



![image-20210121190421254](./images/image-20210121190421254.png)



Completed.

The standby database is now ready for a failover.



![image-20210121222339306](./images/image-20210121222339306.png)
