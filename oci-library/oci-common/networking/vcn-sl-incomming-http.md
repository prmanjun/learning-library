## **Configure Security List to allow HTTP inbound connections**

Create the rules in the default security list that will allow incomming comnections on ports 80/TCP and 443/TCP

1. Click View Virtual Cloud Network to view your new VCN.

2. With your new VCN displayed, click on your Public subnet link.

    The public subnet information is displayed with the Security Lists at the bottom of the page. There should be a link to the Default Security List for your VCN.

3. Click the **Default Security List** link.
    
    The default Ingress Rules for your VCN are displayed.
4. Click Add Ingress Rules.

    An **Add Ingress Rules** dialog is displayed.

5. Enter the following:

* Stateless: Checked
* Source Type: CIDR 
* Source CIDR: 0.0.0.0/0
* IP Protocol: TCP
* Source port range: (leave-blank)
* Destination Port Range: 80
* Description: Allow HTTP connections
        
Once you click Add Ingress Rule, inbound HTTP connections from the specified are allowed to the subnet.

6. Repeat the steps from 1-4 and enter the following:

* Stateless: Checked
* Source Type: CIDR 
* Source CIDR: 0.0.0.0/0
* IP Protocol: TCP
* Source port range: (leave-blank)
* Destination Port Range: 443
* Description: Allow HTTPS connections

Once you click Add Ingress Rule, inbound HTTPS connections from the specified are allowed to the subnet.