import api
import time
from datetime import datetime
import tweett


stops = api.get_bus_stops()

pos = api.get_bus_positions()
print(pos)
print(stops[1]['lat'])
while(True):
	pos = api.get_bus_positions()
	stops = api.get_bus_stops()
	for ps in range(0,len(pos)):
		Ns = pos[ps]['nextStop']
		Sa = api.get_bus_stop(Ns)
		now = datetime.now()
		time_since_0 = (now - now.replace(hour=0, minute=0, second=0, microsecond=0)).total_seconds()
		for s in range(0,len(Sa)):
			for t in range(0,len(Sa[s]['times'])):
				if(time_since_0 == Sa[s]['times'][t]):
					temp = 0
					for i in stops:
						if(stops[i]['id'] == Ns):
							temp = i
					if(pos[ps]['lat'] != stops[temp]['lat'] and pos[ps]['lon'] != stops[temp]['lon']):
						tweett.tweet("Strætó númer {} er kannski seinn".format(pos[ps]['route']))
		time.sleep(16)
		print(ps)
	time.sleep(8)
	print("8")



