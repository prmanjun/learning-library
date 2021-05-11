# Install Sample Application in dev

## Introduction

In this lab we will install a sample application in the *`dev`* environment.

Estimated Lab Time: 5 minutes.

### Objectives

In this lab you will install a sample app from the app library.

## **STEP 1:** Install a Sample Application

1. Log in to the Oracle Autonomous Database for *`dev`*: 

    - Go to **Oracle Databases -> Autonomous Transaction Processing** in your compartment
    - Click the database for dev (*APEX\_DEV* if you used the default names)

      ![](./images/db-list.png)

    - Click **Tools** tab 

      ![](./images/atp-tools.png)

    - Under **Oracle Application Express**, click **Open APEX**

      ![](./images/open-apex.png)

    - Click **Workspace Sign-in**

      ![](./images/ws_signin.png)

    - Enter the credentials for the Workspace Admin user (*WS\_ADMIN* if you used the default names) found in the *`dev.env`* file (WORKSPACE\_ADMIN and WORKSPACE\_ADMIN_PWD).

      If you used the defaults, the values are as follow:
      - Worspace: `WS`.
      - User: `WS_ADMIN`.
      - Password: check in the `dev.env` file.

    ![](./images/signin.png)

2. Click **App Gallery**.

    ![](./images/app-gallery.png)

3. Choose the **Opportunity Tracker** application.

    ![](./images/opportunity-tracker.png)

4. Click **Install**.

5. When installed, make sure to click **Manage** and then **Unlock** the app before the next steps:

  ![](./images/unlock.png)

6. To run the application, sign in with the WS\_ADMIN credentials.

7. On first run, you're asked to configure the application. Click **Finish Configuration**.


You may proceed to the next lab.

## Acknowledgements

 - **Author** - Emmanuel Leroy, Vanitha Subramanyam, March 2021
 - **Last Updated By/Date** - Emmanuel Leroy, Vanitha Subramanyam, March 2021

