# Architecture

## Introduction

The architecture for this runbook is simple, a single machine running inside of an OCI VCN with a public subnet. If you are using a GPU machine, you will need to attach a block storage or a file system. If an HPC shape is chosen, you will have a local NVMe drive attached to your instance.


![](images/rocky_image.png " ")


### Objectives

In this lab:
* Showcase the different OCI components and services you will need in order to run Rocky DEM on OCI
* Briefly describe the acrhitecture required for this runbook

### Prerequisites

* Some understanding of cloud and database terms is helpful
* Familiarity with Oracle Cloud Infrastructure (OCI) is helpful
* Familiarity with networking is helpful



## Acknowledgements

* **Author** - High Performance Compute Team
* **Contributors** -  Chris Iwicki, Harrison Dvoor, Gloria Lee, Selene Song, Bre Mendonca, Samrat Khosla
* **Last Updated By/Date** - Samrat Khosla, January 2021

