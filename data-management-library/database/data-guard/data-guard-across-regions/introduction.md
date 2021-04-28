# Introduction

Oracle Data Guard provides disaster recovery for your Oracle databases.  A standby database is set up to receive redo transaction logs from the primary database.  In the event of a disaster on the primary database, a failover to the standby database will occur.  

For disaster recovery, it is a common practice to set up the primary and standby database in two different data centers preferably located in different geographies.  In this guide we will be setting up Oracle Data Guard between two cloud regions using Oracle Database Cloud Service.  

Prerequisites

- An Oracle Free Tier, Paid or LiveLabs Cloud Account with access to more than one cloud region

- Oracle Cloud user role to manage networks and databases

- SSH public and private keys

- Compartment to work on

Although the primary database will be in one region and the standby in another region, they must both be in the same compartment.  And they must both not have overlapping VCN IP address blocks.

Estimated lab time:  30 minutes



## Learn More

- [Using Oracle Data Guard](https://docs.oracle.com/en-us/iaas/Content/Database/Tasks/usingdataguard.htm)

- [OCI Remote Peering](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/remoteVCNpeering.htm)



## Acknowledgements

- **Author** - Milton Wan, Database Product Management, January 2021
- **Contributors** -
- **Last Updated By/Date** - Milton Wan, Database Product Management, January 24, 2021
- **Workshop Expiry Date** - January 2023
