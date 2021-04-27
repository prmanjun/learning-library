
# Install Oracle Database 19c with Automatic Configuration Script Execution

## Introduction

Certain operations must be performed by the `root` user when you install and configure an Oracle database. Starting with Oracle Database 19c, the Oracle Universal Installer includes an option to run configuration scripts automatically for you as the `root` user. Setting up permissions for configuration scripts to run without user intervention can simplify database installation and help avoid inadvertent permission errors. If you prefer, you can still choose to run the scripts manually, like you would do for an Oracle Database 18c installation.

This lab shows you how to install Oracle Database 19c with the new option to run configuration scripts automatically. You also examine the response file and resulting container database (CDB) and pluggable database (PDB).


Estimated Lab Time: 15 minutes

### Objectives

In this lab, you'll:

- Create users and groups in the Linux operating system
- Create the Oracle base and Oracle inventory directories
- Download the Oracle Database installation image files to a stage directory
- Create an OFA-compliant Oracle home directory and extract the image files into that directory
- Install the database software by using the Oracle Database Setup Wizard
- Review the response file
- Discover the container database (CDB) and pluggable database (PDB)
- Uninstall Oracle Database 19c (optional)

### Prerequisites

To complete this lab, you need to have the following:

- Access to www.oracle.com so that you can download the Oracle Database 19c installation software
- Access to the `root` user on your Linux operating system

### Assumptions

- You are using an Linux operating system.

## **STEP 1**: Create users and groups in the Linux operating system

You need to create an Oracle installation user account (`oracle`) that will own the installation software binaries.

1. At a terminal prompt, switch to the `root` user. You are prompted to enter a password.

    ```nohighlighting
    # <copy>su -</copy>
    ```
2. Create a `dba` group, `oinstall` group, and an `oracle` user account. Add `oracle` to both the `oinstall` and `dba` groups.

    ```nohighlighting
    # <copy>groupadd dba</copy>
    # <copy>groupadd oinstall</copy>
    # <copy>useradd -m -g oinstall -G dba oracle</copy>
    ```

3. Set the password for the `oracle` user. You are prompted to enter and confirm a password.

    ```nohighlighting
    # <copy>passwd oracle</copy>
    ```


## **STEP 2**: Create the Oracle base and Oracle inventory directories

Still as the `root` user, create two directories as per the Oracle Optimal Flexible Architecture (OFA) recommendations in preparation for the installation: **Oracle base** and **Oracle inventory**. Also specify the correct owner, group, and permissions for these directories. All files in Linux belong to an owner and a group.

1. Create the **Oracle base** directory.

    ````
    # <copy>mkdir -p /u01/app/oracle</copy>
    ````

2. Create the **Oracle inventory** directory.

    ````
    # <copy>mkdir -p /u01/app/oraInventory</copy>
    ````

3. Specify `oracle` as the owner and `oinstall` as the group for the Oracle base directory.

    ```
    # <copy>chown -R oracle:oinstall /u01/app/oracle</copy>
    ````
4. Specify `oracle` as the owner and `oinstall` as the group for the Oracle inventory directory.

    ````
    # <copy>chown -R oracle:oinstall /u01/app/oraInventory</copy>
    ````

5. Set the permissions on the `/u01/app` directory and all if its subdirectories (which includes the Oracle base and Oracle inventory directories) so that owner and group can read, write, and execute on the directories.

    ````
    # <copy>chmod -R 775 /u01/app</copy>
    ````

6. Quit the `root` session.

    ```
    $ <copy>exit</copy>
    ```


## **STEP 3**: Download the Oracle Database installation image files to a stage directory

The Oracle Database installation image files are packaged in a ZIP file on Oracle's website.

1. Change the current user to `oracle`.

    ```
    $ <copy>su - oracle</copy>
    ```

2. Create a stage directory, for example, `/stage`, to store the installation image file.

    ````
    $ <copy>mkdir -p /stage</copy>
    ````

2. Start the Firefox web browser. The & in the command below starts Firefox in the background.

    ````
    $ <copy>firefox &</copy>
    ````

3. In the browser, access the URL: `https://www.oracle.com/database/technologies/oracle19c-linux-downloads.html`.


4. Click to download the ZIP file named `LINUX.X64_19100000_db_home.zip`, and save the file to the `/stage` directory.

*The file name will most likely be different for 19.10*





## **STEP 4**: Create an OFA-compliant Oracle home directory and extract the image files into that directory

It's important that the Oracle home directory is in compliance with the Oracle Optimal Flexible Architecture recommendations. Make sure the current user is still `oracle`.  

1. Create an **Oracle home** directory.

    ```
    $ <copy>mkdir -p /u01/app/oracle/product/19.10.0/dbhome_1</copy>
    ```

2. Change to the directory that you just created.

    ```
    $ <copy>cd /u01/app/oracle/product/19.10.0/dbhome_1</copy>
    ```

