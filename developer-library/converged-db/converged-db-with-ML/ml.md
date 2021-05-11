# Oracle Machine Learning

## Introduction

**Move the algorithms, not the data!**

With Oracle Machine Learning, Oracle moves the algorithms to the data. Oracle runs machine learning within the database, where the data reside. This approach minimizes or eliminates data movement, achieves scalability, preserves data security, and accelerates time-to-model deployment. Oracle delivers parallelized in-database implementations of machine learning algorithms and integration with the leading open source environments R and Python. Oracle Machine Learning delivers the performance, scalability, and automation required by enterprise-scale data science projects.

**Oracle Database - the multi-model converged database**

Users should not have to create and manage multiple databases to access different analytical functionality, which adds complexity and cost. Instead, all such functionality should exist in a single converged, multi-model database, bringing together a broad set of algorithms that can operate on data with various data types and data models. This is a key differentiator for Oracle Database, and reinforces Oracle’s goal to provide such advanced development tools to the widest range of developers.

**Features of Oracle Machine Learning**

`Here are a few highlights of Oracle Machine Learning functionality:`

- Oracle integrates machine learning across the Oracle stack and the enterprise, fully leveraging Oracle Database and Oracle Autonomous Database
- Empowers data scientists, data analysts, developers, and DBAs/IT with machine learning
- Eliminates costly data movement and access latency
- Fast and scalable data exploration, data preparation, and machine learning algorithms
- Over 30 algorithms supporting: regression, classification, time series, clustering, feature extraction, anomaly detection
- R and Python integration directly supports data scientist role, leveraging open source ecosystems
- Ease of machine learning model and R/Python script deployment
- Automates key machine learning process steps
- Leverages existing enterprise backup, recovery, and security mechanisms and protocols
- Bring the algorithms to the data
- By including Oracle Machine Learning with Oracle Database on-premises and in the Cloud, Oracle continues to support a next-generation converged data management and machine-learning platform.


*Estimated Lab Time:* 2.5 Hrs

### Prerequisites
This lab assumes you have:
- A Free Tier, Paid or LiveLabs Oracle Cloud account
- SSH Private Key to access the host via SSH
- You have completed:
    - Lab: Generate SSH Keys
    - Lab: Prepare Setup (Free Tier and Paid Tenants Only)
    - Lab: Environment Setup
    - Lab: Initialize Environment
  1.   Have access to or have Installed Oracle Database 19c Enterprise Edition High Performance, Release 19.8.0.0.0 with Data Mining Option.
 
  2. Have access to or have installed Oracle SQL Developer, version 3.0, or later.
     Note: SQL Developer does not have an installer. To install SQL Developer, just unzip the free SQL Developer download to any directory on your PC.
 
  3. Have set up Oracle Data Miner 19c for use within Oracle SQL Developer.
     Note: If you have not already set up Oracle Data Miner, complete the following lesson: Setting Up Oracle   Data Miner 19c Release 2.

    ![](./images/diagram-ml.png " ")


   [](youtube:QnTzm9SShBs)

## STEP 0: Identifying SQL Developer and Data Miner Interface Components

  Before you create a Data Miner Project and build a Data Miner workflow, it is helpful to examine some of the Data Miner interface components within SQL Developer. You can then structure your working environment to provide simplified access to the necessary Data Miner features.

   After setting up Oracle Data Miner for use within SQL Developer, different interface elements may be displayed, including both SQL Developer and Data Miner components.

In the following example, several display elements are open, including the:
-	The SQL Developer Connections tabs
-	The SQL Developer Reports tabs
-	The Data Miner tab

  ![](./images/data-preparation-1.png " ")

`Notes`:
-	The layout and contents of your SQL Developer window may be different than the example shown above.
-	SQL Developer and Data Miner interface elements open automatically when needed.
-	Additional Data Miner interface elements include the Workflow Jobs, Property Inspector, Component   Palette, and Thumbnail tabs. You can open any one them manually from the main menu by using **View > Data Miner >** as shown here:

  ![](./images/data-preparation-2.png " ")

In order to simplify the interface for Data Mining development, you can dismiss the SQL Developer specific interface elements by clicking on the respective Close **[x]** icons for each tab or window.

For example, close both of the SQL Developer tabs mentioned above:

1.	SQL Developer **Reports** tab

   ![](./images/data-preparation-3.png " ")

2.	SQL Developer **Connections** tab
  
   ![](./images/data-preparation-4.png " ")

  Now, the SQL Developer interface should look like this:
   ![](./images/data-preparation-5.png " ")

**DataMiner > Workflow Jobs.**

`Note`: You can re-open the SQL Developer Connections tab (and other interface elements) at any time by using the View menu.
 

## STEP 1: Data Preparation

**1. Start creating a Data Miner Project**

   Before you begin working on a Data Miner Workflow, you must create a Data Miner Project, which serves as a container for one or more Workflows.
