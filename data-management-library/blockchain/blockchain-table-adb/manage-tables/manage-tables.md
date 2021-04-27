# Manage Blockchain Tables (lab in Development)

## Introduction

Blockchain tables are append-only tables in which only insert operations are allowed. Deleting rows is either prohibited or restricted based on time. Rows in a blockchain table are made tamper-resistant by special sequencing & chaining algorithms. Users can verify that rows have not been tampered. A hash value that is part of the row metadata is used to chain and validate rows.

Blockchain tables enable you to implement a centralized ledger model where all participants in the blockchain network have access to the same tamper-resistant ledger.

A centralized ledger model reduces administrative overheads of setting a up a decentralized ledger network, leads to a relatively lower latency compared to decentralized ledgers, enhances developer productivity, reduces the time to market, and leads to significant savings for the organization. Database users can continue to use the same tools and practices that they would use for other database application development.

This lab walks you through the steps to create a Blockchain table, insert data, manage the rows in the table and manage the blockchain table.

Estimated Lab Time: 30 minutes

### Objectives

In this lab, you will:

* Create the Blockchain table and insert rows
* Manage blockchain tables and rows in a blockchain table
* Create a certificate directory and add your certificate
* Sign a row in the blockchain table
* Check the validity of rows in the blockchain table with and without signature

### Prerequisites

* An Oracle Free Tier, Always Free, Paid or LiveLabs Cloud Account
* Provisioned an Oracle Database 21c Instance
* Have successfully completed the Setup lab

## **STEP 1:** Create a blockchain table

1. The `CREATE BLOCKCHAIN TABLE` statement requires additional attributes. The `NO DROP`, `NO DELETE`, `HASHING USING`, and `VERSION` clauses are mandatory.

    Create a Blockchain table named `bank_ledger` that will maintain a tamper-resistant ledger of current and historical transactions using the SHA2_512 hashing algorithm. Rows of the `bank_ledger` blockchain table can never be deleted. Moreover the blockchain table can be dropped only after 16 days of inactivity.

	```
	<copy>
	CREATE BLOCKCHAIN TABLE bank_ledger (bank VARCHAR2(128), deposit_date DATE, deposit_amount NUMBER)
	NO DROP UNTIL 16 DAYS IDLE
	NO DELETE LOCKED
	HASHING USING "SHA2_512" VERSION "v1";
	</copy>
	```

	![](./images/table-created.png " ")

2. Describe the `bank_ledger` blockchain table to view the columns. Notice that the description displays only the visible columns.

	```
	<copy>
	DESC bank_ledger;
	</copy>
	```

	![](./images/describe.png " ")

## **STEP 2:** Insert rows into the blockchain table

1. Insert records into the `bank_ledger` blockchain table.

	```
	<copy>
	INSERT INTO bank_ledger VALUES (999,to_date(sysdate,'dd-mm-yyyy'),100);
	INSERT INTO bank_ledger VALUES (999,to_date(sysdate,'dd-mm-yyyy'),200);
	INSERT INTO bank_ledger VALUES (999,to_date(sysdate,'dd-mm-yyyy'),500);
	INSERT INTO bank_ledger VALUES (999,to_date(sysdate,'dd-mm-yyyy'),-200);
	INSERT INTO bank_ledger VALUES (888,to_date(sysdate,'dd-mm-yyyy'),100);
	INSERT INTO bank_ledger VALUES (888,to_date(sysdate,'dd-mm-yyyy'),200);
	INSERT INTO bank_ledger VALUES (888,to_date(sysdate,'dd-mm-yyyy'),500);
	INSERT INTO bank_ledger VALUES (888,to_date(sysdate,'dd-mm-yyyy'),-200);
	commit;
	</copy>
	```

	![](./images/insert.png " ")

2. Query the `bank_ledger` blockchain table to show the records.

	```
	<copy>
	select * from bank_ledger;
	</copy>
	```

	![](./images/select-all.png " ")

## **STEP 3:** View Blockchain tables and its internal columns

1. Run the command to view all the blockchain tables.

	```
	<copy>
	select * from user_blockchain_tables;
	</copy>
	```

2. Verify the attributes set for the blockchain table in the appropriate data dictionary view.

	```
	<copy>
	SELECT table_name, row_retention, row_retention_locked, table_inactivity_retention, hash_algorithm 
	FROM user_blockchain_tables;
	</copy>
    ```

