# Understanding the Demo Project

## Introduction

In this lab we will clone the demo repository code and look into the various components to understand its structure.

The Demo project consists in a simple application based on micro-services and making use of **Oracle Streaming Service** and **Autonomous Database**, managed within kubernetes via the **OCI Service Broker**.

The application includes a *`producer`* service that generates numeric data for demo purposes. Think of it as an IoT device streaming measurements, or a monitoring service streaming metrics. 

The *`producer`* pushes data to the Oracle Streaming Service, and a *`consumer`* service picks it up at the other end, to post it into the Autonomous Database.

A *`web`* application is used to display the data in real-time: the server gets notified through the Change Query Notification capability of the database that new data is available, and uses Server Sent Events (i.e. Server Push) to push the data to a subscribed client browser.

![](./images/app.png)


Estimated Lab Time: 10 minutes

### Objectives

In this lab you will:

- Copy the demo template to your own Github
- Review the demo project structure
- Provision the required users with *`terraform`*

## **STEP 1:** Use the template

1. To use the template, click **Use this Template**

    ![](./images/template.png)

2. Choose a name

3. **For security reasons, we recommend always making your repo PRIVATE**

4. Click **Create repository from template**.

5. Then under the **Code** button, copy the git URL and clone your repository locally with:

    ```bash
    <copy>
    git clone <your_git_url>
    </copy>
    ```

6. Get into the folder:
    
    ```
    <copy>
    cd ./<name of your repo>
    </copy>
    ```

## **STEP 2:** Review the project structure

1. The project has the following folder structure:

    ```bash
    ├── images
    │   ├── consumer
    │   ├── db-config
    │   ├── producer
    │   └── web
    ├── k8s
    │   ├── base
    │   │   ├── app
    │   │   ├── components
    │   │   └── infra
    │   └── overlays
    │       ├── branch
    │       ├── development
    │       │   ├── app
    │       │   ├── components
    │       │   └── infra
    │       ├── production
    │       │   ├── app
    │       │   ├── components
    │       │   └── infra
    │       └── staging
    │           ├── app
    │           ├── components
    │           └── infra
    ├── makefile
    ├── makefile.common
    ├── makefile.python
    ├── README.md
    ├── creds.env.template
    ├── global.env
    ├── skaffold.yaml
    ├── scripts/
    └── terraform/
    ```

2. The *`images`* folder contains the project applications/services, with their respective code and Dockerfile

3. The *`k8s`* folder contains the kubernetes resource templates

    - The *`k8s/base`* folder contains base templates used for the whole deployment, and includes:
        - an *`app`* folder describing the application resources, 
        - an *`infra`* folder describing the PaaS services, 
        - and a *`components`* folder that contains resources used in both *`infra`* and *`app`*.

    - The *`k8s/overlays`* folder contains the changes to apply to the base templates to configure different environments:
        - a *`development`* environment
        - a *`staging`* environment
        - a *`production`* environment
        - and *`branch`* overlay which uses the *`development`* overlay to produce a branch-suffixed environment within the *`development`* namespace.


4. The *`terraform`* folder contains templates to create the *`users`* and *`credentials`* needed to publish Docker images to the Oracle Container Image Registry (OCIR) and to access the Oracle Streaming Service, as well as a user that can interact with the kubernetes cluster to use for Continuous Integration / Continuous Deployment (CI/CD) pipelines.

## **STEP 3:** Setup the variables required to run the terraform deployment

1. Get into the terraform folder:

    ```bash
    <copy>
    cd ./terraform
    </copy>
    ```


2. Create a *`TF_VARS.sh`* file from this template:

    You have created a similar file for the OKE cluster with OCI Service Broker deployment, and if the variables are already exported you can skip to the next step

    ```bash
    <copy>
    export TF_VAR_user_ocid=ocid1.user.oc1....
    export TF_VAR_fingerprint=00:00:00:00...
    export TF_VAR_private_key_path=~/.oci/oci_api_key.pem
    export TF_VAR_tenancy_ocid=ocid1.tenancy.oc1.....
    export TF_VAR_region=us-ashburn-1    
    </copy>
    ```