3. Extract the image files into the Oracle home directory.

    ```
    $ <copy>unzip -q /staging/db_home.zip</copy>
    ```




## **STEP 5**: Install the database software by using the Oracle Database Setup Wizard

As the `oracle` user, install Oracle Database 19c using the Oracle Database Setup Wizard. During installation, choose to automatically run the configuration scripts.  

1. Change to the Oracle home directory.

    ```
    $ <copy>cd /u01/app/oracle/product/19.10.0/dbhome_1</copy>
    ```
2. Run the `runInstaller` command to start the Oracle Database Setup Wizard. It's important that you run the `runInstaller` command from the Oracle home directory only.

    ```
    <copy>./runInstaller</copy>
    ```

3. On the **Select Configuration Option** page, select **Create and configure a single instance database**. This option creates a starter database with one container database (CDB) and one pluggable database (PDB).

4. On the **Select System Class** page, select **Desktop Class**, and then click **Next**.

5. On the **Select Database Edition** page, select **Standard Edition 2**, and click **Next**.

REVIEWER: You could select Enterprise Edition instead?

6. On the **Specify Installation Location** page, leave the default Oracle base path as is (`/u01/app/oracle`), and click **Next**.

7. On the **Create Inventory** page, leave the default Inventory Directory path as is (`/u01/app/orainventory`), and click **Next**.

8. On the **Select Configuration Type** page, leave **General Purpose / Transaction Processing** selected as the type of database that you want to create, and click **Next**.

9. On the **Database Identifiers** page, set the default values as follows, and then click **Next**:

    - Global database name: **ORCL.localdomain**
    - Oracle system identifier (SID): **ORCL**
    - Create as Container database (selected)
    - Pluggable database name **PDB1**

10. On the **Specify Configuration Options** page, leave the following default settings as is, and then click **Next**:

    - Automatic Memory Management is not enabled.
    - The character set is set to **Unicode (AL32UTF8)**.
    - The sample schemas are not to be installed.

11. On the **Database Storage** page, leave the default file system path (`u01/app/oracle/oradata`) as is, and then click **Next**.

12. On the **Management Options** page, click the **Next** button. This page is for registering with Enterprise Manager (EM) Cloud Control.

13. On the **Recovery Options** page, click the **Enable Recovery** check box. Leave the default recovery area location (`/u01/app/oracle/recovery_area`) as is, and then click **Next**.

14. On the **Schema Passwords** page, click **Use the same password for all accounts**. Enter a password in the **Password** and **Confirm password** boxes. This password is for the `SYS`, `SYSTEM`, and `PDBADMIN` users. Click **Next**.

15. On the **Operating System Groups** page, set all of the groups (except for the Databse Operator group) to `oinstall`, and then click **Next**.

16. On the **Root script execution** page, select the **Automatically run configuration scripts** check box. Leave **Use "root" user credential** selected, and enter the `root` user's password. Click **Next**.

  *This is the new feature that this lab is all about!*

17. On the **Prerequisite Checks** page, wait for the installer to verify that your environment meets the minimum installation and configuration requirements.

18. On the **Summary** page, save the response file so that you can later review how the configuration scripts get automatically executed:

  a) Click **Save Response File**.  

  b) Select the `/tmp` directory to save the `db.rsp` response file.

  c) Click **Save**.

19. Click **Install** to begin installing the software.

20. On the **Install Product** page, monitor the progress of the steps being executed.

21. When prompted to run the configuration scripts as the privileged user, click **Yes**.

  ![Installation message](images/install-message.png)

22. On the **Finish** page, click **Close**. The installation is finished.




## **STEP 6**: Review the Response File

1. Change to the response file directory.

    ```
    $ <copy>cd /tmp</copy>
    ```
2. Open the response file named `db.rsp` by using the `cat` (concatenate) command. This command reads data from the file and provides the content as output.

    ```
    $ <copy>cat db.rsp</copy>
    ```
3. Review the information.

    ```
    oracle.install.db.rootconfig.executeRootScript=true
    #--------------------------------------------------------------------------------------
    # Specify the configuration method to be used for automatic root script execution.
    #
    # Following are the possible choices:
    #   - ROOT
    #   - SUDO
    #--------------------------------------------------------------------------------------
    oracle.install.db.rootconfig.configMethod=ROOT
    ...
    ```


## **STEP 7**: Discover the container database (CDB) and pluggable database (PDB)

