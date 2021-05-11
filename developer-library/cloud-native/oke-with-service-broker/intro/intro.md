# Introduction

## About this Workshop

This lab will walk you through the process of deploying an Oracle Kubernetes Engine (OKE) cluster with the Oracle CLoud Infrastructure (OCI) Service Broker (OSB).

OCI Service Broker lets you manage the lifecycle of services such as Autonomous Database (ATP or ADW), OCI Object Storage or OCI Streaming service as Kubernetes objects.

Estimated Lab Time: 60 minutes.

### Objectives

*Deploy an OKE cluster with OCI Service Broker installed with Terraform*.

In this lab, you will:
- Install the prerequisite software needed to run a Terraform deployment and deploy Kubernetes manifests.
- Deploy an OKE cluster with the OCI Service Broker..
- Provision an example Autonomous Database with Kubernetes.
- Provision an example Object Storage Bucket with Kubernetes.
- Provision an example Stream with Kubernetes.

### Prerequisites

*To run this workshop you need:*

* A Mac OS X, Linux or Windows machine (note that installation of some pre-requisites may be different than the steps in this workshop on Windows).
* An SSH key-pair.
* A OCI account with a compartment set up.

If you are not an administrator on your tenancy, you must insure that the following policies have been set for you:

```
<copy>
Allow group MyGroup to manage groups in tenancy
Allow group MyGroup to manage dynamic-groups in tenancy
Allow group MyGroup to manage policies in tenancy
Allow group MyGroup to manage volume-family in tenancy
Allow group MyGroup to manage instance-family in tenancy

Allow group MyGroup to inspect tenancies in tenancy
Allow group MyGroup to use tag-namespaces in tenancy

Allow group MyGroup to manage all-resources in compartment MyCompartment
</copy>
```

You may proceed to the next lab.

## Acknowledgements

 - **Author** - Emmanuel Leroy, January 2021
 - **Last Updated By/Date** - Emmanuel Leroy, January 2021
