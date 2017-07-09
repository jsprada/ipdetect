# ipdetect
Detect a new IP address used on a subnet. 

Specifically, I created this script to easily find the IP address of a new headless computer, like a Raspberry Pi on the network.  This is a tool I developed for my own necesseity, feel free to use it as you wish.

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

Make the script executable 

    $ chmod +x ipdetect

Run it

    $ ./ipdetect

## Setup
Edit `ipdetect` file.  There are two variables near the beginning of the script, `ip_range` and `ignore_list`

### ip_range
The subnet that you wish to scan.  
For example, to scan a 192.168.1.x subnet, use `192.168.1.0/24`  to scan a 10.0.0.x subnet, use `10.0.0.0/24`

### ignore_list
A list of IP addresses to ignore.  This is useful if you have a wifi device (printer, tablet, laptop) that bobs on and off the network

## Use

Run the script, it will start scanning.  Start up your new device on the netowrk. When found, the new address will be displayed and the script will stop.   


## Todo
* objectify/cleanup/reorganize
