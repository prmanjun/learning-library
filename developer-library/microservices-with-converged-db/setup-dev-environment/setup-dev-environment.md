# Setup OCI, OKE, ATP and Cloud shell
## Introduction

This 25-minute lab will show you how to set up the Oracle Cloud Infrastructure (OCI) Container Engine for Kubernetes (OKE) for creating and deploying a front-end Helidon application which accesses the backend Oracle Autonomous Database (ATP).

### Objectives

* Collect important information that you will use throughout this workshop
* Set up the OKE cluster
* Set up the ATP databases

### What Do You Need?

* An Oracle Cloud paid account or free trial with credits. To sign up for a trial account with $300 in credits for 30 days, click [here](http://oracle.com/cloud/free).

 You will not be able to complete this workshop with the 'Always Free' account. Make sure that you select the free trial account with credits.

## **STEP 1**: Launch the Cloud Shell

Cloud Shell is a small virtual machine running a Bash shell which you access through the OCI Console. Cloud Shell comes with a pre-authenticated CLI which is set to the OCI Console tenancy home page region. It also provides up-to-date tools and utilities.

Click the Cloud Shell icon in the top-right corner of the Console.

Just responded in email as well

## **STEP 2**: Make a clone of the workshop source code
1. To work with application code, you need to make a clone from the GitHub repository using the following command. The workshop assumes this is done from your root directory.

    ```
    <copy>cd ~ ; git clone https://github.com/oracle/microservices-datadriven.git</copy>
    ```

  You should now see `microservices-datadriven` in your root directory


2. Change directory into the cd microservices-datadriven/grabdish directory:

    ```
    <copy>cd ~/microservices-datadriven/grabdish</copy>
    ```
   
   NOTE: THE CLOUD SHELL WILL DISCONNECT AFTER A CERTAIN PERIOD OF INACTIVITY. 
   
   IF YOU ARE DISCONNECTED OR LOG OFF AND RETURN TO CLOUD SHELL, MAKE SURE YOU ARE IN THE `~/microservices-datadriven/grabdish` DIRECTORY.
  
   

## **STEP 3**: Create an OCI compartment and an OKE cluster in that compartment

1. Open up the hamburger menu in the top-left corner of the Console and select **Identity > Compartments**.

   ![](images/15-identity-compartments.png " ")

2. Click **Create Compartment** with the following parameters and click **Create Compartment**:
    - Compartment name: `msdataworkshop`
    - Description: `MS workshop compartment`

    ![](images/16-create-compartment.png " ")

    ![](images/17-create-compartment2.png " ")

3. Once the compartment is created, click the name of the compartment and then click **Copy** to copy the OCID.

    ![](images/19-compartment-name-ocid.png " ")

    ![](images/20-compartment-ocid.png " ")

4. Go back into your cloud shell and verify you are in the `~/microservices-datadriven/grabdish` directory.

5. Run `./setCompartmentId.sh <COMPARTMENT_OCID> <REGION_ID>` where your `<COMPARTMENT_OCID>` and `<REGION_ID>` values are set as arguments.

  For example:

   `./setCompartmentId.sh ocid1.compartment.oc1..aaaaaaaaxbvaatfz6yourcomparmentidhere us-ashburn-1`

5.  To create an OKE cluster, return to the OCI console and open up the hamburger button in the top-left
        corner of the Console and go to **Developer Services > Kubernetes Clusters**.

      ![](images/27-dev-services-oke.png " ")

6. Make sure you are in the newly created compartment and click **Create Cluster**.

      ![](images/28-create-oke.png " ")

7. Choose **Quick Create** as it will create the new cluster along with the new network
    resources such as Virtual Cloud Network (VCN), Internet Gateway (IG), NAT
    Gateway (NAT), Regional Subnet for worker nodes, and a Regional Subnet for load
    balancers. Click **Launch Workflow**.

      ![](images/29-create-oke-wizard.png " ")


8. Change the name of the cluster to `msdataworkshopcluster`, accept all the other defaults, and click **Next** to review the cluster settings.


9. Once reviewed click **Create Cluster**, and you will see the resource creation progress.

      ![](images/31-create-oke-wizard3.png " ")

10. Close the creation window.

      ![](images/32-close-cluster-create.png " ")

11. Once launched it should usually take just a few minutes for the cluster to be
    fully provisioned and the Cluster Status should show Active.

      ![](images/33-click-cluster-name.png " ")

      ![](images/34-copy-cluster-id.png " ")

    Click on the link for the cluster you've just created to see the detail page.
    
      ![](images/clusterdetailpage.png " ")

    Click the **Access Cluster** button.
    
      ![](images/accessyourclustercopylink.png " ")

    Click on the link to copy the oci command.
    
      ![](images/kubeconfigcreateoutput.png " ")

    Return the Cloud Shell, paste and run the command to add the ~/.kube/config needed to access the kubernetes cluster.
    
      ![](images/kubeconfigcommandline.png " ")

## **STEP 4**: Create OCI Vault Secrets for the ATP PDB users and FrontEnd microservice authentication

1. Open up the hamburger menu in the top-left corner of the Console and select **Security > Vault**.

     ![](images/vaultmenu.png " ")
     
2. Click **Create Vault** , specify a name and click **Create**.

   ![](images/masterencryptionkeys.png " ")
   
   Click the link for the vault you just created.
   
   COPY THE OCID FOR THE VAULT AND NOTE IT FOR LATER USE.
 
3. Click **Master Encryption Key** , click **Create Key**, enter a name, and click **Create Key**
   
      ![](images/createmasterencryptionkey.png " ")
        
4. Decide upon a password to be used for all database users that follows the Oracle requirements found here (eg `Welcome12345`: https://docs.oracle.com/en/database/oracle/oracle-database/19/dbseg/keeping-your-oracle-database-secure.html#GUID-451679EB-8676-47E6-82A6-DF025FD65156 

5. Click **Secrets** , click **Create Secret**, enter a name, description, encryption key (created in previous step), leave the default **Plain-Text** Secret Type Template, and provide the DB password (in the **Secret Contents** field) for the database users you will create later and click **Create Secret**
   
      ![](images/createsecret.png " ")
      
   COPY THE OCID OF THIS DB PASSWORD SECRET AND NOTE IT FOR LATER USE.
        
6. Repeat the process to create a secret for the FrontEnd microservice authentication
   
     ![](images/createfrontendauthpwsecret.png " ")
        
   COPY THE OCID OF THIS FRONTEND MICROSERVICE AUTH PASSWORD SECRET AND NOTE IT FOR LATER USE.
   
7. Open up the hamburger menu in the top-left corner of the Console and select **Identity > Dynamic Groups**.

     ![](images/dynamicgroupmenu.png " ")

8. Click **Create Dynamic Group** , specify a name, add the following matching rule providing your compartment ocid

     `All {instance.compartment.id = 'ocid1.compartment.oc1..aaaaaaaaaaaputyourcompartmentidhere'}`
     
     and click **Create**.

     ![](images/createdynamicgroup.png " ")
     
9. Open up the hamburger menu in the top-left corner of the Console and select **Identity > Policies**:

     ![](images/policymenu.png " ")
     
10. Click **Create Policy** specify a name and the following matching rule providing your compartment and vault ocids
   
   `Allow dynamic-group yourdynamicgroupname to manage secret-family in compartment id ocid1.compartment.oc1..yourcompartmentid where target.vault.id = 'ocid1.vault.oc1.phx.yourvaultid'`
  
     ![](images/createpolicy.png " ")
     
    and click **Create**
     

## **STEP 5**: Create ATP databases

  Run the `createATPPDBs.sh` script providing the Vault Secret ocids (created and noted in **Step 4**) for the DB users followed by the ocid for the FrontEnd microservice user

  ```
  <copy>./createATPPDBs.sh <REPLACE WITH VAULT SECRET OCID FOR DB USER> <REPLACE WITH VAULT SECRET OCID FOR FRONTEND USER AUTH></copy>
  ```

   Notice creation of the ORDERDB and INVENTORYDB PDBs and Frontend Auth secret.

   ![](images/createpdboutput1.png " ")

   ![](images/createpdboutput2.png " ")

   _OCIDs for the PDBs are stored and will be used later to create kubernetes secrets that microservices will use to access them._


## **STEP 5**: Create an OCI Registry and Auth key and login to it from Cloud Shell
You are now going to create an Oracle Cloud Infrastructure Registry and an Auth key. Oracle Cloud Infrastructure Registry is an Oracle-managed registry that enables you to simplify your development-to-production workflow by storing, sharing, and managing development artifacts such as Docker images.

1. Open up the hamburger menu in the top-left corner of the console and go to **Developer Services > Container Registry**.

  ![](images/21-dev-services-registry.png " ")

2. Take note of the namespace (for example, `axkcsk2aiatb` shown in the image below).  Click **Create Repository** , specify the following details for your new repository, and click **Create Repository**.
    - Repository Name: `<firstname.lastname>/msdataworkshop`
	- Access: `Public`

  Make sure that access is marked as `Public`.  

  ![](images/22-create-repo.png " ")

  ![](images/22-create-repo2.png " ")

  Go to Cloud Shell and run `./addOCIRInfo.sh` with the namespace and repository name as arguments

  ```
  <copy>./addOCIRInfo.sh <namespace> <repository_name></copy>
  ```

  For example `./addOCIRInfo.sh axkcsk2aiatb msdataworkshop.user1/msdataworkshop`

3. You will now create the Auth token by going back to the User Settings page. Click the Profile icon in the top-right corner of the Console and select **User Settings**.

  ![](images/23-user-settings.png " ")

4. Click on **Auth Tokens** and select **Generate Token**.

  ![](images/24-gen-auth-token.png " ")

5. In the description type `msdataworkshoptoken` and click **Generate Token**.

  ![](images/25-gen-auth-token2.png " ")

6. Copy the token value.

  ![](images/26-save-auth-token.png " ")

7. Go to Cloud Shell and run `./dockerLogin.sh <USERNAME> "<AUTH_TOKEN>"` where `<USERNAME>` and `"<AUTH_TOKEN>"` values are set as arguments.

  * `<USERNAME>` - is the username used to log in (typically your email address). If your username is federated from Oracle Identity Cloud Service, you need to add the `oracleidentitycloudservice/` prefix to your username, for example `oracleidentitycloudservice/firstname.lastname@something.com`
  * `"<AUTH_TOKEN>"` - paste the generated token value and enclose the value in quotes.

  For example `./dockerLogin.sh user.foo@bar.com "8nO[BKNU5iwasdf2xeefU;yl"`


8. Once successfully logged into Container Registry, we can list the existing docker images. Since this is the first time logging into Registry, no images will be shown.

    ```
    <copy>docker images </copy>
    ```


## **STEP 6**: Install GraalVM, Jaeger, and Frontend Loadbalancer
Run the `installGraalVMJaegerAndFrontendLB.sh` script to install both GraalVM and Jaeger.

 ```
 <copy>cd ~/microservices-datadriven/grabdish; ./installGraalVMJaegerAndFrontendLB.sh</copy>
 ```

You may now proceed to the next lab.

## Acknowledgements

* **Author** - Paul Parkinson, Dev Lead for Data and Transaction Processing, Oracle Microservices Platform, Helidon
* **Adapted for Cloud by** - Nenad Jovicic, Enterprise Strategist, North America Technology Enterprise Architect Solution Engineering Team
* **Documentation** - Lisa Jamen, User Assistance Developer - Helidon
* **Contributors** - Jaden McElvey, Technical Lead - Oracle LiveLabs Intern
* **Last Updated By/Date** - Tom McGinn, June 2020


