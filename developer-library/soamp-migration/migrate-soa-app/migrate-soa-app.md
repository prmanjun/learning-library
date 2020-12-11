# Migrating the SOA domain

## Introduction: 

Migrating a SOA domain is equivalent to re-deploying the applications and resources to a new domain and infrastructure.
Once source and target environments are ready for migration, you can transition your production system from on-premises deployment to OCI deployment.

We'll use a manual process to migrate the domain from on-premises and re-deploy on OCI.

Estimated Lab Time: 45 min

### About Product/Technologies

**Deploying, Undeploying, and Redeploying SOA Composite Applications**

Oracle SOA Suite uses the SCA standard as a way to assemble service components into a SOA composite application. You can deploy, undeploy, and redeploy SOA composite applications.

SOA composite applications consist of the following:

Service components such as Oracle Mediator for routing, BPEL processes for orchestration, human tasks for workflow approvals, business rules for designing business decisions, and complex event processing for queries of event streams

Binding components (services and references) for connecting SOA composite applications to external services, applications, and technologies

These components are assembled together into a SOA composite application. This application is a single unit of deployment that greatly simplifies the management and lifecycle of SOA applications.

You can use Fusion Middleware Control, Oracle JDeveloper, or the command line to deploy, undeploy, or redeploy a SOA application.

Migration with manual process consists in 3 steps:

- Convert the SOA code version from 12.2.1.3 to 12.2.1.4 by redeploying it in JDeveloper 12.2.1.4 .

- Create the same directory structure used in source SOA code in the target SOA server .

- Deploy the code with 12.2.1.4 version in SOA server.

### Objectives

In this lab, you will:

- Discover the source SOA Suite Environment and test the source code
- Prepare Your Source for Migration/Side-by-Side Upgrade    
- Prepare Your Target Environment
- Transition from Old Deployment to New Deployment
- Check that the migration was successful by testing your code in SOA

### Prerequisites

To run this lab, you need to:

- Have setup the demo 'on-premises' environment to use as the source domain to migrate
- Have deployed a SOA on OCI domain using the marketplace

## **STEP 1:** Discover the source SOA Suite Environment

