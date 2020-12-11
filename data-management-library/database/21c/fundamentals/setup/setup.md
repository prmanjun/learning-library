# Setup 21C Environment

## Introduction
In this lab, you will run the scripts to setup the environment for the Oracle Database 21c workshop.

Estimated Lab Time: 15 minutes

### Objectives

In this lab, you will:
* Define and test the connections
* Download scripts needed to run 21c labs
* Update scripts with the chosen password

### Prerequisites

* An Oracle Free Tier, Always Free, Paid or LiveLabs Cloud Account
* Working knowledge of vi or nano
* Completed Lab: SSH Keys
* Completed Lab: Create a DBCS VM Database
* DBCS Public Address
* Database Unique Name


## **STEP 1**: Define and test the connections

1. If you aren't still logged in, login to Oracle Cloud and re-start the Oracle Cloud Shell otherwise skip to Step 4.
2. In Cloud Shell or your terminal window, navigate to the folder where you created the SSH keys and enter this command, using your IP address:

    ```
    $ <copy>ssh -i ./myOracleCloudKey opc@</copy>123.123.123.123
    Enter passphrase for key './myOracleCloudKey':
    Last login: Tue Feb  4 15:21:57 2020 from 123.123.123.123
    [opc@tmdb1 ~]$
    ```
3. Once connected, you can switch to the "oracle" OS user and connect using SQL*Plus:

    ```
    [opc@tmdb1 ~]$ sudo su - oracle
    [oracle@tmdb1 ~]$ . oraenv
    ORACLE_SID = [cdb1] ?
    The Oracle base has been set to /u01/app/oracle
    [oracle@tmdb1 ~]$ sqlplus / as sysdba

    SQL*Plus: Release 21.0.0.0.0 - Production on Sat Nov 15 14:01:48 2020
    Version 21.2.0.0.0

    Copyright (c) 1982, 2020, Oracle.  All rights reserved.

    Connected to:
    Oracle Database 21c EE High Perf Release 21.0.0.0.0 - Production
    Version 21.0.0.0.0

    SQL>
	```

4. Verify that your Oracle Database 21c `CDB21` and `PDB21` are created using the commands below.

	```
	<copy>
	ps -ef|grep smon
	sqlplus / as sysdba
	</copy>
	```
	```
	<copy>
	show pdbs
	</copy>
	```

3. Ensure that the TNS alias have been created for both cdb21 and pdb21 in the tnsnames.ora file. If they are not there then you will need to add them. The file is located in `/u01/app/oracle/homes/OraDB21Home1/network/admin/tnsnames.ora`

	```
	<copy>
	cat /u01/app/oracle/homes/OraDB21Home1/network/admin/tnsnames.ora
	</copy>
	```

4. In order to create the TNS Entries for the CDB1 and PDB1 you will need the correct SERVICE\_NAME parameters for them. We will use the lsnrctl program to get the SERVICE\_NAME values for our TNS entries.

	```
	lsnrctl status
	```

5. The output of the lsnrctl command will give you several entries. The two we care about are the following. Your values will be slightly different based on your vcn name, subnet and region.

	```
	Service "cdb1_iad1vs.subnet11241424.vcn11241424.oraclevcn.com"
	Service "pdb1.subnet11241424.vcn11241424.oraclevcn.com"
	```

6. You are going to create two entries in the tnsnames.ora file. One for CDB1 and one for PDB1. Edit the tnsnames.ora using vi or nano to edit.

	````
	<copy>
	vi /u01/app/oracle/homes/OraDB21Home1/network/admin/tnsnames.ora
	</copy>
	````

