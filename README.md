# juniper_ztp

## **Abstract**
This infrastructure has the purpose of service as a ZTP staging environment to quickly deploy code and finalized configurations for Juniper devices.

**The devices in question capable of being automated by this environment are:**
* Juniper QFX
* Juniper EX
* Juniper SRX

![Alt text](images/ztp_staging.png?raw=true "Title")

**The lab is comprised of two major building blocks:**
* **Automation Server 1**
  * DHCP for handing out IP addresses to newly connected devices
  * FTP Server for target code and configuration file transfer to newly connected devices

* **Automation Server 2**
  * Ansible Core for DHCPD.conf file generation and push to Automation Server 1 where DHCP services are running

**Automation Server 1**
* **DHCP**
  * ISC2 DHCP server is running and will allow for the following options to be defined:
    * Option 43 sub-option 0: Specifies image file name
    * Option 43 sub-option 1: Specifies configuration file name
    * Option 150: Specifies Target Server IP address for newly connected devices to fetch files from 
     

* **FTP**

**Automation Server 2**

* dhcpd.conf generation

* dhcpd.conf push to Automation Server 1

