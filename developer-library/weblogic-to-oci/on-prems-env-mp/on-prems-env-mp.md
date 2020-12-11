# Setup an 'On-Premises' Environment Using the Workshop Image.

## Introduction

This lab walks you through setting up an environment to simulate an established on-premises environment, using a Compute instance on OCI deployed through the marketplace.

At the end of this lab, you will have a simulated 'on-premises' environment running with an Oracle 12c Database and WebLogic Server 12c with a domain containing 2 applications and a datasource.

Estimated Lab Time: 15 minutes

### Objectives

In this lab you will:

- Launch a demo Marketplace image
- Check that the services are up and running
- Log into the instance
- Create a SSH key pair

### Prerequisites

For this lab you need:

- A compute instance with 4 OCPUs available to run the image.

## **STEP 1:** Launch the workshop marketplace stack

- Navigate to [Workshop Environment Marketplace Stack](https://cloudmarketplace.oracle.com/marketplace/listing/82173888)

1. Click **Get App**

  <img src="../../../on-prems-env-mp/images/get-app.png"  width="100%">

2. Sign in to your Oracle Cloud Infrastructure Account

  <img src="../../../on-prems-env-mp/images/sign-in.png"  width="50%">

3. Choose a compartment

  <img src="../../../on-prems-env-mp/images/wls-workshop-mp1.png"  width="100%">

4. Accept the Terms and Conditions and click **Launch**

  <img src="../../../on-prems-env-mp/images/wls-workshop-mp2.png"  width="100%">

5. Click **Next**

  <img src="../../../on-prems-env-mp/images/next.png"  width="70%">

6. Paste your **SSH public key**

   To connect to the WebLogic servers via SSH, you need to provide a public key the server will use to identify your computer.

  <img src="../../../on-prems-env-mp/images/ssh-key.png"  width="50%">

7. Click **Next** and then **Create**

  <img src="../../../on-prems-env-mp/images/job-running.png"  width="100%">

  It will take about 1 to 2 minutes to create the stack.

8. When the job finishes, you can find the Public IP address of the instance at the bottom of the logs, or in the **Output** area. Make a note of this information.

  <img src="../../../on-prems-env-mp/images/job-output.png"  width="100%">

## **STEP 2:**  Check the local environment is up and running

*It will take another 4 to 5 minutes for all the services to come online.*

1. The console will be available at `http://PUBLIC-IP:7001/console` (replace `PUBLIC_IP` with the Compute instance public IP) and the WebLogic admin user is `weblogic` with password `welcome1`

  <img src="../../../on-prems-env-mp/images/localhost-admin-console.png"  width="100%">

2. The **SimpleDB** application will be running at `http://PUBLIC-IP:7003/SimpleDB/` (substitute `PUBLIC-IP` with the public IP of the instance). It may take a minute or 2 after the admin console is up for the SimpleDB app to be running.

3. It shows statistics of riders of the Tour de France stored in the database, and looks like this:

  ![](./images/localhost-simpledb-app.png)

You may proceed to next steps while the environment is coming up, but make sure it is up before proceeding to the next lab.

## **STEP 3:** Log in to the 'On-premises' environment

*Most of the work will be done from the simulated on-premises environment deployed in the compute instance on OCI.*

1. To log into the instance, use:

    ```bash
    ssh opc@<public-ip>
    ```
    Replace the `<public-ip>` with the IP provided in the output of the provisioning job.

2. You will be prompted to add this IP to the list of known hosts. Enter `yes`

## **STEP 4:** Create a SSH key

*We'll need a SSH key pair to communicate with the WebLogic servers and the database on OCI. The public key will need to be provided when provisioning those resources.*

We'll create a SSH key pair in the default folder

1. Once on the compute instance on OCI, switch to the oracle user:

    ```bash
    <copy>
    sudo su - oracle
    </copy>
    ```

2. Create the SSH keypair

    ```bash
    <copy>
    ssh-keygen
    </copy>
    ```
    and just hit `Enter` (default) for all the prompts

3. You will find two files `id_rsa` and `id_rsa.pub` inside the folder `~/.ssh/` or `/home/oracle/.ssh/`

    `id_rsa` is the private key, which should never be shared, and will be required to connect to any OCI resource provisioned with the corresponding public key `id_rsa.pub`

    Note this key will be the default SSH key from the instance used for the on-premises environment.

    **Note:** This is only to be done once. If you run it again, a new key will overwrite the previous one and you will lose access to any resource provisioned with that key.

You may proceed to the next lab.

## Acknowledgements

 - **Author** - Emmanuel Leroy, May 2020
 - **Last Updated By/Date** - Emmanuel Leroy, August 2020

## Need Help?
Please submit feedback or ask for help using our [LiveLabs Support Forum](https://community.oracle.com/tech/developers/categories/Weblogic). Please click the **Log In** button and login using your Oracle Account. Click the **Ask A Question** button to the left to start a *New Discussion* or *Ask a Question*.  Please include your workshop name and lab name.  You can also include screenshots and attach files.  Engage directly with the author of the workshop.

If you do not have an Oracle Account, click [here](https://profile.oracle.com/myprofile/account/create-account.jspx) to create one.
