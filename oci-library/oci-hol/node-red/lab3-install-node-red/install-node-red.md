# Installing Node-RED

## Introduction
This lab describes how to install Node-RED on Oracle Autonomous Linux.

Estimated Lab Time: 20 minutes

### Objectives

In this lab, you will:
* Install Node.js
* Install Git
* Install Grunt-cli
* Install Node-RED

### Prerequisites

* Access to a compute instance running Oracle Autonomous Linux

## **STEP 1**: Installing Node.js

First, we need to install Node.js. Make sure you are connected to the compute instance via SSH. To configure the Node.js and the Oracle Instant Client repository:

`sudo yum install -y oracle-nodejs-release-el7 oracle-release-el7`

To install the latest Node.js:

`sudo yum install nodejs`

## **STEP 2**: Installing Git

Git is required in order to clone the latest Node-RED repository. To install Git run:

`sudo yum install git`

## **STEP 3**: Install grunt-cli

To install the grunt-cli module globally:

`sudo npm install -g grunt-cli`

## **STEP 4**: Install Node-RED

### Clone the source repository
Now it is time to install Node-RED. Start by cloning the Node-RED source repository from Github:

`git clone https://github.com/node-red/node-red.git`

This will create the `node-red` directory. Change into the `node-red` directory and continue with the next step.

## **STEP 5**: Install the dependencies

Next we want to install any dependencies.

`npm install`

## **STEP 6**: Building Node-RED
Finally, we can build the application. To build Node-RED:

`grunt build`

You are done with the installation of Node-RED. Before we run Node-RED, we want to first update the Network Security List in OCI and the
`iptables` of the OAL installatio.

You may now [proceed to the next lab](#next).

## Learn More


* [Node.js for Oracle Linux](https://yum.oracle.com/oracle-linux-nodejs.html#InstallingNodeOnOL7)
* [Node-RED](https://nodered.org/)

## Acknowledgements
* **Author** - Kevin Lazarz, Program Manager, TE Hub
* **Last Updated By/Date** - Kevin Lazarz, Program Manager, TE Hub March 2021

Test
