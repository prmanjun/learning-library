# Setup the Environment (lab in Development)

## Introduction
In the previous lab you created an ADB instance. In this lab you will connect to the ADB instance from Oracle Cloud Shell.

*Estimated time:* 20 Minutes

### Objectives
- Create a bucket, auth token and Oracle Wallet
- Create a Database Credential for the Users

### Prerequisites
- Lab: Provision ADB

## **STEP 1:** Create a Bucket

1. Login to Oracle Cloud if you are not already logged in.

2. Click on the hamburger menu and navigate to Object Storage and click on **Object Storage**.

3. Choose the compartment where your ATP is provisioned and click **Create Bucket**.

4. Name your bucket atp1 and click create.

5. Once the bucket is created, click on the bucket and make note of the bucket name and namespace.

## **STEP 2:** Create Oracle Wallet in Cloud Shell

There are multiple ways to create an Oracle Wallet for ADB.  We will be using Oracle Cloud Shell as this is not the focus of this workshop.  To learn more about Oracle Wallets and use the interface to create one, please refer to the lab in this workshop: [Analyzing Your Data with ADB - Lab 6](https://apexapps.oracle.com/pls/apex/dbpm/r/livelabs/view-workshop?p180_id=553)

1.  Login to the Oracle Cloud if you aren't logged in already.
   
2.  Click the Cloud Shell icon to start up Cloud Shell
      ![](./images/cloud-shell.png " ")
3.  While your Cloud Shell is starting up, click on the Hamburger Menu -> **Autonomous Transaction Processing** 
      ![](https://raw.githubusercontent.com/oracle/learning-library/master/common/images/console/database-atp.png " ")

4.  Click on the **Display Name** to go to your ADB main page.
   
5.  Locate the **OCID** (Oracle Cloud ID) you will need that in a few minutes. 

      ![](./images/locate-ocid.png " ")

6.  Use your autonomous\_database\_ocid to create the Oracle Wallet. You will be setting the wallet password to the same value as the ADB admin password for ease of use: *WElcome123##* Note: This is not a recommended practice and just used for the purposes of this lab. 
7.  Copy the command below and paste it into Cloud Shell.  Do not hit enter yet.  

      ````
      <copy>
      cd ~
      oci db autonomous-database generate-wallet --password WElcome123## --file 21c-wallet.zip --autonomous-database-id  </copy> ocid1.autonomousdatabase.oc1.iad.xxxxxxxxxxxxxxxxxxxxxx
      ````

      ![](./images/wallet.png " ")

8.  Press copy to copy the OCID from Step 5 and fill in the autonomous database ocid that is listed in the output section of your terraform.  Make sure there is a space between the --autonomous-database-id phrase and the ocid.  Click **enter**.  Be patient, it takes about 20 seconds.

9.  The wallet file will be downloaded to your cloud shell file system in /home/yourtenancyname

10. Enter the list command in your cloud shell below to verify the *21c-wallet.zip* was created
   
      ````
      ls
      ````
      ![](./images/21cwallet.png " ")

## **STEP 3:** Create Auth Token

1.  Click on the person icon in the upper right corner.
2.  Select **User Settings**
      ![](./images/select-user.png " ")
3.  Copy the username.
4.  Under the **User Information** tab, click the **Copy** button to copy your User OCID.
      ![](./images/copy-user-ocid.png " ")

5.  Create your auth token with description `atp1` using the command below by substituting your actual *user OCID* for the userid below.  *Note: If you already have an auth token, you may get an error if you try to create more than 2 per user*
   
      ````
      <copy>
       oci iam auth-token create --description adb1 --user-id </copy> ocid1.user.oc1..axxxxxxxxxxxxxxxxxxxxxx
      ````
      ![](./images/token.png " ")

6.  Identify the line in the output that starts with "token".
7.  Copy the value for the token somewhere safe, you will need it for the next step.

## **STEP 4:** Connect to ADB with SQL Developer Web

Please proceed to next step if you are already connected to Autonomous Database with SQL Developer Web as a ADMIN user.

1. To navigate to your Autonomous Database, click on the hamburger menu on the top left corner of the Oracle Cloud console and select your Autonomous Database you provisioned.

2. If you can't find your ADB instance, ensure you are in the correct region, compartment and have chosen the right flavor of your ADB instance.

3. Click on the Display Name of your ADB instance to navigate to your ADB instance details page.

4. Click on the **Tools** tab, select **Database Actions**, a new tab will open up.

5. Provide the **Username - ADMIN** and click **Next**.

6. Now provide the **Password - WElcome123##** for the ADMIN user you created when you provisioned your ADB instance and click **Sign in** to sign in to Database Actions.

7. Click on **SQL** under the Development section to sign in to SQL Developer Web as an ADMIN user.

## **STEP 5:** Create a Database Credential for Your Users

To access data in the Object Store you have to enable your database user to authenticate itself with the Object Store using your OCI object store account and Auth token. You do this by creating a private CREDENTIAL object for your user that stores this information encrypted in your Autonomous Transaction Processing. This information is only usable for your user schema.

1. Copy and paste this the code snippet in to SQL Developer worksheet. Specify the credentials for your Oracle Cloud Infrastructure Object Storage service by replacing the `<username>` and `<token>` with the following username and password:

	- Credential name: Description of the auth token. In this example, the auth token is created with the description - `atp1` in step 3
	- Username: The username will be the OCI Username you noted in step 3
	- Password: The password will be the OCI Object Store Auth Token you generated in step 3.

	```
	<copy>
	BEGIN
  		DBMS_CLOUD.CREATE_CREDENTIAL(
    		credential_name => 'atp1',
    		username => '<username>',
    		password => '<token>'
  		);
	END;
	/
	</copy>
	```

    Now you are ready to load data from the Object Store.

You may now [proceed to the next lab](#next).

## Acknowledgements
* **Authors** - Anoosha Pilli
* **Contributors** - Anoosha Pilli, Didi Han, Database Product Management
* **Last Updated By/Date** - Didi Han, April 2021