3. Populate the variables with your tenancy information, gathered from the installation of the OCI CLI

4. Source the *`TF_VARS.sh`* file

    ```bash
    <copy>
    . ./TF_VARS.sh
    </copy>
    ```

## **STEP 4:** Populate the *`terraform.tfvars`* file

1. Generate a *`terraform.tfvars`* from the *`terraform.tfvars.template`*

    ```bash
    <copy>
    cp terraform.tfvars.template terraform.tfvars
    </copy>
    ```
2. Populate the required variables:

    If you are not able to create users, you will need to provide the *`user_ocid`* of users that are part of groups with the proper policies (see below)
    If you are able to create users but not groups or policies, provide the group_ocid for each user.

    Provide the *`cluster_id`* of the cluster created in lab 2, which was output in the terraform output

    ```yaml
    tenancy_ocid = "ocid1.tenancy.oc1.."
    compartment_ocid = "ocid1.compartment.oc1.."
    region           = "us-ashburn-1"
    cluster_id = "ocid1.cluster...."

    # provide the OCID of the pusher user if you want to reuse an existing user
    ocir_pusher_ocid = null
    # provide the OCID of the OCIR pusher group if you want to reuse an existing group to create a user
    # only one group is needed per tenancy
    ocir_pushers_group_ocid = null

    # provide the OCID of the CI user to deploy to k8s, if you want to reuse an existing user
    ci_user_ocid = null
    # provide the OCID of the CI User group if you want to reuse an existing group to create a user
    # only one group is needed per OKE cluster
    ci_user_group_ocid = null

    # provide the OCID of the streaming user if you want to reuse an existing user
    streaming_user_ocid = null
    # provide the OCID of the streaming user group if you want to reuse an existing group to create a user
    # only one group is needed per OKE cluster
    streaming_group_ocid = null
    ```

    The terraform will provision a user in a OCIR pusher group with the following policies (provided here for reference for your tenancy administrator if they need to create them for you)

    ```
    <copy>
    allow group ocir_pusher_group_name to use repos in tenancy
    allow group ocir_pusher_group_name to manage repos in tenancy where ANY {request.permission = 'REPOSITORY_CREATE', request.permission = 'REPOSITORY_UPDATE'}
    </copy>
    ```

    The terraform will provision a user in a Streaming Service group with the following policies:

    ```
    <copy>
    allow group streaming_group_name to use stream-pull in tenancy
    allow group streaming_group_name to use stream-push in tenancy
    </copy>
    ```

    The terraform will provision a user in a Cluster user group with the following policies:

    ```
    <copy>
    allow group ci_group_name to use clusters in tenancy where request.region = '{region}'
    </copy>
    ```

## **STEP 5:** Run the terraform script

1. Init the terraform project:

    ```bash
    <copy>
    terraform init
    </copy>
    ```

2. Apply the terraform

    ```bash
    <copy>
    terraform apply
    </copy>
    ```

    And answer *`yes`* at the prompt

3. The terraform outputs the following useful info:

    - The *`OCIR_pusher_username`* and *`token`* required to login to the OCIR image registry

4. You should also find the following artifacts in the folder for the CI user:

    - A *`cluster_admin_user_xxxx_rsa_private_key.pem`* file for a CI user to access the cluster via the OCI CLI
    - A corresponding *`cluster_admin_user_xxxx_oci_config.txt`* file
    - A *`kubeconfig`* file

## **STEP 6:** Docker login 

1. The terraform creates a `creds.env` file on the root of the project.

2. Go back to the root folder:

    ```bash
    <copy>
    cd ..
    </copy>
    ```

4. Login to the Docker OCIR repository

    You can do so with the helper function 

    ```bash
    <copy>
    make repo-login
    </copy>
    ```

    which uses the `creds.env` and `gobal.env` files and runs the `docker login <region>.ocir.io/<tenancy_namespace>` command with the credentials saved in `creds.env`


You may proceed to the next lab.

## Acknowledgements

 - **Author** - Emmanuel Leroy, February 2021
 - **Last Updated By/Date** - Emmanuel Leroy, February 2021