1. Set the Oracle environment variables. You need to set these each time you open a new terminal window.

  a) List the search path that holds the `oraenv` script.

    ```
    $ <copy>which oraenv</copy>

    /usr/local/bin/oraenv
    $
    ```

  b) Source the `oraenv` script. The dot in the command means to do a source operation. `oraenv` sets the required environment variables needed for you to connect to your database instance. For example, it sets the  `ORACLE_SID` and `ORACLE_HOME` environment variables and includes the ``$ORACLE_HOME/bin` directory in the  `PATH` environment variable setting. Environment variables that this script sets will persist in the terminal window until you close it. Don't forget to put a space after the dot. For the `ORACLE_SID` value, enter `ORCL`.

    ```
    $ <copy>. oraenv</copy>

    ORACLE_SID = [oracle] ? ORCL

    The Oracle base has been set to /u01/app/oracle
    $
    ```

2. View the environment variables set by the `oraenv` command that you just ran.

    ```
    $ <copy>set | grep ORACLE</copy>

    OLD_ORACLE_BASE=
    ORACLE_BASE=/u01/app/oracle
    ORACLE_HOME=/u01/app/oracle/product/19.10.0/dbhome_1
    ORACLE_SID=ORCL
    $
    ```


3. Using SQLPlus, connect to the root container of your database. SQL*Plus is an interactive and batch query tool that is installed with every Oracle Database installation.

    ```
    $ <copy>sqlplus / as sysdba</copy>

    SQL*Plus: Release 19.0.0.0.0 - Production on Mon Mar 29 0:9:24:01 2021
    Version 19.10.0.0.0

    Copyright (c) 1982, 2021, Oracle. All rights reserved.

    Connected to:
    Oracle Database 19c Enterprise Edition Release 19.0.0.0.0 - Production
    Version 19.10.0.0.0

    SQL>
    ```

4. Verify that you are logged in to the root container as the `SYS` user by using the `SHOW` user command.
The `SHOW` command is a tool-specific command, and is supported in SQL*Plus, SQL*Developer, and SQLcl. It is not SQL language, does not appear in any SQL Language reference manuals, and is not available to any tool or utility that relies on the SQL Language like Toad or within PL/SQL programs or Java programs. For this example and others that follow, you could use SQL instead of the SHOW command, if desired.

    ```
    SQL> <copy>SHOW user</copy>

    USER is "SYS"
    SQL>
    ```

5. Show the current container name. Because you're currently connected to the root container, the name should be `CDB$ROOT`.

    ```
    SQL> <copy>SHOW con_name</copy>

    CON_NAME
    -------------------
    CDB$ROOT
    SQL>
    ```


6. List all the containers in the CDB by querying the `V$CONTAINERS` view. The results should list three containers - the root container (`CDB$ROOT`), the seed PDB (`PDB$SEED`), and the pluggable database (`PDB1`).

  a) Set the format.

    ```
    SQL> <copy>COLUMN name FORMAT A8</copy>
    ```

  b) Query `V$CONTAINERS`.

    ```
    SQL> <copy>SELECT name, con_id FROM v$containers ORDER BY con_id;</copy>


    NAME         CON_ID
    -------- ----------
    CDB$ROOT          1
    PDB$SEED          2
    PDB1              3
    SQL>
    ```

7. Exit SQL*Plus.

    ```
    $ <copy>EXIT</copy>
    ```



## **STEP 8**: Uninstall Oracle Database 19c (Optional)

If you need to uninstall the database, follow the steps below. If you plan to continue on to the other labs in this workshop, do not uninstall the database.

1. Change to the directory where the Oracle Database 19c software is installed.

    ```
    $ <copy>cd /u01/app/oracle/product/19.0.0/dbhome_2/deinstall</copy>
    ```
2. Launch deinstall.

    ```
    $ <copy>./deinstall</copy>
    ```
3. For the first question, press **Enter** because you did not create a database after the installation.

    ```
    Specify the list of database names that are configured in this Oracle home []:
    ```
4. Specify the Oracle Home path.

    ```
    Oracle Home selected for deinstall is: <copy>/u01/app/oracle/product/19.0.0/dbhome_2</copy>
    ```
5. Enter the inventory location.

    ```
    Inventory Location where the Oracle home registered is: <copy>/u01/app/oraInventory</copy>
    ```
6. Enter **y** to continue.

    ```
    Do you want to continue (y - yes, n - no)? [n]: <copy>y</copy>
    ```
7. Review the [deinstall_output.txt](https://docs.oracle.com/en/database/oracle/oracle-database/19/tutorial-install-oracle-database-with-automatic-root-scripts-execution/files/deinstall_output.txt) file to ensure that the software is uninstalled successfully.

    ```
    Oracle Universal Installer cleanup was successful.
    ...
    Oracle deinstall tool successfully cleaned up temporary directories.
    ############# ORACLE DEINSTALL TOOL END #############
    Quit the session.
    ```
8. Quit the session.

    ```
    $ <copy>exit</copy>
    ```

## Learn More

- [Get Started with Oracle Database 19c](https://docs.oracle.com/en/database/oracle/oracle-database/19/)
- [Install and Upgrade to Oracle Database 19c](https://docs.oracle.com/en/database/oracle/oracle-database/19/install-and-upgrade.html)

## Acknowledgements

- **Author**- Jody Glover, Principal User Assistance Developer, Database Development
- **Last Updated By/Date** - Jody Glover, Database team, March 29 2021
