# ipdetect
Detect a new IP address used on a subnet. 

When building an IoT device, you can't connect to it using SSH until you know the IP address.   This is a simple utility that I created as a wrapper around an nmap ARP scan to find and report the IP address of a new device on the network. 

I created this script to make it easy to find the IP address of a new headless computer, like a Raspberry Pi, or an IoT device on the network.  This is a tool I developed for my own necessity, feel free to use it as you wish.   The underlying mechanism is an ARP scan, with a few extra features to make it more convenient.

Note: Only tested on Linux.

## Requirements

* Python 3
* python-libnmap module

##  Install

Get this repository

    $ git clone https://github.com/jsprada/ipdetect

Change into the directory

    $ cd ipdetect

Install the required Python modules

    $ sudo pip install -r requirements.txt

Make the script executable (optional)

    $ chmod +x ipdetect

Run it

    $ ./ipdetect
    
or (if you opt out of making it executable):

    $ pyhton ipdetect

## Setup
Edit `ipdetect` file.  There are two variables near the beginning of the script, `ip_range` and `ignore_list`

### ip_range
The subnet that you wish to scan.  
For example, to scan a 192.168.1.x subnet, use `192.168.1.0/24`  to scan a 10.0.0.x subnet, use `10.0.0.0/24`

### ignore_list
A list of IP addresses to ignore.  This is useful if you have a previously known wifi device, like a phone, printer, tablet, laptop, etc. that bobs on and off the network.   Add those addresses to this list, and `ipdetect` will ignore it.

## Use

Run the script from a computer on the network, it will start scanning.   First it will inventory the existing devices on the network and store these as a baseline scan.  Connect and start up your Pi or IoT device on the network.  When found, the new address will be displayed and the script will stop.   Press CTRL-C to stop the script manually.

Example output:

```
$ ./ipdetect
Starting scan on: 192.168.1.0/24. Press CTRL-C to stop
Ignoring ['192.168.1.140', '192.168.1.138']
Establishing baseline scan
 - 192.168.1.1 is up
 - 192.168.1.2 is up
 - 192.168.1.16 is up
 - 192.168.1.22 is up
 - 192.168.1.100 is up
 - 192.168.1.104 is up
 - 192.168.1.108 is up
 - 192.168.1.110 is up
 - 192.168.1.198 is up
Connect your new device now.
Scanning for new IPs
 - 192.168.1.1 is up
 - 192.168.1.2 is up
 - 192.168.1.16 is up
 - 192.168.1.22 is up
 - 192.168.1.100 is up
 - 192.168.1.104 is up
 - 192.168.1.110 is up
 - 192.168.1.140 is up
 - 192.168.1.198 is up
Ignoring ['192.168.1.140']
No new IPs detected yet
Scanning for new IPs
 - 192.168.1.1 is up
 - 192.168.1.2 is up
 - 192.168.1.16 is up
 - 192.168.1.22 is up
 - 192.168.1.100 is up
 - 192.168.1.104 is up
 - 192.168.1.105 is up
 - 192.168.1.108 is up
 - 192.168.1.110 is up
 - 192.168.1.140 is up
 - 192.168.1.198 is up
Scan stopped, new IP detected: ['192.168.1.105']

```


## Todo
* objectify/cleanup/reorganize/
* auto-detect IP range
* compile and add to AUR for Arch Linux users.
