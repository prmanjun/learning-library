# Lab 7: Teardown

## Introduction

In this 20-minute lab we will provision and setup the resources in your tenancy to install and execute microservices.  will show you how to set up the Oracle Cloud Infrastructure (OCI) Container Engine for Kubernetes (OKE) for creating and deploying a front-end Helidon application which accesses the backend Oracle Autonomous Database (ATP).

### Objectives

* Clone the setup and microservices code
* Execute the setup

## **STEP 1**: Delete the Workshop Resources

Run the following command to delete the resources created in you tenancy.  It will delete everything except the compartment.  It will take several minutes to run.  The script will delete the Object Storage bucket, OCI Registry repositories, OKE cluster, listeners, VCN and databases.

    ```
    <copy>source destroy.sh</copy>
    ```

## **STEP 2**: Delete the Directory

Delete the directory in your cloud shell where you installed the workshop.

    ```
    <copy>rm -rf <directory name></copy>
    ```

## **STEP 3**: Delete the Compartment

In the OCI console navigate to the Identity -> Compartments screen.  Select the compartment that was created for the workshop and delete it.  Note, even when the script in step 1 has completed, it can take some time for OCI to fully remove all the resources.  It will not be possible to delete the compartment until this has completed.

## Acknowledgements

* **Author** - Richard Exley, Consulting Member of Technical Staff, Oracle MAA and Exadata
* **Adapted for Cloud by** - Nenad Jovicic, Enterprise Strategist, North America Technology Enterprise Architect Solution Engineering Team
* **Documentation** - Lisa Jamen, User Assistance Developer - Helidon
* **Contributors** - Jaden McElvey, Technical Lead - Oracle LiveLabs Intern
* **Last Updated By/Date** - Tom McGinn, June 2020


