# Prepare Target ATP

## Introduction

Up to now we have created all of the necessary resources using Terraform in OCI. It is now time to prepare the Target Database, ATP. 

*Estimated lab time*: 10 minutes

### Objectives

We need to create our target tables for our GoldenGate migration and enable GGADMIN for replication to the Autonomous Database.

For a technical overview of this lab step, please watch the following video:

[](youtube:K89v3fprzpg)

### Prerequisites

* This lab assumes that you completed all preceding labs.

## **Step 1**: Open SQL Developer Web 

1. Go to the top-left hamburger icon, navigate to **Autonomous Transaction Processing** and click on **HOL Target ATP** database.

	![](/images/2.atp.PNG)

2. In **Tools** tab, where you will see **Database Actions**, click on **Open Database Actions**. You may need to enable a pop-up in your browser if it doesn't open anything.

	![](/images/2.atp_1.PNG)

3. A new sign-in page opens, enter **ADMIN** in Username, when it asks you to enter the password, which is in the terraform output. Go and copy, then paste here.

	![](/images/sql_dev_1.png)

4. In the **DEVELOPMENT** section, click on **SQL**. 

	![](/images/sql_dev_5.png)

## **Step 2**: Create Target Tables

1. Let's create our target tables for migration. Please download the target table creation script **[from here](./files/CreateTables.sql)**. Make sure to save these with the correct extension **.sql** not txt!

2. SQL Developer Web opens a worksheet tab, where you execute queries. Drag your downloaded **CreateTables.sql** file and drop it in the worksheet area. Then run create statements.

	![](/images/sql_dev_2.png)

	There should be **5** tables created after script execution.


## **Step 3**: Enable GGADMIN 

1. Now let's continue to unlock and change the password for Oracle GoldenGate user (ggadmin) in the Autonomous Database. Enable GGADMIN by running the following query.

	```
	<copy>
	alter user ggadmin identified by "GG##lab12345" account unlock;
	</copy>
	```

	![](/images/sql_dev_3.png)

2. Let's check whether the parameter `enable_goldengate_replicaton` is set to true. 

	```
	<copy>
	select * from v$parameter where name = 'enable_goldengate_replication';
	</copy>
	```

	![](/images/sql_dev_4.png)
	
3. If value is _**FALSE**_ then modify the parameter, else go to next step.

	```
	<copy>
	alter system set enable_goldengate_replication = true scope=both;
	</copy>
	```

	We successfully enabled GGADMIN in our target Autonomous Database and created target table structures. 

**This concludes this lab. You may now [proceed to the next lab](#next).**

## Acknowledgements

* **Author** - Bilegt Bat-Ochir - Senior Solution Engineer
* **Contributors** - John Craig - Technology Strategy Program Manager, Patrick Agreiter - Senior Cloud Engineer
* **Last Updated By/Date** - Bilegt Bat-Ochir 4/15/2021