7. Copy the entry for CDB1 that is already in the tnsnames file. Make the following changes:
    - Change the name of the entry to be CDB1 instead of the Unique Database Name.
		- Make sure the SERVICE\_NAME parameter has SERVICE\_NAME from the lsnrctl command above.
		- Do not change the host and port values.

	````
	CDB1 =
	(DESCRIPTION =
	(ADDRESS = (PROTOCOL = TCP)(HOST = hostname21.subnet11241424.vcn11241424.oraclevcn.com)(PORT = 1521))
	(CONNECT_DATA =
	(SERVER = DEDICATED)
	(SERVICE_NAME = cdb1_iad1vs.subnet11241424.vcn11241424.oraclevcn.com)
	)
	)
	````

8. Repeat the same process for PDB1 in the tnsnames file making the following changes:
    - Change the name of the entry to be PDB1 instead of the Unique Database Name.
    - Make sure the SERVICE\_NAME parameter has SERVICE\_NAME from the lsnrctl command above.
    - Do not change the host and port values.

		````
		PDB1 =
		(DESCRIPTION =
		(ADDRESS = (PROTOCOL = TCP)(HOST = hostname21.subnet11241424.vcn11241424.oraclevcn.com)(PORT = 1521))
		(CONNECT_DATA =
			(SERVER = DEDICATED)
			(SERVICE_NAME = pdb1.subnet11241424.vcn11241424.oraclevcn.com)
		)
		)
		````

9. Test the connection to CDB1.  Connect to CDB1 with SQL*Plus.

	````
	<copy>
	sqlplus sys@cdb1 AS SYSDBA
	</copy>
	````

10. Verify that the container name is CDB$ROOT.

	````
	<copy>
	SHOW CON_NAME;
	</copy>
	````

11. Test the connection to PDB1

	````
	<copy>
	CONNECT sys@PDB1 AS SYSDBA
	</copy>
	````

8.  Show the container name

	````
	<copy>
	SHOW CON_NAME;
	</copy>
	````

9. Exit SQL*Plus

	````
	<copy>
	exit
	</copy>
	````

## **STEP 2**: Download scripts

Download the Cloud\_21c\_labs.zip file to the /home/oracle directory from Oracle Cloud object storage and unzip the file.

*Note*: These scripts are designed for DBCS VM single node instances

1.  Change to the oracle user home directory

	````
	<copy>
	cd /home/oracle
	wget https://objectstorage.us-ashburn-1.oraclecloud.com/p/te64gQPSzMrOJZh5jwYPrmS6xwtddOdN90lIWF6mAvM_uIbJlAUEhyGzugZhUTF3/n/oraclepartnersas/b/workshop/o/Cloud_21c_Labs.zip
  </copy>
	````

2.  Unzip Cloud\_21c\_labs.zip

	```
	<copy>
	unzip Cloud_21c_Labs.zip
	</copy>
	```

## **STEP 3**: Update the scripts to the current environment

Execute the /home/oracle/labs/update\_pass.sh shell script. The shell script prompts you to enter the password\_defined\_during\_DBSystem\_creation and sets it in all shell scripts and SQL scripts that will be used in the practices.

1. Make the script readable, writable, and executable by everyone.

	```
	<copy>
	chmod 777 /home/oracle/labs/update_pass.sh
	</copy>
	```

2. Run the script.

	```
	<copy>
	/home/oracle/labs/update_pass.sh
	</copy>
	```

You may now [proceed to the next lab](#next).

## Acknowledgements
* **Author** - Dominique Jeunot, Database UA Team
* **Contributors** -  David Start, Kay Malcolm, Database Product Management
* **Last Updated By/Date** -  David Start, December 2020

## Need Help?
Please submit feedback or ask for help using our [LiveLabs Support Forum](https://community.oracle.com/tech/developers/categories/livelabsdiscussions). Please click the **Log In** button and login using your Oracle Account. Click the **Ask A Question** button to the left to start a *New Discussion* or *Ask a Question*.  Please include your workshop name and lab name.  You can also include screenshots and attach files.  Engage directly with the author of the workshop.

If you do not have an Oracle Account, click [here](https://profile.oracle.com/myprofile/account/create-account.jspx) to create one.