3. Use the `USER_TAB_COLS` view to display all internal column names used to store internal information like the users number, the users signature.

	```
	<copy>
	SELECT table_name, internal_column_id "Col ID", SUBSTR(column_name,1,30) "Column Name", SUBSTR(data_type,1,30) "Data Type", data_length "Data Length"
	FROM user_tab_cols
	ORDER BY internal_column_id;
	</copy>
	```

4. Query the `bank_ledger` blockchain table to display all the values in the blockchain table including values of internal columns.

	```
	<copy>
	select bank, deposit_date, deposit_amount, ORABCTAB_INST_ID$,
	ORABCTAB_CHAIN_ID$, ORABCTAB_SEQ_NUM$,
	ORABCTAB_CREATION_TIME$, ORABCTAB_USER_NUMBER$,
	ORABCTAB_HASH$, ORABCTAB_SIGNATURE$, ORABCTAB_SIGNATURE_ALG$,
	ORABCTAB_SIGNATURE_CERT$ from bank_ledger;
	</copy>
	```

## **STEP 4:** Manage blockchain tables

When you try to manage the rows using update, delete, truncate you get the error `operation not allowed on the blockchain table` if the rows are not outside the retention period.

1. Update a record in the `bank_ledger` blockchain table by setting deposit\_amount=0.

	```
	<copy>
	update bank_ledger set deposit_amount=0 where bank=999;
	</copy>
	```

	![](./images/update.png " ")

2. Delete a record in the `bank_ledger` blockchain table.

	```
	<copy>
	delete from bank_ledger where bank=999;
	</copy>
	```

	![](./images/delete.png " ")

3. Truncating the table `bank_ledger`.

	```
	<copy>
	truncate table bank_ledger;
	</copy>
	```

	![](./images/truncate.png " ")


## **STEP 5:** Manage rows in a blockchain table

Similar to managing rows within the retention period, managing the blockchain table using alter, drop will throw an error.

1. Drop the table `bank_ledger`. It will drop successfully if no row exists in the table.

	```
	<copy>
	drop table bank_ledger;
	</copy>
	```

	![](./images/drop.png " ")

2. Alter the table `bank_ledger` to not delete the rows until 20 days after insert.

	```
	<copy>
	ALTER TABLE bank_ledger NO DELETE UNTIL 20 DAYS AFTER INSERT;
	</copy>
	```

	![](./images/alter-1.png " ")

3. Create another table `bank_ledger_2`.

	```
	<copy>
	CREATE BLOCKCHAIN TABLE bank_ledger_2 (bank VARCHAR2(128), deposit_date DATE, deposit_amount NUMBER)
	NO DROP UNTIL 16 DAYS IDLE
	NO DELETE UNTIL 16 DAYS AFTER INSERT
	HASHING USING "SHA2_512" VERSION "v1";
	</copy>
	```

	![](./images/create-new-table.png " ")

4. Alter the table `bank_ledger_2` by specifying that the rows cannot be deleted until 20 days after they were inserted.

	```
	<copy>
	ALTER TABLE bank_ledger_2 NO DELETE UNTIL 20 DAYS AFTER INSERT;
	</copy>
	```

	![](./images/alter-new-table.png " ")

5. Run the command to view all the blockchain tables.

	```
	<copy>
	select * from user_blockchain_tables;
	</copy>
	```

## **STEP 6:** Verify rows without signature

1. Verify the rows in blockchain table using DBMS\_BLOCKCHAIN\_TABLE.VERIFY_ROWS.

	```
	<copy>
	DECLARE
		verify_rows NUMBER;
		instance_id NUMBER;
	BEGIN
		FOR instance_id IN 1 .. 4 LOOP
			DBMS_BLOCKCHAIN_TABLE.VERIFY_ROWS('ADMIN','BANK_LEDGER',
	NULL, NULL, instance_id, NULL, verify_rows);
		DBMS_OUTPUT.PUT_LINE('Number of rows verified in instance Id '||
	instance_id || ' = '|| verify_rows);
		END LOOP;
	END;
	/
	</copy>
	```

	![](./images/verify.png " ")

2. DBA view of blockchain tables.

	```
	<copy>
	select * from dba_blockchain_tables;
	</copy>
	```

You may now [proceed to the next lab](#next).

## Acknowledgements

* **Author** - Rayes Huang, Mark Rakhmilevich, Anoosha Pilli
* **Contributors** - Anoosha Pilli, Product Manager, Oracle Database
* **Last Updated By/Date** - Anoosha Pilli, April 2021