In the tutorial Setting up Oracle Data Miner 11g Release 2, you learned how to create a database account and SQL Developer connection for a data mining user named dmuser. This user has access to the sample data that you will be mining.
***Note:*** If you have not yet set up Oracle Data Miner, or have not created the data mining user, you must first complete the tasks presented in the tutorial [Setting Up Oracle Data Miner 19c Release 2](https://docs.oracle.com/en/database/oracle/oracle-database/19/tutorial-install-dm-repo/),

  To create a Data Miner Project, perform the following steps:

1. In the Data Miner tab, right-click the data mining user connection that you previously created, and select **New Project**, as shown here:

    ![](./images/data-preparation-6.png " ")

2. In the Create Project window, enter a project name (in this example Data_Preparation) and then click **OK**.

    ![](./images/data-preparation-7.png " ")

    ***Note***: You may optionally enter a comment that describes the intentions for this project. This description can be modified at any time.

  `Result`: The new project appears below the data mining user connection node.

    ![](./images/data-preparation-8.png " ")

**Build a Data Miner Workflow**

A Data Miner Workflow is a collection of connected nodes that describe a data mining processes.
A workflow:
- Provides directions for the Data Mining server. For example, the workflow says, "Build a model with these characteristics." The data-mining server builds the model with the results returned to the workflow.
- Enables you to interactively build, analyze, and test a data mining process within a graphical environment.
- Might be used to test and analyze only one cycle within a particular phase of a larger process, or it may encapsulate all phases of a process designed to solve a particular business problem.

**What Does a Data Miner Workflow Contain?**

- Visually, the workflow window serves as a canvas on which you build the graphical representation of a data mining process flow, like the one shown here:

   ![](./images/data-preparation-9.png " ")

   ***Notes***:
   - Each element in the process is represented by a graphical icon called a node.
   - Each node has a specific purpose, contains specific instructions, and may be modified individually in numerous ways.
   - When linked together, workflow nodes construct the modeling process by which your particular data mining problem is solved.

   As you will learn, any node may be added to a workflow by simply dragging and dropping it onto the workflow area. Each node contains a set of default properties. You modify the properties as desired until you are ready to move onto the next step in the process.


**2. Sample Data Mining Scenario**

   In this topic, you will create a data mining process that predicts the revenue of customers. 

   To accomplish this goal, you build a workflow that enables you to:

   - Identify and examine the source data
   - Extract data from multiple sources.
   - Combine the data from multiple sources into a common format that can be utilized for ML. 

`To create the workflow for this process, perform the following steps.`

**3. Create a Workflow and Add data for the workflow**

  1.  Right-click your project (Retail\_Data\_Analysis) and select **New Workflow** from the menu. For this workflow we will be using these three tables :  `DATA_REL, JSON_PURCHASEORDER, XML_PURCHASEORDER`

   ![](./images/data-preparation-10.png " ")

   `Result`: The Create Workflow window appears.

  2. In the Create Workflow window, enter **Praparing_Data** as the name and click **OK**.
   
   ![](./images/data-preparation-11.png " ")

    `Result`:
     - In the middle of the SQL Developer window, an empty workflow canvas opens with the name that you specified.
     - On the right-hand side of the interface, the Component Palette tab of the Workflow Editor appears (shown below with a red border).
     - In addition, three other Oracle Data Miner interface elements are opened:
       o	The Thumbnail tab
       o	The Workflow Jobs tab
       o	The Property Inspector tab

    ![](./images/data-preparation-12.png " ")


   3. The first element of any workflow is the source data. We will extract data from a JSON table and a XM table. Here, we cannot directly add a data source. We will use a query editor to read the tables in a relational table format. You add a Data Source node to the workflow, and select the JSON\_PURCHASEORDER and XML\_PURCHASEORDER tables as the data source.

     **A.** In the Component Palette, click the **Data** category. A list of data nodes appear, as shown here:
    ![](./images/data-preparation-13.png " ")

     **B.** Drag and drop the two SQL Query nodes onto the Workflow pane.

    `Result`: A SQL Query node appears in the Workflow pane. Right Click on it and select edit option from the context menu.  Paste the below queries for JSON and XML tables respectively. Now Click in ‘OK’.

   **JSON:**
    SELECT jt.* FROM JSON_PURCHASEORDER, JSON\_TABLE(JSON\_DOCUMENT, '$[*]'  COLUMNS (INVOICENO VARCHAR2(256) PATH '$.INVOICENO', STOCKCODE VARCHAR2(256) PATH '$.STOCKCODE', DESCRIPTION VARCHAR2(1024) PATH DESCRIPTION, QUANTITY Number PATH QUANTITY, INVOICEDATE VARCHAR2(1024) PATH INVOICEDATE, UNITPRICE NUMBER(38,2) PATH UNITPRICE, CUSTOMERID VARCHAR2(1024) PATH CUSTOMERID, STATE VARCHAR2(256)  PATH STATE)) jt

   **XML:**
   SELECT xt.* FROM   XML\_PURCHASEORDER x, XMLTABLE('PURCHASEORDER' PASSING x.XML\_DOCUMENT COLUMNS INVOICENO VARCHAR2(256), STOCKCODE VARCHAR2(256), DESCRIPTION VARCHAR2(1024),QUANTITY NUMBER,  INVOICEDATE VARCHAR2(1024), UNITPRICE NUMBER(38,2), CUSTOMERID VARCHAR2(1024), STATE VARCHAR2(256) ) xt


   **Notes:**
   - Oracle Data Miner generates workspace node names and model names automatically. In this example, the name "SQL Query" is generated. You may not get exactly the same node and model names as shown in this lesson.
   - You can change the name of any workspace node or model using the Property Inspector.

    ![](./images/data-preparation-14.png " ")

   **C.** Drag and drop the **Create Table or View** node onto the Workflow pane. Right click on the Query nodes and connect them to the output nodes. Rename the output nodes.

   - Oracle Data Miner generates workspace node names and model names automatically. The table name can be changed from the **Properties** Panel, as shown below.

   ![](./images/data-preparation-15.png " ") 

   **D.** Right click on the output table of JSON and XML and then click on ‘Run’

    ![](./images/data-preparation-16.png " ")

   Click on each of the Output Node and select ‘View Data’

    ![](./images/data-preparation-17.png " ")

   Combine the data from two different sources (XML and JSON), now in two tables into a single table.

   Drag a SQL Query control and connect it to both the XML and JSON table. Write a UNION Query like mentioned below to append the two tables. Then we connect the Query control table to an Output table. 
   
   `Note`: Change the table names according to our project. 

   SELECT * FROM "JSON\_DATA1\_N$10002" UNION ALL SELECT * FROM "XML\_DATA2\_N$10005"

   We can view the combined data by connecting this query to an Output table and executing ‘Run’ on the Output table.

    ![](./images/data-preparation-18.png " ")

   4.We add the RDBMS regular table data, using a data source

   - Drag and drop the **Data Source** node onto the Workflow pane.

    `Result`: A Data Source node appears in the Workflow pane and the Define Data Source wizard opens.
   
    ![](./images/data-preparation-19.png " ")

   In Step 1 of the wizard

   **A.**	Select DATA_RELTN from the Available Tables/Views list, as shown here:

    ![](./images/data-preparation-20.png " ") 

   `Note:`You may use the two tabs in the bottom pane in the wizard to view and examine the selected table. The Columns tab displays information about the table structure, and the Data tab shows a subset of data from the selected table or view.

   **B.** Click Next to continue.

   5.In Step 2 of the wizard

   - you may remove individual columns that you do not need in your data source. In our case, we will keep all of the attributes that are defined in the table.
   - At the bottom of the wizard window, click Finish.

   ![](./images/data-preparation-21.png " ") 

   `Result`: As shown below, the data source node name is updated with the selected table name, and the properties associated with the node are displayed in the Property Inspector, located below the Component Palette pane.
   
   ![](./images/data-preparation-22.png " ")
   
   `Notes`:
    - You can resize nodes in the workflow canvas by entering or selecting a different value from the Zoom options. Notice that 75% has been selected from the Zoom pull-down list.
    - You can add descriptive information about any node by using the Details tab in the Property Inspector.
    - The Thumbnail tab also provides a smaller display of the larger workflow window. As you drag nodes around the workflow window, the thumbnail view automatically adjusts.

**Examine the Source Data**

  - You can use an Explore Data node to examine the source data. Although this is an optional step, Oracle Data Miner provides this tool to enable you to verify if the selected data meets the criteria to solve the stated business problem.

  Follow these steps:
  
  1. Drag and drop the Explore Data node from the Component Palette to the Workflow, like
   ![](./images/data-preparation-23.png " ")
                
   `Result`: A new Explore Data node appears in the workflow pane, as shown here. (As before, a node name is automatically generated.)
    ![](./images/data-preparation-24.png " ") 

   `Notes`:
    A yellow Information (!) icon in the border around any node indicates that it is not complete. Therefore, at least one addition step is required before the Explore Data node can be used.
   
   In this case, a data source node must be "linked" to the Explore Data node to enable further exploration of the source data.

  2. To link the data source and explore data nodes, use the following instructions:
  
   A. Right-click the data source node (DATA_RELTN), select **Connect** from the pop-up menu, and then drag the pointer to the Explore Data node, as shown here:

   ![](./images/data-preparation-25.png " ") 

   B.	Then, click the Explore Data node to connect the two nodes. The resulting display looks like this:
   
   ![](./images/data-preparation-26.png " ")

  3. Right click Explore data and click edit. Next, select a "Group By" attribute for the data sourceA. Double-click the Explore Data node to display the Select Attributes window..

  A. In the Group By list, select the CUSTOMER_ID attribute, as shown here:
   ![](./images/data-preparation-27.png " ")
  B. Then, click OK.

   `Note`: The Select Attributes window also allows you to remove (or re-add) any attributes from the source data.

  4. Next, right-click the Explore Data node and select Run.

    ![](./images/data-preparation-28.png " ")

   `Result`:
   - Data Miner displays status information in the Workflow Jobs tab while processing the node.
   - When the update is complete, the data source and explore data nodes show a green check mark in the borders, like this:

   ![](./images/data-preparation-29.png " ")
   `Note`: When you run any process from the workflow canvas,                                              the steps that you have specified are executed by the Oracle Data Miner Server.
   
   5.To see results from the Explore Data node, perform the following:
  
  A. Right-click the Explore Data node and select View Data from the menu
   ![](./images/data-preparation-29.png " ")

    Go to statistics tab and click on one of the row.

   ![](./images/data-preparation-31.png " ")

   `Result:` A new tab opens for the data profile node, as shown below

   `Notes`:
    - Data Miner calculates a variety of information about each attribute in the data set, as it relates to the "Group By" attribute that you previously defined, including a Histogram, Distinct Values, Mode, Average, Min and Max value, Standard Deviation, Variance, Skewness, and Kurtosis.
    - The display enables you to visualize and validate the data, and also to manually inspect the data for patterns or structure.

  B. Select any of the attributes in the Name list to display the associated histogram in the bottom window.

  C. When you are done examining the source data, dismiss the Explore Data tab by clicking the Close icon (X). 
  
  Next, you move from a high-level manual analytic exercise to using the power of database data mining.

  6.Now we can append the data from `DATA_REL` and `JSON_XML_COMBINED` into a single table using the `UNION ALL` query in the `SQL Query` control and store the data in a output table. Steps will be similar to what we had mentioned earlier. 

  A.  Before we `JOIN` the tables, we will update the some of the attributes to numeric type, so that the data types of both tables match during the join.  Add a `Transform` node and connect the `DATA_REL` table to the `Transform` node. 
   
   ![](./images/data-preparation-32.png " ")

  B. Right Click on the `Transform` node and select `Run` option. Now you can view the data statistics when you Right Click on the `Transform` node and Select the `Edit` option

   ![](./images/data-preparation-33.png " ") 

  C. The edit Wizard comes up for the `Transform` Node. Click on the Browse table button, and select the XML_JSON_COMBINED data table.  Click on the `Add Custom Transformation` button as marked in the image.

   ![](./images/data-preparation-34.png " ") 

  D. We want to convert the datatype of Quantity column from Varchar2 to Numeric. From the `Functions` tab, expand `Conversion` and click on the `TO_NUMBER` function to bring it to the `Expression` panel.

   ![](./images/data-preparation-35.png " ")

  E. Now select the `Attributes` Tab and Click on `OUANTITY`, to select this attribute.  Type the `Column Name`. Keep it same `QUANTITY`.  Now `validate` the expression by clicking the Validate button. After successful validation, click on the `OK` button.

   ![](./images/data-preparation-36.png " ")


  F. Now select the varchar2 ‘Quantity’ column and click on the `Exclude Column` button as shown below. Now you can see an x mark in the output column for the variable. We do this because we do not need this varchar column anymore; instead, we have the numeric `Quantity` column. Click on `OK` now.

   ![](./images/data-preparation-37.png " ")

  G.Now drag a `Create Table` node into the canvas and connect it with the `Transform` node. Right click on the `output node` and select `Run` from the context menu.  After successful execution, again right click on `output node` and select `View Data`.

   ![](./images/data-preparation-38.png " ")

  H. We select the `Column` tab and check the `Quantity` column. It will now be shown as numeric.

   ![](./images/data-preparation-39.png " ")

  7.Drag a `SQL Query` node. Connect it to the Relational DB table and combined JSON and XML table.  Right Click on the node and select the `Edit` option. The Editor window opens up.

   ![](./images/data-preparation-40.png " ")

  A. Copy paste the below query and change the table or Node names according to your project. The UNION ALL command combines the result set of two or more SELECT statements, thus resulting in a table with all the data from both the tables. 

  select "JSON_XML_N$10088"."CUSTOMERID","JSON_XML_N$10088"."DESCRIPTION","JSON_XML_N$10088"."INVOICEDATE","JSON_XML_N$10088"."INVOICENO","JSON_XML_N$10088"."QUANTITY","JSON_XML_N$10088"."STATE","JSON_XML_N$10088"."STOCKCODE","JSON_XML_N$10088"."UNITPRICE" from "JSON_XML_N$10088"
   UNION ALL 
  select "DATA_RELATN_N$10029"."CUSTOMERID","DATA_RELATN_N$10029"."DESCRIPTION","DATA_RELATN_N$10029"."INVOICEDATE","DATA_RELATN_N$10029"."INVOICENO","DATA_RELATN_N$10029"."QUANTITY","DATA_RELATN_N$10029"."STATE","DATA_RELATN_N$10029"."STOCKCODE","DATA_RELATN_N$10029"."UNITPRICE" from "DATA_RELATN_N$10029"
   Click OK.

   ![](./images/data-preparation-41.png " ")

  B. Now, write click on the `SQL Query` node and select `Run`.  After successful completion, a green tick mark will appear on the node. 

   ![](./images/data-preparation-42.png " ")

  C.  Now drag a `Create Table` node to get an `Output table`. Connect it to the Query node.  Now Right Click on the `Output table` and select `Run`.  This will store the resullt set from query into the table.

   ![](./images/data-preparation-43.png " ")

  8.Drag a `Transform` node into the canvas as shown below. Connect it to the `output table` that contains the combined XML and JSON data. After connecting, right click and select the `Run` option
   ![](./images/data-preparation-44-45.png " ") 
   
  A. Now Right Click on the `Transform node` and select Edit option.  This will open up the `Edit Transform Node` wizard. Click on the `Add Custom Transformation` button as marked in the image. 

   ![](./images/data-preparation-47.png " ")

  B.  We want to create a new attribute called TOTALAMOUNT which will be a product of QUANTITY*UNITPRICE
    
    Select the two attributes QUANTITY and UNITPRICE along with the * symbol for multiplication.

   ![](./images/data-preparation-48.png " ")

  C. Put the `Column Name` as TOTALAMOUNT, click on the `validate` button to Validate the expression and     then click `OK`.
   
   The new attribute is now visible in the attribute `Names` Column. Click OK. 

   ![](./images/data-preparation-49.png " ")

  D. Right Click and Run the `Transform node`.  After that drag a `Create Table` node to create an output table. Connect it to `Transform` node and then Right Click and select the `Run` option.  The transformed table data will be stored in the output table.


   ![](./images/data-preparation-50.png " ")

  9.Now we will create 3 new attributes with the aggregate function. Three attributes (QUANTITY, TOTALAMOUNT, and UNITPRICE) will be aggregated using the SUM function, grouped by CUSTOMERID and STATE.

   A.  Drag the `Aggregate` node into the canvas and connect it to the transformed table data. Right click and select the `Edit` option from context menu.  

    ![](./images/data-preparation-51.png " ")

   B.Click on the `Aggregate Wizard` on the Edit Aggregate node window. Now we will define the aggregation. In our case, we check the check box of the `Sum` function of `Numerical` data. Click on the Next button.

    ![](./images/data-preparation-52.png " ")

   C.In the `Select Columns` step of the wizard, we select the three columns, `QUANTITY, TOTALAMOUNT, and UNITPRICE` and click `Next`.
    ![](./images/data-preparation-53.png " ")

   D. In `Select Sub Group By`, we do not select any columns and click on Next. 

    ![](./images/data-preparation-54.png " ")

   E. Now the new column names can be seen. Click on the `Finish` button.
    ![](./images/data-preparation-55.png " ")

   F. Now Click on the `Edit` button beside the `Group By` field.
    ![](./images/data-preparation-56.png " ")
   
   G.  Select the two columns CUSTOMERID and STATE for Group by and Click `Ok`. We can see the output columns listed in the wizard. Click `Ok`. 
    ![](./images/data-preparation-57.png " ")

   H.Drag a Create Table node to the canvas and connect it with the `Aggregate` node.  Right Click on the `output table` node and select `Run` option. After the execution is completed, data is stored in the `output node`. Now Right Click on the `Output Node` and select `View Data` to see the aggregated data in the output table.
    ![](./images/data-preparation-58.png " ")

   I. We can see the aggregated columns as shown below. 
    ![](./images/data-preparation-59.png " ")

   10.Now we will go ahead with another aggregation, we will do a `Count(Distinct)` with three columns: DESCRIPTION, INVOICEDATE and STOCKCODE.  

   A. Drag a new `Aggregate Node` to the canvas and connect it to the Transformed Data, output node. 
    ![](./images/data-preparation-60.png " ")
    ![](./images/data-preparation-61.png " ")
   B. Right Click on the `Aggregate` node and select the Edit option.  The Aggregation wizard opens up.  In the Select Functions step, check the `COUNTDISTINCT()` function under the Character functions and select `Next`.
    ![](./images/data-preparation-62.png " ")
   
   C.Select the columns STOCKCODE, INVOICEDATE and DESCRIPTION in the `Select Columns` step and click on `Next`

   ![](./images/data-preparation-63.png " ")

   D. Skip the `Select Sub Group By` step in the wizard, Click on `Next`.  The three new columns will be listed. Click `Finish`. 

    ![](./images/data-preparation-64.png " ")

   E. Click on the `Edit` button to select the `Group By` Columns, Select CUSTOMERID and STATE and click Ok
    ![](./images/data-preparation-65.png " ")

   F. Click `Ok` to close the wizard
    ![](./images/data-preparation-66.png " ")

   11.Drag a `Create Table` node to the canvas and connect it with the `Aggregate` node.  Right click on the Output node and select the `Run` option. The aggregated data will be stored in the `output` table.  Right click on the Output node and select `View Data` to see the aggregated data.

    ![](./images/data-preparation-67.png " ") 
    ![](./images/data-preparation-67a.png " ") 

   12.Drag a `Join` node into the Canvas. Connect the `Join` node with the two output tables, containing the aggregated data (Sum Aggregation and Distinct Count aggregated data).

   ![](./images/data-preparation-69.png " ")
   ![](./images/data-preparation-70.png " ")

   A.Right Click on the `Join` node and select `Edit`, to start the `Join` Node wizard. In the Wizard click on the + sign as shown in the image below.

   ![](./images/data-preparation-71.png " ")

   B. Select the Source tables as shown, and then select the join columns.  We will use CUSTOMERID and STATE as the join columns.  Select each of the join column pairs from both the tables, and click on the Add button to add the join criteria. After selecting both join columns, click Ok. 

    ![](./images/data-preparation-72.png " ")

   C.Now remove the redundant columns from the join table output. To remove the redundant columns, select the columns and click on the x button as shown below. When prompted for confirmation, select `Yes`.

   ![](./images/data-preparation-73.png " ")

   D.Go to the filter tab and we will add a filter to remove NULL values from the CUSTOMERID column of both tables. The criteria will be as below. The column names can be selected by clicking on the right panel displaying the table name and its columns.

    "AGG_SUM"."CUSTOMERID" IS NOT NULL  And "AGG\_COUNT\_DISTINCT"."CUSTOMERID" IS NOT NULL

   Click on the `Validate` button to validate your query. After the query is validated, click on `Ok`. Close the wizard by clocking `Ok`.

    ![](./images/data-preparation-74.png " ")

   E. Right Click on the `Join` node and select `Run` to execute the join node. Drag a `Create Table` node to the canvas. Connect the `Join` node to the output table and execute the output table, by selecting `Run`. 

    ![](./images/data-preparation-75.png " ")

   F. Right click on the output node and select `View` to see the joined data

   ![](./images/data-preparation-76.png " ")

   13.The next step is to remove the rows with duplicate CUSTOMERID.  
   A.  Add a SQL Query node to the workflow and connect it to the Joined data output node. 

   ![](./images/data-preparation-77.png " ")

   B. Right Click on the `SQL Query` node and select the Edit option. In the `SQL Query Node Editor` window, write a similar query as mentioned below. Change the table names according to your project. Then click `Ok`. 
   SELECT * from "JOINEDDATA_N$10059" where customerid not in (select customerid from "JOINEDDATA_N$10059" group by customerid having count(*) > 1)

    ![](./images/data-preparation-78.png " ")

   C. Drag a `Create Table` node into the workflow and connect it with the `SQL Query` node.  Right Click on `SQL Query` node and select `Run`.

   ![](./images/data-preparation-79.png " ")

   D. After successful execution, right click on the `Output` Table node and select `View Data`. Now we have records with unique CUSTOMERID and here from NULL values. 

    ![](./images/data-preparation-80.png " ")

   14.Save the workflow by clicking the Save All icon in main toolbar

   ![](./images/data-preparation-81.png " ")

   Now your data is ready for usage in machine learning algorithms. 
   ![](./images/data-preparation-82.png " ")

We have final three source tables:
-	JSON and XML data combined
-	JSON, XML and RELATIONAL data combined
-	Transformed Relational Data

**This concludes this lab. You may now [proceed to the next lab](#next).**

## STEP 2: Regression

**Create a Data Miner Project**

To create a Data Miner Project, perform the following steps:
1. In the Data Miner tab, right-click the data mining user connection that you previously created, and select **New Project**, as shown here:

![](./images/regression1.png " ")

2. In the Create Project window, enter a project name (in this example Regression) and then click **OK**.

![](./images/regression2.png " ")

**Note**: You may optionally enter a comment that describes the intentions for this project. This description can be modified at any time.

**Result**: The new project appears below the data mining user connection node.

![](./images/regression3.png " ")

**Build a Data Miner Workflow**

To create the workflow for this process, perform the following steps:

1. Create a Workflow and Add data for the workflow. Right-click your project (Regression) and select **New Workflow** from the menu.
![](./images/regression5.png " ")

  **Result**: The Create Workflow window appears.

2. In the Create Workflow window, enter **Predicting_Customer_Value** as the name and click **OK**.

![](./images/regression6.png " ")

  **Result:**
In the middle of the SQL Developer window, an empty workflow canvas opens with the name that you specified.On the right-hand side of the interface, the Component Palette tab of the Workflow Editor appears (shown below with a red border).

In addition, three other Oracle Data Miner interface elements are opened:

o	The Thumbnail tab

o	The Workflow Jobs tab

o	The Property Inspector tab

![](./images/regression7.png " ")

3. The first element of any workflow is the source data. We will extract data from a JSON table and a XM table. Here, we cannot directly add a data source. We will use a query editor to read the tables in a relational table format. You add a Data Source node to the workflow, and select the JSON_PURCHASEORDER and XML_PURCHASEORDER tables as the data source.
In the Component Palette, click the **Data** category. A list of data nodes appear, as shown here:
![](./images/regression8.png " ")

We will add a  RDBMS regular table data, using a data source. This is the JSON and XML combined table ()
Drag and drop the **Data Source** node onto the Workflow pane.

**Result**: A Data Source node appears in the Workflow pane and the Define Data Source wizard opens.
![](./images/regression9.png " ")

4. In Step 1 of the wizard, select FINAL_JSON_XML_DATA from the Available Tables/Views list, as shown here:

![](./images/regression10.png " ")

**Note**: You may use the two tabs in the bottom pane in the wizard to view and examine the selected table. The Columns tab displays information about the table structure, and the Data tab shows a subset of data from the selected table or view.

Click **Next** to continue.

5. In Step 2 of the wizard, you may remove individual columns that you do not need in your data source. In our case, we will keep all of the attributes that are defined in the table.
At the bottom of the wizard window, click **Finish**.

![](./images/regression11.png " ")


**Result**: As shown below, the data source node name is updated with the selected table name, and the properties associated with the node are displayed in the Property Inspector, located below the Component Palette pane.

![](./images/regression12.png " ")

**Notes:**

•	You can resize nodes in the workflow canvas by entering or selecting a different value from the Zoom options. Notice that 75% has been selected from the Zoom pull-down list.

•	You can add descriptive information about any node by using the Details tab in the Property Inspector.

•	The Thumbnail tab also provides a smaller display of the larger workflow window. As you drag nodes around the workflow window, the thumbnail view automatically adjusts.

**Examine the Source Data**

You can use an Explore Data node to examine the source data. Although this is an optional step, Oracle Data Miner provides this tool to enable you to verify if the selected data meets the criteria to solve the stated business problem.
Follow these steps:
1. Drag and drop the Explore Data node from the Component Palette to the Workflow, like this:

![](./images/regression13.png " ")

**Result**: A new Explore Data node appears in the workflow pane, as shown here. (As before, a node name is automatically generated.)

**Notes:** A yellow Information (!) icon in the border around any node indicates that it is not complete. Therefore, at least one addition step is required before the Explore Data node can be used.
In this case, a data source node must be "linked" to the Explore Data node to enable further exploration of the source data.

2.	To link the data source and explore data nodes, use the following instructions:

Right-click the data source node (DATA_RELTN), select Connect from the pop-up menu, and then drag the pointer to the Explore Data node, as shown here:

![](./images/regression14.png " ")

3. Then, click the Explore Data node to connect the two nodes. The resulting display looks like this:

![](./images/regression15.png " ")

Double-click the Explore Data node to display the Select Attributes window.In the Group By list, select the CUSTOMER_ID attribute, as shown here:

![](./images/regression16.png " ")

Then, click **OK**.

**Note:** The Select Attributes window also allows you to remove (or re-add) any attributes from the source data.

4. Next, right-click the Explore Data node and select **Run**.

![](./images/regression17.png " ")

**Result:**

o	Data Miner displays status information in the Workflow Jobs tab while processing the node.

o	When the update is complete, the data source and explore data nodes show a green check mark in the borders, like this:

![](./images/regression18.png " ")

**Note:** When you run any process from the workflow canvas, the steps that you have specified are executed by the Oracle Data Miner Server.

5. To see results from the Explore Data node, perform the following:
Right-click the Explore Data node and select View Data from the menu

![](./images/regression19.png " ")


**Result:** A new tab opens for the data profile node, as shown below

![](./images/regression20.png " ")

**Notes:**
Data Miner calculates a variety of information about each attribute in the data set, as it relates to the "Group By" attribute that you previously defined, including a Histogram, Distinct Values, Mode, Average, Min and Max value, Standard Deviation, Variance, Skewness, and Kurtosis.
o	The display enables you to visualize and validate the data, and also to manually inspect the data for patterns or structure.

Select any of the attributes in the Name list to display the associated histogram in the bottom window.

When you are done examining the source data, dismiss the Explore Data tab by clicking the Close icon (X). 

Next, you move from a high-level manual analytic exercise to using the power of database data mining.

6. Save the workflow by clicking the Save All icon in main toolbar.

![](./images/regression21.png " ")

**Build the Models**

In this topic, you build the selected models against the source data. This operation is also called “training” a model, and the model is said to “learn” from the training data.

A common data mining practice is to build (or train) your model against part of the source data, and then to test the model against the remaining portion of your data. By default, Oracle Data Miner this approach.

The models have the same build data and the same target.

By default, the models are all tested. The test data is created by randomly splitting the build data into a build data set and a test data set. The default ratio for the split is 60 percent build and 40 percent test. When possible Data Miner uses compression when creating the test and build data sets.

In the Workflow Editor, expand Models, and click Regression.

Drag and drop the node from the Components pane to the Workflow pane.

The GUI shows that the node has no data associated with it. Therefore, it cannot be built.

![](./images/regression22.png " ")

Right-click, and click Connect the data to regression node. Drag the line to the Regression node and click again

The **Edit Regression Build Node** dialog box opens. 

The Build tab enables you to specify or change the characteristics of the models to build. To edit the characteristics of the model to build, follow these steps:

o	In the Target field, select a target from the drop-down list. The list consist of attributes from the table or view specified in the Data Source node that is connected to the build node. For our use case, we select the TOTALAMOUNT_SUM column
You must specify a target. All models in the node have the same target.
o	In the Case ID field, select one attribute from the drop-down list. This attribute must uniquely identify a case. We will select the column CUSTOMERID.

In the Models Settings list, select which models you want to build. You can build Support Vector Machine (SVM) and Generalized Linear Models (GLM). You can delete any of these models by selecting the model and clicking
To delete any model, select the model and click x. We will keep both the models. 

![](./images/regression23.png " ")

Right Click on the **Regression** node and select **Run**

![](./images/regression24.png " ")

**Compare the Models**

After you build/train the selected models, you can view and evaluate the results for all of the models in a comparative format. Here, you compare the relative results of all four classification models.

Follow these steps:

Right-click the classification build node and select **Compare Test Results** from the menu.

![](./images/regression25.png " ")

**Results:** A Class Build display tab opens, showing a graphical comparison of the four models, as shown here:

The **Performance** tab displays the test results for several common test metrics. The **Performance** tab for **Regression** model show these measures for all models:

By default, All Measures are displayed. The selected measures are displayed as graphs. Since you are comparing test results for two models, then the different models have graphs in different colors.

**Predictive Confidence:** Predictive Confidence provides an estimate of accurate the model is. Predictive Confidence is a number between 0 and 1. Oracle Data Miner displays Predictive Confidence as a percentage. For example, the Predictive Confidence of 59 means that the Predictive Confidence is 59 percent (0.59).  Measures how much better the predictions of the mode are than those of the naive model. 

**Mean Absolute Error:** The Mean Absolute Error (MAE) is the average of the absolute value of the residuals (error).

**Root Mean Square Error:** The Root Mean Squared Error (RMSE) is the square root of the average squared distance of a data point from the fitted line.

**Mean Predicted Value:** The average of the predicted values.

**Mean Actual Value:** The average of the actual values.

![](./images/regression26.png " ")

The **Residual Plot tab** shows the Residual Plot for each model. You can compare two plots side by side.
The **residual plot** is a scatter plot of the residuals. Each residual is the difference between the actual value and the value predicted by the model. Residuals can be positive or negative. If residuals are small (close to 0), then the predictions are accurate. A residual plot may indicate that predictions are better for some classes of values than others.

The bottom pane show the Residual result summary table. The table contains the Models grid which supplements the information presented in the plots. You can minimize the table using the splitter line.

The table has the following columns:

o	Model, the name of the model along with color of the model in the graphs

o	Predictive Confidence

o	Mean Absolute Error

o	Root Mean Square Error

o	Mean Predicted Value

o	Mean Actual Value

o	Algorithm

o	Creation Date (and time)

By default, results for all models in the node are displayed

![](./images/regression27.png " ")

**Select and Examine a Specific Model**


Using the analysis performed in the past topic

![](./images/regression28.png " ")

The **Coefficients** Tab shows the Regression Coefficients. When you build a multivariate linear regression model, the algorithm computes a coefficient for each of the predictors used by the model. The coefficient is a measure of the impact of the predictor x on the target y.

![](./images/regression29.png " ")

**Apply the Model**

In this topic, you apply the Regression model and then create a table to display the results. You "apply" a model in order to make predictions - in this case to predict which customers are likely to buy insurance.

To apply a model, you perform the following steps:

First, specify the desired model (or models) in the Class Build node.

Then, you add a new Data Source node to the workflow. (This node will serve as the "Apply" data.)

Next, add an Apply node to the workflow.

Finally, you link both the Class Build node and the new Data Source node to the Apply node.
Follow these steps to apply the model and display the results:

In the Workflow Editor, expand **Model Operations**, and click **Apply**. Drag and drop the **Apply** node in the Workflow pane.

![](./images/regression30.png " ")

Link the Data node, Model nodes, and Build nodes to the Apply Node.  Since we do not have a separate dataset for test data, we will connect the same dataset to the apply node. Alternatively, you can use the sample node to create a separate train data and the remaining data can be used as test data.

The Apply node takes a collection of models and returns a single score. The Apply node produces a query as the result. The result can further transformed or connected to a Create Table or View node to save the data as a table.

To make predictions using a model, you must apply the model to new data. This process is also called scoring the new data.

Right Click and select **Edit** in the context menu.  In the **Edit Apply Node** wizard, uncheck automatic settings.  Select CUSTOMERID as the Case ID.  Now delete the columns Prediction Upper Bounds (PBUP) and Prediction Lower Bounds (PBLW) using the x symbol as shown in the image below.  Click **Ok**. 

![](./images/regression31.png " ")

Right Click on Apply node and select Run to execute the node. 

![](./images/regression32.png " ")

After Successful execution, right click on Apply node and select View Data. 

![](./images/regression33.png " ")

An automatic setting that returns the best prediction for the model. The data type returned depends on the target value type used during the build of the model.

![](./images/regression34.png " ")

**Summary:**

In this workshop, you examined and solved a "Regression" prediction data mining business problem by using the Oracle Data Miner graphical user interface, which is included as an extension to SQL Developer.
In this lab, you have learned how to:

o	Identify Data Miner interface components

o	Create a Data Miner project

o	Build a Workflow document that uses Regression models to predict customer behavior.

## STEP 3: MBA

1. Start creating a Data Miner Project

Before you begin working on a Data Miner Workflow, you must create a Data Miner Project, which serves as a container for one or more Workflows.
Create a SQL Developer connection for a data mining user named dmuser. This user has access to the sample data that you will be mining.
Note: If you have not yet set up Oracle Data Miner, or have not created the data mining user, you must first complete the tasks presented in the tutorial Setting Up Oracle Data Miner 19c Release 2,
To create a Data Miner Project, perform the following steps:

1. In the Data Miner tab, right-click the data mining user connection that you previously created, and select **New Project**, as shown here:

![](./images/mba1.jpg " ")

2. In the Create Project window, enter a project name (in this example MBA) and then click **OK**.

![](./images/mba2.jpg " ")

Note: You may optionally enter a comment that describes the intentions for this project. This description can be modified at any time.

Result: The new project appears below the data mining user connection node.

![](./images/mba3.jpg " ")

2. Build a Data Miner Workflow

A Data Miner Workflow is a collection of connected nodes that describe a data mining processes.

A workflow:

•	Provides directions for the Data Mining server. For example, the workflow says, "Build a model with these characteristics." The data-mining server builds the model with the results returned to the workflow.
•	Enables you to interactively build, analyze, and test a data mining process within a graphical environment.
•	Might be used to test and analyze only one cycle within a particular phase of a larger process, or it may encapsulate all phases of a process designed to solve a particular business problem.

3. Sample Data Mining Scenario

In this topic, you will use the Market Basket Analysis technique for better understanding customer purchasing patterns

To accomplish this goal, you build a workflow that enables you to:

•	Use Market Basket Analysis technique to understand customer-purchasing patterns. 
•	Select and run the models that produce the most actionable results

To create the workflow for this process, perform the following steps.

4. Create a Workflow and Add data for the workflow

1.	Right-click your project (Retail_Data_Analysis) and select New Workflow from the menu. 
 
![](./images/mba4.jpg " ")
 
 Result: The Create Workflow window appears.

 2. In the Create Workflow window, enter Association_Rules as the name and click OK.

 ![](./images/mba5.jpg " ")

 Result:

•	In the middle of the SQL Developer window, an empty workflow canvas opens with the name that you specified.
•	On the right-hand side of the interface, the Component Palette tab of the Workflow Editor appears (shown below with a red border).
•	In addition, three other Oracle Data Miner interface elements are opened:
o	The Thumbnail tab
o	The Workflow Jobs tab
o	The Property Inspector tab

![](./images/mba6.jpg " ")

3. The first element of any workflow is the source data. We will extract data from JSON and XML table.

3.1 In the Component Palette, click the **Data** category. A list of data nodes appear, as shown here:

![](./images/mba7.jpg " ")

3.2 We will add a  RDBMS regular table data, using a data source. This is the JSON and XML combined table ()

 Drag and drop the **Data Source** node onto the Workflow pane.

Result: A Data Source node appears in the Workflow pane and the Define Data Source wizard opens.

![](./images/mba8.jpg " ")

In Step 1 of the wizard:

3.3 Select JSON_XML_REL_COMBINED from the Available Tables/Views list, as shown here:

![](./images/mba9.jpg " ")

Note: You may use the two tabs in the bottom pane in the wizard to view and examine the selected table. The Columns tab displays information about the table structure, and the Data tab shows a subset of data from the selected table or view.

3.4 Click Next to continue.

4. In Step 2 of the wizard, you may remove individual columns that you do not need in your data source. In our case, we will keep all of the attributes that are defined in the table.

At the bottom of the wizard window, click Finish.

![](./images/mba10.jpg " ")

Result: As shown below, the data source node name is updated with the selected table name, and the properties associated with the node are displayed in the Property Inspector, located below the Component Palette pane.

![](./images/mba11.jpg " ")

4.1. Similarly add another source table TRANSFORMED_REL_DATA into the workflow.

![](./images/mba12.jpg " ")

![](./images/mba13.jpg " ")

5. Build the Models

In this topic, you build the selected models against the source data. This operation is also called “training” a model, and the model is said to “learn” from the training data.

A common data mining practice is to build (or train) your model against part of the source data, and then to test the model against the remaining portion of your data. By default, Oracle Data Miner this approach.

In the Workflow Editor, expand Models, and click Association.

Drag and drop the node from the Components pane to the Workflow pane.

![](./images/mba14.jpg " ")

Connect the association model with the data source **(TRANSFORMED_REL_DATA)**, which will open the following window. There, you need to specify a transaction as instructed below.  Click on the Edit icon as marked below. 

![](./images/mba15.jpg " ")

	Select **CUSTOMERID** and **INVOICENO** as the transaction Id.
	Select **DESCRIPTION** as the Item Id.
	Apriori is selected as the default association algorithm. Keep it as it is.


![](./images/mba16.jpg " ")  ![](./images/mba17.jpg " ")

Click on OK button.

![](./images/mba18.jpg " ")

Now right-click on the association and select Run. You will see the following analysis model. After successful execution, a green tick is visible on the association node.

![](./images/mba19.jpg " ")  ![](./images/mba20.jpg " ")

Right-click on the “Assoc Build” and then click on View Models

![](./images/mba21.jpg " ")

It will display the results as shown in the following screenshot.

![](./images/mba22.jpg " ")

Drag another association node to the canvas and connect it to the **JSON_XML_REL_COMBINED** data. We can repeat the exact same steps for this association node and then we the model result.

![](./images/mba23.jpg " ")

Below is the association rules for the JSON_XML data.

![](./images/mba24.jpg " ")

6. Interpreting the results of the market basket analysis

Referring to the association rules of the relational data table, there are almost 1386 association rules generated from the analysis we did. That’s a lot. So, we can basically interpret the results shown in Data Miner with rationale such as:

“If a customer buys REGENCY TEA PLATE GREEN  AND REGENCY TEA PLATE ROSES (refer to the first line of the result set), that person is likely to buy REGENCY TEA PLATE PINK. This can be stated with a 80.12% confidence level.”

And, its all about the level of confidence. This is where decisions can be made with the belief that structuring an association on grouping the two or more items together is more likely to be successful.

You can sort the rule result set by confidence level. Each of these rules discovered through the database analytics we just did will help the organization improve how it does business.

The Association Rules model measures the raw and conditional probabilities for the co-occurrence of attribute values.

The Support is the probability that all items in the rule (in both the “If” clause and the “Then” clause) will be found together in a checkout basket, and the Confidence is the conditional probability that the item(s) in the “then” clause are found, given that the item(s) in the “If” clause are present.

You can automate this data mining execution to create a result set and export it to CSV files(s) or store it in a database for immediate retrieval in an ETL process or directly in Oracle BI. This makes the ability to have some near real time data mining activity take place within the organization and potentially even compare business or data mining logic with some level of dynamic variation and control.

**Summary:**

In this workshop, you examined and solved a "Association" data mining business problem by using the Oracle Data Miner graphical user interface, which is included as an extension to SQL Developer.

In this tutorial, you have learned how to:

o	Identify Data Miner interface components
o	Create a Data Miner project
o	Build a Workflow document that uses Market Basket Analysis models to uncover association between items purchased together and identify patterns of co-occurrence.

## STEP 4: Clustering

**1: Start creating a Data Miner Project**

Before you begin working on a Data Miner Workflow, you must create a Data Miner Project, which serves as a container for one or more Workflows.

In the tutorial Setting Up **Oracle Data Miner 11g Release 2**, you learned how to create a database account and SQL Developer connection for a data mining user named dmuser. This user has access to the sample data that you will be mining.

***Note: If you have not yet set up Oracle Data Miner, or have not created the data mining user, you must first complete the tasks presented in the tutorial Setting Up Oracle Data Miner 19c Release 2,***

To create a Data Miner Project, perform the following steps:

1.	In the Data Miner tab, right-click the data mining user connection that you previously created, and select **New Project**, as shown here:

  ![](./images/clustering_6.jpg " ") 
 
2.	In the Create Project window, enter a project name (in this example Clustering) and then **click OK**.

  ![](./images/clustering_7.png " ")
 
***Note: You may optionally enter a comment that describes the intentions for this project. This description can be modified at any time.***

**Result:** The new project appears below the data mining user connection node.

  ![](./images/clustering_8.png " ")
  
 
**Build a Data Miner Workflow**

A Data Miner Workflow is a collection of connected nodes that describe a data mining processes.

A workflow:
- Provides directions for the Data Mining server. For example, the workflow says, "Build a model with these characteristics." The data-mining server builds the model with the results returned to the workflow.
- Enables you to interactively build, analyze, and test a data mining process within a graphical environment.
- Might be used to test and analyze only one cycle within a particular phase of a larger process, or it may encapsulate all phases of a process designed to solve a particular business problem.
  
What Does a Data Miner Workflow Contain?

Visually, the workflow window serves as a canvas on which you build the graphical representation of a data mining process flow, like the one shown here:

  ![](./images/clustering_9.jpg " ")

***Notes:***
  - Each element in the process is represented by a graphical icon called a node.
  - Each node has a specific purpose, contains specific instructions, and may be modified individually in numerous ways.
  - When linked together, workflow nodes construct the modeling process by which your particular data mining problem is solved.
  
As you will learn, any node may be added to a workflow by simply dragging and dropping it onto the workflow area. Each node contains a set of default properties. You modify the properties as desired until you are ready to move onto the next step in the process.

**Sample Data Mining Scenario**

In this topic, you will create a data mining process that groups customers into clusters based on their attributes like items purchased, spending, location etc. This technique is called Clustering. Typically clustering is used in customer segmentation analysis to try an better understand what type of customers you have.

Like with all data mining techniques, Clustering will not tell you or give you some magic insight into your data. Instead, it gives you more information for you to interpret and add the business meaning to them. With Clustering, you can explore the data that forms each cluster to understand what it really means.
To accomplish this goal, you build a workflow that enables you to:

- Build and compare several Clustering models
- Select and run the models that produce the most actionable results
  
To create the workflow for this process, perform the following steps.

**2: Create a Workflow and Add data for the workflow**

1.	Right-click your project (Retail\_Data\_Analysis) and select New Workflow from the menu.

  ![](./images/clustering_10.jpg " ")
 
  Result: The Create Workflow window appears.
 
2.	In the Create Workflow window, enter Predicting\_Customer\_Value as the name and click OK.

  ![](./images/clustering_11.jpg " ")
 
  Result:
  - In the middle of the SQL Developer window, an empty workflow canvas opens with the name that you specified.
  - On the right-hand side of the interface, the Component Palette tab of the Workflow Editor appears (shown below with a red border).
    - In addition, three other Oracle Data Miner interface elements are opened:
    - The Thumbnail tab
    - The Workflow Jobs tab
    - The Property Inspector tab

  ![](./images/clustering_12.jpg " ")

3. The first element of any workflow is the source data. We will extract data from a JSON table and a XM table. Here, we cannot directly add a data source. We will use a query editor to read the tables in a relational table format. You add a Data Source node to the workflow, and select the JSON\_PURCHASEORDER and XML\_PURCHASEORDER tables as the data source.

  In the Component Palette, click the Data category. A list of data nodes appear, as shown here:

  ![](./images/clustering_13.png " ")

4. Defining the data we will used to Build our Cluster models

  We are going to divide the data in our FINAL\_JSON\_XML\_DATA into two data sets. The first data set will be used to build the Cluster models. The second data set will be used as part of the Apply node.

  To divide the data we are going to use the Sample Node that can be found under the Transformation tab of the Component Palette.


  Create your first Sample Node.
  Drag a sample node into the workflow and connect it with the data node.

  ![](./images/clustering_14.png " ") ![](./images/clustering_15.png " ")
        
  In the Settings tab of the Property Inspector set the sample size to 60% and in the Details tab rename the node to Sample Build. Select the Case ID a CUSTOMERID.

  ![](./images/clustering_16.png " ") ![](./images/clustering_17.png " ")
        
  Create a second Sample node and give it a sample size of 40%. Rename this node to Sample Apply. Select CUSTOMERID as Case ID.

  ![](./images/clustering_18.png " ") ![](./images/clustering_19.png " ")
                    
  Right click on each of these Sample nodes to run them and have them ready for the next step of building the Clustering models.
                                              
  ![](./images/clustering_20.png " ") ![](./images/clustering_21.png " ") ![](./images/clustering_22.png " ")

5. Save the workflow by clicking the Save All icon in main toolbar.
 
  ![](./images/clustering_23.png " ")

**3: Build the Models**

In this topic, you build the selected models against the source data. This operation is also called “training” a model, and the model is said to “learn” from the training data.

A common data mining practice is to build (or train) your model against part of the source data, and then to test the model against the remaining portion of your data. By default, Oracle Data Miner this approach.
The models have the same build data and the same target.

By default, the models are all tested. The test data is created by randomly splitting the build data into a build data set and a test data set. The default ratio for the split is 60 percent build and 40 percent test. When possible Data Miner uses compression when creating the test and build data sets.

To create the Clustering models, go to the Component Palette. Under the Models tab, select **Clustering**.
  ![](./images/clustering_24.png " ")
 
Move the mouse to the workflow worksheet, near the **FINAL\_JSON\_XML\_DATA** node and click the worksheet. The Clustering node will be created. Now we need to connect the data with the Clustering node. To do this right click on the **Sample Build** node and select **Connect** from the drop down list. Then move the mouse to the Clustering node and click. An arrowed line is created connecting the two nodes.

  ![](./images/clustering_25.png " ") ![](./images/clustering_26.png " ")
       
At this point, we can run the Clustering Build node or we can have a look at the setting for each algorithm.

**4: The Clustering Algorithm settings**

To setup the Cluster Build node you will need to double click on the node to open the properties window. The first thing that you need to do is to specify the Case ID (i.e. the primary key). In our example, this is the **CUSTOMERID**.
  ![](./images/clustering_27.png " ")

Oracle Data Miner has three clustering algorithms. The first of these is the **expectation-maximization** clustering, the second clustering algorithm is the well know **k-Means** (it is an enhanced version of it) and the third is O-Cluster. To look at the settings for each algorithm, click on the model listed under Model Settings and then click on the **Edit Advanced** icon as shown below.
  ![](./images/clustering_28.png " ") ![](./images/clustering_29.png " ")

A new window will open that lists all the attributes for the in the data source. The CUSTOMERID is unchecked as we said that this was the CASE_ID.

Click on the Algorithm Settings tab to see the internal settings for the **k-means algorithm**. All of these settings have a default value. Oracle has worked out what the optimal setting are for you. The main setting that you might want to play with is the Number of Clusters to build. The default is 10, but you might want to play with numbers between 5 and 15 depending on the number of clusters or segments you want to see in your data.

To view the algorithm settings for **O-Cluster** or **EM Cluster** click on this under the Model Setting. We have less internal settings to worry about here, but we again can determine how many clusters we want to produce.

For our scenario, we are going to take the default settings.
  ![](./images/clustering_30.png " ")

**5: Run/Generate the Clustering models**

At this stage we have the data set-up, the Cluster Build node created and the algorithm setting all set to what we want.
Now we are ready to run the Cluster Build node.

To do this, right click on the Cluster Build node and click run. ODM will go create a job that will contain PL/SQL code that will generate a cluster model based on K-Means and a second cluster model based on O-Cluster. This job is submitted to the database and when it is complete, we will get the little green tick mark on the top right hand corner of the Cluster Build node.
  ![](./images/clustering_31.png " ") ![](./images/clustering_32.png " ")
               
**6: View the Cluster Models**

To view the the cluster modes we need to right click the Cluster Build node and select View Models from the drop down list. We get an additional down down menu that gives the names of the three cluster models that were developed.

In my case, these are **CLUS\_EM_1\_8, CLUS\_KM\_1\_8 and CLUS\_OC\_1\_8**. You may get different numbers on your model names. These numbers are generated internally in ODM
The first one that we will look at will be the K-Mean Cluster Model (**CLUS\_KM\_1\_8**). 

Select this from the menu.
  ![](./images/clustering_33.png " ")
 
**7: View the Cluster Rules**

The hierarchical K-Mean cluster mode will be displayed. You might need to readjust/resize some of the worksheets/message panes etc in ODM to get the good portion of the diagram to display.
    
  ![](./images/clustering_34.png " ") ![](./images/clustering_35.png " ")

  With ODM you cannot change, alter, merge, split, etc. any of the clusters that were generated. 

  To see that the cluster rules are for each cluster you can click on a cluster. When you do this you should get a pane (under the cluster diagram) that will contain two tabs, Centroid and Cluster Rule.

  The Centroid tab provides a list of the attributes that best define the selected cluster, along with the average value for each attribute and some basic statistical information.

  ![](./images/clustering_36.png " ")  ![](./images/clustering_37.png " ")
 
  For each cluster in the tree we can see the number of cases in each cluster the percentage of overall cases for this cluster. Work your way down the tree exploring each of the clusters produced.

  The further down the tree you go the smaller the percentage of cases will fall into each cluster.

**8: Compare Clusters**

In addition to the cluster tree, ODM also has two addition tabs to allow us to explore the clusters. These are Cluster and Compare tabs.

  ![](./images/clustering_38.png " ")

  Click on the Cluster tab. We now get a detailed screen that contain various statistical information for each attribute. We can for each attribute get a histogram of the values within each attribute for this cluster.

  We can use this important to start building up a picture of what each cluster might represent based on the values (and their distribution) for each cluster.

  ![](./images/clustering_39.png " ")
 
**9: Multi-Cluster – Multi-variable Comparison of Clusters**

The next level of comparison and evaluation of the clusters can be found under the Compare tab.
This lets us compare two clusters against each other at an attribute level. For example, let us compare cluster 3 and 11. The attribute and graphics section is updated to reflect the data for each of cluster. These are color coded to distinguish the two clusters.

  ![](./images/clustering_40.png " ")
 
  We can work our way down through each attribute and again we can use this information to help us to understand what each cluster might represent.

  An additional feature here is that we can do multi-variable (attribute) comparison. Holding down the control button select STATE, UNITPRICE\_SUM and QUANTITY\_SUM. With each selection, we get a new graph appearing at the bottom of the screen. This shows the distribution of the values by attribute for each cluster.  We can learn a lot from this.

  ![](./images/clustering_41.png " ")

  So one possible conclusion we could draw from this data would be that Cluster 3 has customers from Arkansas and Cluster 11 has customers only from Louisiana.

**10: Renaming Clusters**

When you have discovered a possible meaning for a Cluster, you can give it a meaningful name instead of it having a number. In our example, we would like to re-label Cluster 3 to ‘Arkansas Customers’. To do this click on the Edit button that is beside the drop down that has cluster 3. Enter the new label and click OK.

  ![](./images/clustering_42.png " ")
 
  In the drop down, we will now get the new label appearing instead of the cluster number.
    Similarly, we can do this for the other cluster **e.g. ‘Louisiana Customer’**.

  ![](./images/clustering_43.png " ")
 
  We have just looked at how to explore our **K-Means** model. You can do similar exploration of the **O-Cluster** and **EM** (**expectation maximization**) model.
  We have now explored our clusters and we have decided which of our Clustering Models best suits our needs. In our scenario, we are going to select the **K-Mean** model to apply and label our new data.

**11: Create the Apply Node**

We have already setup our sample of data that we are going to use as our Apply Data Set. We did this when we setup the two different Sample node.

We are going to use the Sample node that was set to 40%.

The first step requires us to create an Apply Node. This is under the Model Operations tab, in the components panel. Click on the Apply node, move the mouse to the workflow worksheet and click near the Sample Apply node.

  ![](./images/clustering_44.png " ") 
 
  To connect the two nodes, move the mouse to the Sample Apply node and right click. Select Connect from the drop down menu and then move the mouse to the Apply node and click again. A connection arrow appears joining these nodes.

  ![](./images/clustering_45.png " ") ![](./images/clustering_46.png " ")
             
**12: Specify the Clustering Model to use & Output Data**

Now we will select the clustering model we want to apply to our new data.
We need to connect the **Cluster Build** node to the **Apply** node. Move the mouse to the Cluster Build node; **right click** and select connect from the drop down menu. Move the mouse to the **Apply** node and click. We get the connection arrow between the two nodes.

  ![](./images/clustering_47.png " ")
 
  The final step is to specify what clustering mode we would like to use. In our scenario, we are going to specify the K-Mean model.

  (Single) Click the Cluster Build node. We now need to use the Property Inspector to select the K-Means model for the apply set. 

  ![](./images/clustering_48.png " ")
 
  In the Models tab of the Property Inspector, we should have our three cluster models listed. Under the Output column click in the box for the O-Cluster and EM Cluster, model. We should now get a little red ‘x’ mark appearing. The K-Mean model should still have the green arrow under the Output column.

  ![](./images/clustering_49.png " ")
 

**13: Run the Apply Node**

We have one last data setup to do on the Apply node. We need to specify what data from the apply data set we want to include in the output from the Apply node.  For simplicity, we will include the primary key, but you could include all the attributes.  In addition to including the attributes from the apply data source, the Apply Node will also create some attributes based on the Cluster model we selected. In our scenario, the K-Means model will create two additional attributes. One of these will contain the Cluster ID and the other attribute will be the probability of the cluster being valid.

To include the attributes from the source data, double click on the Apply node. This will open the Edit Apply Node window. You will see that it already contains the two attributes that will be created by the K-Mean model.

  ![](./images/clustering_50.png " ")
 
  To add the attributes from the source data, click on the **Additional Output tab**, click in the **reset** option and then click on the green **‘+’** symbol. For simplicity, just select the CUSTOMERID. Click the OK button to finish.

  ![](./images/clustering_51.png " ")
 
  Now we are ready to run the Apply node. To do this right click on the Apply Node and select Run from the drop down menu.

  ![](./images/clustering_52.png " ")
 
  When everything is completed, you will get the little green tick mark on the top right hand corner of the Apply node.

  ![](./images/clustering_53.png " ")
 
**14: View the Results**

To view the results and the output produced by the Apply node, right click on the Apply node and select View Data from the drop down menu.

We get a new tab opened in SQL Developer that will contain the data. This will consist of the CUSTOMERID, the K-means Cluster ID and the Cluster Probability. You will see that the some of the clusters assigned will have a number and some will have the cluster labels that we assigned in a previous step.

  ![](./images/clustering_54.png " ")
 
  It is now up to you to decide how you are going to use this clustering information in an operational or strategic way in your organization.

**Summary**
In this workshop, you examined and solved a "Clustering" data mining business problem by using the Oracle Data Miner graphical user interface, which is included as an extension to SQL Developer.

 In this tutorial, you have learned how to:

  -  Identify Data Miner interface components
  - Create a Data Miner project
  - Build a Workflow document that uses Clustering models for market research to segment the customers based  on their choice and preference.

## Learn More
 - [ML](https://www.oracle.com/in/data-science/machine-learning/what-is-machine-learning/)
 - [ML Offerings](https://blogs.oracle.com/machinelearning/machine-learning-in-oracle-database)

## Rate this Workshop
When you are finished don't forget to rate this workshop!  We rely on this feedback to help us improve and refine our LiveLabs catalog.  Follow the steps to submit your rating.

1.  Go back to your **workshop homepage** in LiveLabs by searching for your workshop and clicking the Launch button.
2.  Click on the **Brown Button** to re-access the workshop  

   ![](https://raw.githubusercontent.com/oracle/learning-library/master/common/labs/cloud-login/images/workshop-homepage-2.png " ")

3.  Click **Rate this workshop**

   ![](https://raw.githubusercontent.com/oracle/learning-library/master/common/labs/cloud-login/images/rate-this-workshop.png " ")

<!-- If you selected the **Green Button** for this workshop and still have an active reservation, you can also rate by going to My Reservations -> Launch Workshop. -->

## Acknowledgements
* **Authors** - Balasubramanian Ramamoorthy, Amith Ghosh
* **Contributors** - Laxmi Amarappanavar, Ashish Kumar, Priya Dhuriya, Maniselvan K, David Start, Rene Fontcha, Pragati Mourya.
* **Last Updated By/Date** - Rene Fontcha, LiveLabs Platform Lead, NA Technology, March 2021

## Need Help?
Please submit feedback or ask for help using our [LiveLabs Support Forum](https://community.oracle.com/tech/developers/categories/livelabsdiscussions). Please click the **Log In** button and login using your Oracle Account. Click the **Ask A Question** button to the left to start a *New Discussion* or *Ask a Question*.  Please include your workshop name and lab name.  You can also include screenshots and attach files.  Engage directly with the author of the workshop.

If you do not have an Oracle Account, click [here](https://profile.oracle.com/myprofile/account/create-account.jspx) to create one.