1. Open the Firefox web browser to [`http://localhost:7001/em`](http://localhost:7001/em)
to open the EM console for the on-premises environment, 

    - usename `weblogic`
    - password `welcome1`

    ![](./images/3-open-console.png)

2. Click the menu icon

    ![](./images/menu.png =80%x*)

3. Now click on top right button and go to **SOA_Domain -> SOA -> SOA-Infra**

    ![](./images/4-open-project.png)

4. Then click the **Deployed Composites** tab

    ![](./images/deployed-composites.png)

5. Search for the composite **IWSProj3[1.0]** used for migration in this lab.

    ![](./images/5-deployed-composite.png)

    This application is a simple file movement composite which moves a test XML file from the `/tmp/soa/out` folder to the `/tmp/soa/out1` folder.

    The XML needs to be a valid XML file.

## **STEP 2:** Test the application

For testing, we'll place a test XML file in the `/tmp/soa/out` folder, wait 5 to 10 seconds to see the file be removed from the `/tmp/soa/out/` folder and move to the `/tmp/soa/out1` folder as `File_1.txt` 


1. Create the necessary folders:

    ```
    <copy>
    mkdir -p /tmp/soa/out
    mkdir -p /tmp/soa/out1
    chmod -R 777 /tmp/soa/
    </copy>
    ```

2. Copy the test file into the `/tmp/soa/out/` folder

    ```
    <copy>
    cd /tmp/soa/out
    cp /u01/training/OrderSampleOSB.xml ./
    </copy>
    ```

3. Check the file is in the `/tmp/soa/out` folder

    ```
    <copy>
    ls -lh
    </copy>
    ```

4. Wait 5 to 10sec and check the file is now gone:

    ```
    <copy>
    ls -lh
    </copy>
    ```

5. Check the file `File_1.xml` was created in the `/tmp/soa/out1` folder:

    ```
    <copy>
    cd /tmp/soa/out1
    ls -lah
    </copy>
    ```

    It should show 

    ```
    File_1.xml
    ```

## **STEP 2:** Prepare Your Source for Migration (Side-by-Side Upgrade)

In this step we will migrate the application to version 12.2.1.4 which is the target SOA version, from 12.2.1.3 which is the current version.

In order to achieve this, you need to:

* open the application in JDeveloper 12.2.1.3.
* deploy the application as a SAR file
* open JDeveloper 12.2.1.4
* create a new project in JDeveloper 12.2.1.4
* import the SAR file generated in JDeveloper 12.2.1.3 
* let the import wizard migrate the code to 12.2.1.4
* Deploy the application with JDeveloper 12.2.1.4 as a SAR file

*If you used the local VirtualBox VM, you downloaded JDeveloper 12.2.1.4 as part of the SOA Suite Quickstart 12.2.1.4.*

*If you are using the Markletplace demo image, both 12.2.1.3 and 1.2.2.14 JDeveloper version are available on the desktop*

![](./images/soa-local-rdp.png =70%x*)

1. Open the Jdeveloper 12.2.1.3 on the on-premises desktop

    ![](./images/jdev12213.png)

2. In the Application tab, select **IWSApplication**

    ![](./images/open-iwsapplication.png =40%x*)

3. Right click on the Project **IWSProj3**

    ![](./images/iwsproj3.png =40%x*)

4. Select **Deploy -> Deploy IWSProj3...**

    ![](./images/deploy-iwsproj3a.png =70%x*)

5. Select **Generate SAR File** and click **Next**

    ![](./images/deploy-iwsproj3b.png =70%x*)

6. Review and click **Next**

    ![](./images/deploy-iwsproj3c.png =70%x*)

7. Review and click **Finish**

    ![](./images/deploy-iwsproj3d.png =70%x*)

8. Let the code build successfully 

    ![](./images/compilecode12213.png)

9. Open Jdeveloper 12.2.1.4

    If you use the marketplace environment, JDeveloper 12.2.1.4 is on the desktop, click the icon and click **Run** and **OK** to use the full dev suite.

    Otherwise, open the JDeveloper 12.2.1.4 you installed as part of the SOA Quickstart 12.2.1.4 locally


10. Create a new SOA Application 

    ![](./images/j12214a.png =50%x*)

11. Select **SOA Application** in the template list

    ![](./images/j12214b.png =70%x*)

12. Set **IWSApplication** for Application Name, and click **Next**

    ![](./images/j12214c.png =70%x*)

13. Keep the default Project Name, and click **Next**

    ![](./images/j12214d.png =70%x*)

14. Select **Empty Composite**, and click **Finish**

    ![](./images/j12214e.png =70%x*)

15. Click on **File -> Import**

    ![](./images/j12214f.png =35%x*)

16. Select **SOA Archive Into SOA Project** and click **OK**

    ![](./images/j12214g.png =50%x*)

17. Name the project as same as in source environmant **IWSProj3** and click **Next**` button**

    ![](./images/j12214h.png =70%x*)

18. Click on **Browse**

    ![](./images/j12214i.png =70%x*)

19. Go to the location where you have deployed your Jdeveloper 12.2.1.3 project.

    - On the marketplace environment, it will be under `/u02/training/SOAJdevProjects/IWSApplication/IWSProj3/deploy`

    - On your local machine it usualy would be under `JDEVELOPER_FOLDER/mywork/IWSApplication/IWSProj3/deploy`


20. Select the **sca_IWSProj3.jar** and click on **Open** button

    ![](./images/j12214j.png =70%x*)

21. Review and click on **Finish** 

    ![](./images/j12214k.png =70%x*)

22. Let the 12.2.1.3 code migrate to Jdev 12.2.1.4 


We can now deploy the upgraded project as a SAR file

23. Right click the **IWSProj3** project

    ![](./images/iwsproj3.png =40%x*)

24. Select **Deploy -> Deploy IWSProj3...**

    ![](./images/j12214l.png =70%x*)

25. Select **Generate SAR file** and click **Finish**

    ![](./images/j12214m.png =70%x*)

26. Wait until the code compiles successfully

    ![](./images/compilecode12214.png =70%x*)

## **STEP 3:** Prepare Your Target Environment

Prepare your target environment by importing or recreating all the configurations of your source. This will ensure successful deployment of the target Oracle SOA Suite on Marketplace instance.

1. Connect to your SOA on OCI compute instance via the bastion host

    In the terminal window where you opened the tunnel earlier, in the on-premises environment use:

    ```
    <copy>
    ssh -o ProxyCommand="ssh -W %h:%p opc${BASTION_IP}" opc@${REMOTEHOST}
    </copy>
    ```

2. Once on the target server, create the folder structure needed by the application:

    ```
    <copy>
    mkdir -p /tmp/soa/out
    mkdir -p /tmp/soa/out1
    chmod -R 777 /tmp/soa/
    </copy>
    ```

## **STEP 4:** Re-deploy the upgraded application on the target SOA domain

1. Once you are connected to your SOAMP server , open `SOA EM` console in the local browser
in the on-premises environment at [https://localhost:7002/em](https://localhost:7002/em) and provide the credentials.

2. You might see a browser warning because the SSL security is using a self-signed certificate. Go through the steps to confirm the exception:

    ![](./images/firefox-ssl1.png =50%x*)

    ![](./images/firefox-ssl2.png =50%x*)

    ![](./images/soamp-deployment-1.png)

3. Login with the credential from provisioning

    - username: `weblogic`
    - password: `welcome1`

2. Click the menu icon

    ![](./images/menu.png =80%x*)

3. Now click on top right button and go to **SOA_Domain -> SOA -> SOA-Infra**

    ![](./images/nav-composite.png =40%x*)

4. Then click the **Deployed Composites** tab

    ![](./images/deployed-composites.png)

5. Click **Deploy**

    ![](./images/deploy.png =70%x*)

6. Select the **Archive is on the machine...** option

    ![](./images/deploy2.png =70%x*)


7. Click **Browse** and the navigate to the folder location of the upgraded 12.2.14 Application 

    - if you used the local VirtualBox VM, it would be in:
        `JDEVELOPER_FOLDER\mywork\IWSApplication\IWSProj3\deploy` 
        
    - If you used the marketplace environment, it is under `/u02/oracle/developer/mywork/IWSApplication/IWSProj3/deploy`

    ![](./images/filepath.png =70%x*)

8. Select the `sca_IWSProj3.jar` file then click on **Open**


9. Click **Next**

    ![](./images/deploy2.png =70%x*)


10. Select **SOA Folder** as **default** and click **Next**

    ![](./images/deploy4.png)

12. Review all the information and then click **Deploy**

    ![](./images/deploy5.png)

8. You can see **Processing Deploy** Deployment in progress message and wait until you get the message **Deployment Succeeded** and click **Close** button

    ![](./images/deploy6.png =60%x*)

9. Check the deployed project in **Dashboard** 

    ![](./images/soamp-deployment-9.png)


## **STEP 5:** Check the application on the target SOA domain

1. Get back in the terminal where you SSH'ed to the target instance 

2. Navigate to the folder `/tmp/soa/out`

    ```
    cd /tmp/soa/out
    ```

3. We'll select an XML file from the target server to use as demo, and copy it into the `/tmp/soa/out/` folder

    ```
    sudo cp /etc/firewalld/direct.xml /tmp/soa/out
    ```

4. Wait 5 to 10 seconds to check that the file disappeared from the folder as it is been polled by the service which you have deployed. 

    ```
    ls -l
    ```

5. Go to destination folder `/tmp/soa/out1` and you can see a new file with name `File_1.xml` is created by the soa service.

    ```
    cd /tmp/soa/out1
    ls -l
    ```

    ![](./images/success.png =70%x*)

6. you can check the **Flow Instances** of the project with one **FlowID** generated

    ![](./images/soamp-testing-5.png)

5. Click on **FlowID** and see the **Audit Trail** and the relevant logs.

    ![](./images/soamp-testing-6.png)

You may proceed to the next lab

## Acknowledgements

 - **Author** - Akshay Saxena, October 2020
 - **Last Updated By/Date** - Akshay Saxena, October 2020

## See an issue?
Please submit feedback using this [form](https://apexapps.oracle.com/pls/apex/f?p=133:1:::::P1_FEEDBACK:1). Please include the *workshop name*, *lab* and *step* in your request.  If you don't see the workshop name listed, please enter it manually. If you would like for us to follow up with you, enter your email in the *Feedback Comments* section.
