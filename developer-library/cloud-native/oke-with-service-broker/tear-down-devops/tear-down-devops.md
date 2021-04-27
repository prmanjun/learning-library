# Tearing down the infrastructure

## Introduction

In this lab we will be cleaning up our deployment and tearing down the infrastructure.

Estimated Lab Time: 10 minutes

### Objectives

In this lab you will:

- Tear down the infrastructure deployed.
- Tear down the cluster

## **STEP 1:** Tearing down the application and infrastructure

1. Before discarding the cluster, we need to undeploy the Kubernetes manifests that were deployed, which deployed services external to the cluster (load balancer, Autonomous Database, and Stream)

2. To undeploy the app run the following in each environment the app was deployed:

    ```bash
    <copy>
    make delete ENVIRONMENT=development
    </copy>
    ```

    ```bash
    <copy>
    make delete ENVIRONMENT=staging
    </copy>
    ```

    ```bash
    <copy>
    make delete ENVIRONMENT=production
    </copy>
    ```

3. To undeploy the infra, run the following in each environment the app was deployed:

    ```bash
    <copy>
    make delete-infra ENVIRONMENT=development
    </copy>
    ```

    ```bash
    <copy>
    make delete-infra ENVIRONMENT=staging
    </copy>
    ```

    ```bash
    <copy>
    make delete-infra ENVIRONMENT=production
    </copy>
    ```

## **STEP 2:** Tear down the users

1. Get back in the repo terraform folder, run:

    ```bash
    <copy>
    cd terraform
    </copy>
    ```

2. then run:

    ```bash
    <copy>
    terraform destroy
    </copy>
    ```

    and type `yes` at the prompt.

    This will take a minute or less

## **STEP 3:** Tear down the cluster

1. Go back to the cluster deployment folder, from your original cluster deployment with terraform and there again run:

    ```bash
    <copy>
    terraform destroy
    </copy>
    ```

    and type `yes` at the prompt.

    This will take several minutes.

2. Sometimes the destroy phase will fail because the nodes in the node pool are not completely cleaned up before the terraform attempts to destroy the VCN.

    Run the destroy command again to finish clean up if it fails at first.

## **STEP 4:** Clean up Docker images

1. Go to your OCIR image registry and delete any unwanted images. They were created under the `demo` artifact name.


## Acknowledgements

 - **Author** - Emmanuel Leroy, March 2021
 - **Last Updated By/Date** - Emmanuel Leroy, March 2021
