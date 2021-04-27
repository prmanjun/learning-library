## **Configure Security List to allow MySQL inbound connections**

Create a rule in the **Security List for Private Subnet-*VCN Name*** security list that will allow incomming comnections on ports 3306/TCP and 33060/TCP

1. Click View Virtual Cloud Network to view your new VCN.

2. With your new VCN displayed, click on your Private subnet link.

    The private subnet information is displayed with the Security Lists at the bottom of the page. There should be a link to the **Security List for Private Subnet-*VCN Name*** for your private subnet.

3. Click the **Security List for Private Subnet-*VCN Name*** link.
    
    The default Ingress Rules for your VCN are displayed.

4. Click Add Ingress Rules.

    An **Add Ingress Rules** dialog is displayed.

5. Enter the following:

* Stateless:  Checked
* Source Type: CIDR
* Source CIDR: 10.0.0.0/24
* IP Protocol: TCP
* Source port range: (leave-blank)
* Destination Port Range: 3306
* Description: Allow MySQL connections
        
Once you click Add Ingress Rule, inbound MySQL connections from the specified are allowed to the subnet.

6. Repeat the steps from 1-4 and enter the following:

* Stateless: Checked
* Source Type: CIDR 
* Source CIDR: 10.0.0.0/24
* IP Protocol: TCP
* Source port range: (leave-blank)
* Destination Port Range: 33060
* Description: Allow MySQL X connections

Once you click Add Ingress Rule, inbound MySQL X connections from the specified are allowed to the subnet.