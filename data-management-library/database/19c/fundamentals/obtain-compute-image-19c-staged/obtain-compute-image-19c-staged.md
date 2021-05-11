# Obtain a Compute Image with Staged Oracle Database 19c Installer Files

## Introduction
In this lab, you use Resource Manager in Oracle Cloud Infrastructure (OCI) to quickly create a compute instance that has the Oracle Database 19c installer files staged on it. This lab creates the environment that you will use in the [Install ORacle Database 19c using Automatic Root Script Execution](?lab="install-db19c-auto-config-script-execution.md") lab

In Resource Manager, you begin by creating a stack, which is a collection of Oracle Cloud Infrastructure resources corresponding to a given Terraform configuration. A Terraform configuration is a set of one or more TF files written in HashiCorp Configuration Language (HCL) that specify the Oracle Cloud Infrastructure resources to create. The Terraform configuration that you use in this lab is provided by LiveLabs and loads a custom image stored in Oracle Cloud Marketplace. Guacomole is installed on the image to provide a friendly user interface. You can also access a terminal window on the image. After you create the stack, you apply it to start the provisioning job in OCI. When the job is completed, you log in to your compute instance through a browser.

*If you are working in the LiveLabs tenancy, you can skip STEP 1 because it has already been done for you.*

Estimated Lab Time: 30 minutes

### Objectives

In this lab, you learn how to do the following:

- Create and apply a stack in Resource Manager
- Obtain the public IP address of your compute instance
- Connect to your compute instance from a browser
- Enable copying and pasting from your local computer to your Guacamole desktop
- Connect to your compute instance from Cloud Shell

### Prerequisites

- You have an Oracle account. You can obtain a free account by using Oracle Free Tier or you can use a paid account provided to you by your own organization.
- You have created SSH keys.

### Assumptions

- You are signed in to Oracle Cloud Infrastructure.

## **STEP 1**: Create and apply a stack in Resource Manager

*If you are working in the LiveLabs tenancy, you can skip this step and proceed to STEP 2*.

1. Download [livelabs-db19installed-0421.zip](https://apexapps-stage.oracle.com/pls/apex/dbpm/r/livelabs/view-workshop?wid=667) to a directory on your local computer. This ZIP file contains the terraform script.

2. On the home page in Oracle Cloud Infrastructure, click **Create a stack**. The **Create Stack** page is displayed. The **Create Stack** page is displayed.

  ![Create a stack tile on the home page](images/create-a-stack.png)

3. For **Stack Information**, do the following:

  a) Select **My Configuration**.

  b) In the **Stack Configuration** area, select **.ZIP file**, click **Browse**, select the ZIP file that you just downloaded, and then click **Open**.

  c) Scroll down, and in the **NAME** box, enter a name for the stack, for example, **livelabs19cstaged**.

  ![Stack Information](images/stack-information-page.png)

  d) Click **Next**.

4. For **Configure Variables**, do the following:

  a) Leave **Region** as is.

  b) Select the compartment in which you want to create the compute instance.

  c) Select an availability domain.

  d) Select **Paste SSH Key**, and paste the contents of your public key into the box.

  e) Leave **VMStandard.E2.4** selected as the instance shape. This shape meets the memory requirements for installing Oracle Database 19c.

  f) Leave the network settings as is.

  ![Configure Variables](images/configure-variables-page.png)

  g) Click **Next**.

5. On the **Review** page, verify that the information is correct.

  ![Review page](images/review-page.png)

6. Click **Create**. Your stack is created and the **Stack Details** page is displayed.

  ![Stack Details page](images/stack-details-page.png)

6. From the **Terraform Actions** drop-down, select **Apply**. The **Apply** window is displayed.

7. In the **Apply** window, leave the name as is and the **APPLY JOB PLAN RESOLUTION** set to **Automatically approve**, and click **Apply**. Resource Manager starts a job to deploy your resources.

  ![Apply window](images/apply-window.png)

8. When the job is finished, inspect the log. The last line should read `Apply complete!`.


## **STEP 2**: Obtain the public IP address of your compute instance

1. From the navigation menu in the Oracle Cloud Infrastructure Console, select **Compute**, and then **Instances**.

2. Select your compartment.

3. Find the public IP address of the compute instance called **workshop-staged** in the table and jot it down.

4. (Optional) Click the **workshop-staged** compute instance to view all of its details.


## **STEP 3**: Connect to your compute instance via a browser

1. On your local computer, open a browser, and enter the following url. Replace `compute-public-ip` with the public IP address of your compute instance.

    ```nohighlighting
    <copy>compute-public-ip:8080/guacamole</copy>
    ```

2. Enter `oracle` as the username and `Guac.LiveLabs_` as the password, and then click Login. Don't forget the underscore at the end of the password!
    (guacamole-login-page.png)

   You are presented with a Guacamole desktop. The desktop provides shortcuts to Firefox and a terminal window.


## **STEP 4**: Enable copying and pasting from your local computer to your Guacamole desktop
During your labs you may need to copy text from your local PC or Mac to the remote Guacamole desktop. For example, you may want to copy commands from the lab guide and paste them into the terminal window. While such direct copying and pasting isn't supported on the Guacamole desktop, you can enable an alternative local-to-remote clipboard by using the Input Text field.

1. On your compute instance, enter **CTRL+ALT+SHIFT** (Windows) or **CTRL+CMD+SHIFT** (Mac).

2. Select **Text Input**.

  A black Text Input field is added to the bottom of your screen. In this field, you can paste any text copied from your local environment.

  ![](./images/guacamole-clipboard-2.png " ")

3. Test copy and pasting the following text. Prior to pasting, ensure that the cursor is placed at the location where you want to paste the text, then right-click inside the black **Text Input** field, and paste the text.

    ```nohighlighting
    <copy>echo "This text was copied from my local desktop on to my remote session"</copy>
    ```
    ![](./images/guacamole-clipboard-3.png " ")


## **STEP 5**: Connect to your compute instance via Cloud Shell

1. On the toolbar in Oracle Cloud Infrastructure, click the Cloud Shell icon to launch Cloud Shell.

  ![Cloud Shell icon](images/cloud-shell-icon.png)

  A terminal window opens at the bottom of the page.

2. Enter the following `ssh` command to connect to your compute instance. Replace `public-ip-address` with the public IP address of your compute instance.

  `cloudshellkey` is the name of the private key file that you created in the [Generate SSH Keys - Cloud Shell](?lab=https://raw.githubusercontent.com/oracle/learning-library/master/common/labs/generate-ssh-key-cloud-shell/generate-ssh-keys-cloud-shell.md) lab. If your private key has a different name, then replace `cloudshellkey` with it.

    ```nohighlighting
    $ <copy>ssh -i ~/.ssh/cloudshellkey opc@public-ip-address</copy>
    ```

    A message states that the authenticity of your compute instance can't be established. Do you want to continue connecting?

3. Enter **yes** to continue. The public IP address of your compute instance is added to the list of known hosts on your Cloud Shell machine.

  You are now connected to your new compute instance via Cloud Shell.


You may now [proceed to the next lab](#next).

## Learn More

- [Resource Manager](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Concepts/landing.htm#ResourceManager)
- [Video about Resource Manager](https://youtu.be/udJdVCz5HYs)
- [Oracle Cloud Marketplace](https://cloudmarketplace.oracle.com/marketplace/en_US/homePage.jspx)

## Acknowledgements

- **Author**- Jody Glover, Principal User Assistance Developer, Database Development
- **Last Updated By/Date** - Jody Glover, Database team, April 21 2021
