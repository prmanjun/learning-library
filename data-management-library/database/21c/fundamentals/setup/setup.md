# Setup Environment

## Introduction
In this lab, you will run the scripts to setup the environment for the Oracle Database 21c workshop. 

Estimated Lab Time: 15 minute

### Objectives

In this lab, you will:
* Define and test the connections
* Download scripts
* Update scripts

### Prerequisites

* An Oracle Free Tier, Always Free, Paid or LiveLabs Cloud Account
* Working knowledge of vi

## **STEP 1**: Define and test the connections

1. Verify that your Oracle Database 21c `CDB21` and `PDB21` are created, that alias entries are either automatically or manually created in `/u01/app/oracle/homes/OraDB21Home1/network/admin/tnsnames.ora`

2. The sub-directory `OraDB21Home1` is the sub-directory mentioned in the file `/u01/app/oraInventory/ContentsXML/oraInventory`.
   
      ````
      <HOME_LIST>
      <HOME NAME="OraGrid210" LOC="/u01/app/21.0.0.0/grid" TYPE="O" IDX="1" CRS="true">
      <HOME NAME="<B>OraDB21000_home1</B>" LOC="/u01/app/oracle/product/21.0.0.0/dbhome_1" TYPE="O" IDX="2">
      </HOME_LIST>
      ````
3. Create an alias entry by copying the CDB alias entry, replace the CDB alias name with your PDB name, and the CDB service name with your PDB service name.
   
      ````
      cat /u01/app/oracle/homes/OraDB21Home1/network/admin/tnsnames.ora
      ````
4. Create an alias entry by copying the CDB alias entry, replace the CDB alias name with your PDB name, and the CDB service name with your PDB service name.  Use vi to do this.

      ````
      vi /u01/app/oracle/homes/OraDB21000_home1/network/admin/tnsnames.ora
      ````
5. Do the same operation for each new PDB created in the CDB.

6. Test the connection to CDB21.  Connect to CDB21 with SQL*Plus.
   
      ````
      sqlplus sys@CDB21_iad1bw AS SYSDBA
      ````

7. Verify that the container name is CDB$ROOT.
      ````
      SHOW CON_NAME;
      ````

8. Test the connection to PDB21
   
      ````
      CONNECT sys@PDB21 AS SYSDBA
      ````

9.  Show the container name
    
      ````
      SHOW CON_NAME;
      ````
10. Exit SQL*Plus
    
      ````
      exit
      ````

## **STEP 2**: Download scripts
Download the Cloud\_Preview\_21c\_labs.zip file to the /home/oracle directory on your VM and unzip the file.

1.  Change to the oracle user home directory
   
      ````
      cd /home/oracle
      ````
2.  Unzip Cloud\_Preview\_21c\_labs.zip

      ````
      unzip Cloud_Preview_21c_labs.zip
      ````

## **STEP 3**: Update the scripts to the current environment

Execute the /home/oracle/labs/update\_pass.sh shell script. The shell script prompts you to enter the password\_defined\_during\_DBSystem\_creation and sets it in all shell scripts and SQL scripts that will be used in the practices.
1. Make the script readable, writable, and executable by everyone.

      ````
      <copy>
      chmod 777 /home/oracle/labs/update_pass.sh
      </copy>
      ````

2. Run the script.

      ````
      <copy>
      /home/oracle/labs/update_pass.sh
      </copy>
      ````

You may now [proceed to the next lab](#next).

## Learn More

* [URL text 1](http://docs.oracle.com)
* [URL text 2](http://docs.oracle.com)

## Acknowledgements
* **Author** - Dominique Jeunot, Database UA Team
* **Contributors** -  Kay Malcolm, Database Product Management
* **Last Updated By/Date** -  Kay Malcolm, Database Product Management

## Need Help?
Please submit feedback or ask for help using our [LiveLabs Support Forum](https://community.oracle.com/tech/developers/categories/livelabsdiscussions). Please click the **Log In** button and login using your Oracle Account. Click the **Ask A Question** button to the left to start a *New Discussion* or *Ask a Question*.  Please include your workshop name and lab name.  You can also include screenshots and attach files.  Engage directly with the author of the workshop.

If you do not have an Oracle Account, click [here](https://profile.oracle.com/myprofile/account/create-account.jspx) to create one.
