
from libnmap.process import NmapProcess
from libnmap.parser import NmapParser

class NewScan(object):
	def __init__(self, ip_range):
		self.ip_range = ip_range
		self.nmap_scan = self.new_scan()
		self.active_ips = self.getActiveIps()
	

	def new_scan(self):
		nm = NmapProcess(self.ip_range, options="-sP")
		rc = nm.run()
		return NmapParser.parse_fromstring(nm.stdout)
		

	def getActiveIps(self):
		ip_list = []
		hosts = self.nmap_scan.hosts

		for host in hosts:
			if host.status == "up":
				print(" - %s is up" % host.address)
				ip_list.append(host.address)
		return ip_list

	

	

	