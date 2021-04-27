# Create Datasource Connections

## Introduction
This lab describes how to configure datasource connections. The Oracle GoldenGate Veridata  Server must be able to connect to an Oracle GoldenGate Veridata Agent for each database that contains source and target data that you want to compare. A connection is defined by a host, the port number of an Oracle GoldenGate Veridata Agent (or Manager, if a C-agent), and the datasource that is accessed by the agent. You need to create connections before you create any of the GoldenGate Veridata objects, such as groups, compare pairs, profiles, or jobs.

*Estimated Lab Time*: 15 minutes

### Objectives
In this lab, you will:
* Create a Connection in Oracle GoldenGate Veridata.

### Prerequisites
This lab assumes you have:

* A Free Tier, Paid or LiveLabs Oracle Cloud account
* SSH Private Key to access the host via SSH
* You have completed:
    * Lab: Generate SSH Keys (Free-tier and Paid Tenants only)
    * Lab: Prepare Setup (Free-tier and Paid Tenants only)
    * Lab: Environment Setup
    * Lab: Initialize Environment
* The following are required to complete this lab:
    * Oracle GoldenGate Veridata installed
    * Oracle Database 19c (19.3.0.0) (for the repository)

## **STEP 1:** Login to Oracle GoldenGate Veridata
  To login to GoldenGate Veridata:
  1. In a browser, enter the URL, for example: http://*veridata_server_host:veridata_server_port-number*/veridata/login.jsf.
  2. Enter your login credentials and click **Login**:
      ![](./images/1-login-veridata.png " ")

## **STEP 2:** Create a Connection
To get started with Oracle GoldenGate Veridata, you must define a connection to the source and target databases that contain the data that you want to compare. Oracle GoldenGate Veridata Server uses the connection information to communicate with Oracle GoldenGate Veridata Agent.

**Note**: Ensure that you have the Administrator or the Power User roles to create and configure connections.

To create connections:
1. From the left navigation pane, click **Configuration** and then click **Connection Configuration** to display the **Connection configuration** page.
    ![](./images/2-connection-configuration.png " ")
2. Click **New** to display the **New Connection Assistant** page to create one connection for the source database.
3. Enter the **Connection Name**, for example, **SourceConnection** and click **Next**.
    ![](./images/3-connection-name-description.png " ")
4. Enter the following details:
    * **Host Name or IP Address**: Name of the host where Oracle GoldenGate Veridata Agent is running.
    * **Port**: The port number for Oracle GoldenGate Veridata Agent on that host.
    * **Datasource Type**: The datasource that is associated with this agent.
      ![](./images/4-new-connection-assistant.png " ")
5. Click **Next** to enter the Datasource Connection credentials:
    ![](./images/5-new-connection-assistant-datasource-credentials.png " ")
6. Click **Finish**.
  You have created one connection successfully.
7. Click **Create another Connection** to create the target connection, and click **OK** to display the **New Connection Assistant** page.
  ![](./images/5-new-connection-assistant-create-another-connection.png " ")
7. Follow points 3 to 6 to create another connection (for example, **TargetConnection**) for the target database.

## Learn More

* [Oracle GoldenGate Veridata Documentation](https://docs.oracle.com/en/middleware/goldengate/veridata/12.2.1.4/index.html)
* [Configuring Connections](https://docs.oracle.com/en/middleware/goldengate/veridata/12.2.1.4/gvdug/configure-workflow-objects.html#GUID-75005B4D-5C24-4467-A68B-1FE66A168905)

### Acknowledgements
* **Author** - Anuradha Chepuri, Principal UA Developer, Oracle GoldenGate User Assistance
* **Contributors** -  Nisharahmed Soneji (PM), Sukin Varghese (QA), GoldenGate
* **Last Updated By/Date** - Anuradha Chepuri, Oracle GoldenGate User Assistance, April 2021
