# Migrate the JBoss/WildFly Application

## Introduction

In this lab, we will migrate the application to the JBoss/WildFly Cluster on Oracle Cloud Infrastructure.

Estimated Lab Time: 10min

### Objectives

In this lab, you will:
* Move the application over to the JBoss/WildFly cluster on OCI
* Configure the datasource used by the application to point to the Autonomous Database

### Prerequisites

For this lab, you need

* To have provisioned the WildFly cluster on OCI

## **STEP 1**: Connect to the WildFly admin console

1. From the output of the WildFly deployment, gather the command to create a SOCKSv5 proxy

    It should look something like:

    ```bash
    ssh -C -D 1088 opc@<BASTION_IP>
    ```

2. Run the command in your terminal

    ```bash
    <copy>
    ssh -C -D 1088 opc@<BASTION_IP>
    </copy>
    ```

2. Open a new FireFox browser window.

3. Go to Preferences

    ![](./images/firefox-prefs.png =25%x*)

4. In the search bar, type **proxy**, then click **Settings**

    ![](./images/firefox-proxy.png)

5. In the Settings page, Click **Manual proxy configuration**, then **SOCKS v5**, and enter **localhost** for the host and **1088** for the  port as below:

    ![](./images/firefox-proxy-settings.png =70%x*)

6. Then navigate to the WildFly admin console URL, using the **Private IP** of the wildfly server.

    It should be [http://10.1.2.2:9990/console/](http://10.1.2.2:9990/console/) or [http://10.1.2.3:9990/console/](http://10.1.2.3:9990/console/) if this is your first deployment.

    If you get the message below, you are looking at the wrong node, try the other node's IP

    ![](./images/wrong-node.png)

## **STEP 2:** Locate the WAR file

1. Since we built the `SimpleDB.war` WAR file inside the Docker container, we can find it on your local machine in the 'on-premises' environment folder under:

    ```
    <copy>
    wildfly-to-oci/wildfly/app
    </copy>
    ```

## **STEP 3:** Install the application in WildFly console

1. In the WildFly console, click **Start** under **Deployments**

    ![](./images/wildfly-main.png)

2. Then click **By Server Group** -> **main-server-group** and then the **(+)** icon to **Upload New Deployment**

    ![](./images/new-deployment.png)

3. On the modal prompt, navigate to the location of the WAR file, and select it.

    ![](./images/deployment-step1.png =70%x*)

4. Click Next

    ![](./images/deployment-step2.png =70%x*)

5. Do not change the values in the next screen and click **Finish**

6. The domain controller will deploy the application on all servers in the server group

    ![](./images/deployment-step4.png =70%x*)


## **STEP 4:** Check the application served via the load balancer

1. Get the load balancer public IP from the Terraform output

2. Go to http://`LOAD_BALANCER_IP`/SimpleDB/

3. Check that you see the application being served.

    ![](./images/lb-simpledb-app.png)

You may proceed to the next lab.

## Acknowledgements
 - **Author** - Subash Singh, Emmanuel Leroy, October 2020
 - **Last Updated By/Date** - Emmanuel Leroy, October 2020
