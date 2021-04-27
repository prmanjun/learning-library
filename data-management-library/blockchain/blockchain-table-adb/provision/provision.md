# Provision Autonomous Database Instance (lab in Development)

## Introduction

In this lab, you will provision the Oracle Autonomous Database instance

Estimated Lab Time: 5 minutes

### Objectives

In this lab, you will:
- Provision an Autonomous Database instance

### Prerequisites

- This lab requires an [Oracle Cloud account](https://www.oracle.com/cloud/free/). You may use your own cloud account, a cloud account that you obtained through a trial, a Free Tier account, or a LiveLabs account.

## **STEP 1**: Provision an ADW instance

1. Login to the Oracle Cloud, as shown in the previous lab.

2. If you are using a Free Trial or Always Free account, and you want to use Always Free Resources, you need to be in a region where Always Free Resources are available. You can see your current default **Region** in the top, right hand corner of the page.

    ![Select region on the far upper-right corner of the page.](./images/Region.png " ")

3. Once you are logged in, you can view the cloud services dashboard where all the services available to you. Click on hamburger menu, search for Autonomous Data Warehouse and select it.

    **Note:** You can also directly access your Autonomous Data Warehouse or Autonomous Transaction Processing service in the **Quick Actions** section of the dashboard.

    ![](./images/choose-adb.png " ")

4. From the compartment drop-down menu select the **Compartment** where you want to create your ADB instance. This console shows that no databases yet exist. If there were a long list of databases, you could filter the list by the **State** of the databases (Available, Stopped, Terminated, and so on). You can also sort by **Workload Type**. Here, the **Data Warehouse** workload type is selected.

    ![](images/livelabs-compartment.png " ")

5. Click **Create Autonomous Database** to start the instance creation process.

    ![Click Create Autonomous Database.](./images/Picture100-23.png " ")

6.  This brings up the **Create Autonomous Database** screen, specify the configuration of the instance:
    - **Compartment** - Select a compartment for the database from the drop-down list.
    - **Display Name** - Enter a memorable name for the database for display purposes. This lab uses **DEMOATP** as the ADB display name.
    - **Database Name** - Use letters and numbers only, starting with a letter. Maximum length is 14 characters. (Underscores not initially supported.) This lab uses **DEMOATP** as database name.

    ![Enter the required details.](./images/adw-wine.png " ")

7. Choose a workload type, deployment type and configure the database:
    - **Choose a workload type** - For this lab, choose __Transaction Processing__ as the workload type.
    - **Choose a deployment type** - For this lab, choose **Shared Infrastructure** as the deployment type.
    - **Always Free** - If your Cloud Account is an Always Free account, you can select this option to create an always free autonomous database. An always free database comes with 1 CPU and 20 GB of storage. For this lab, we recommend you to check **Always Free**.
    - **Choose database version** - Select **21c** database version from the available versions.
    - **OCPU count** - Number of CPUs for your service. Leave as it is, or if you choose an Always Free database, it comes with 1 CPU.
    - **Storage (TB)** - Select your storage capacity in terabytes. Leave as it is or, if you choose an Always Free database, it comes with 20 GB of storage.
    - **Auto Scaling** - For this lab, keep auto scaling enabled.

    ![Choose the remaining parameters.](./images/Picture100-26c.png " ")

8. Create administrator credentials, choose network access and license type and click **Create Autonomous Database**.

    - **Password** - Specify the password for **ADMIN** user of the service instance.
    - **Confirm Password** - Re-enter the password to confirm it. Make a note of this password.
    - **Choose network access** - For this lab, accept the default, "Allow secure access from everywhere".
    - **Choose a license type** - For this lab, choose **License Included**.

    ![](./images/create.png " ")

9.  Your instance will begin provisioning. In a few minutes, the state will turn from Provisioning to Available. At this point, your Autonomous Data Warehouse database is ready to use! Have a look at your instance's details here including its name, database version, OCPU count, and storage size.

    ![Database instance homepage.](./images/provision.png " ")

    ![Database instance homepage.](./images/provision-2.png " ")


Please *proceed to the next lab*.

## Acknowledgements

* **Author** - Anoosha Pilli, Database Product Manager
* **Contributors** -  Anoosha Pilli, Database Product Management
* **Last Updated By/Date** - Anoosha Pilli, April 2021
